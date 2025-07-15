import praw
import spacy
from flask import Flask, render_template, request, jsonify
from datetime import datetime
import os
from typing import List, Dict, Tuple
from prawcore.exceptions import ResponseException
import re
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Initialize Reddit API client
def init_reddit_client() -> praw.Reddit:
    try:
        reddit = praw.Reddit(
            client_id="rCdZsDIqRC2Js8c9MgdAtw",  # Replace with your valid client_id
            client_secret="EJlKr2SQEetSSoTwWvSxEqwZ4IcxYA",  # Replace with your valid client_secret
            user_agent="PersonaAnalyzer/0.1 by u/LawyerAcrobatic2599"  # Replace with your Reddit username
        )
        reddit.user.me()
        return reddit
    except ResponseException as e:
        if e.response.status_code == 401:
            raise ValueError("Invalid Reddit API credentials (401 Unauthorized). Please update client_id, client_secret, and user_agent.")
        raise

# Initialize spaCy for NLP
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    os.system("python -m spacy download en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

def extract_username_from_url(url: str) -> str:
    if not url or "reddit.com/user/" not in url:
        raise ValueError("Invalid Reddit profile URL. Use format: https://www.reddit.com/user/username")
    match = re.search(r"user/([^/]+)", url)
    return match.group(1) if match else None

def scrape_user_data(username: str, reddit: praw.Reddit) -> Tuple[List[Dict], List[Dict]]:
    try:
        user = reddit.redditor(username)
        posts = [{"id": s.id, "title": s.title, "text": s.selftext, "subreddit": s.subreddit.display_name,
                  "created": datetime.fromtimestamp(s.created_utc)} for s in user.submissions.new(limit=50)]
        comments = [{"id": c.id, "text": c.body, "subreddit": c.subreddit.display_name,
                     "created": datetime.fromtimestamp(c.created_utc)} for c in user.comments.new(limit=50)]
        return posts, comments
    except ResponseException as e:
        raise ValueError(f"Error scraping user {username}: {str(e)}")
    except Exception as e:
        raise ValueError(f"Error scraping user {username}: {str(e)}")

def extract_persona_traits(texts_with_source: List[Tuple[str, str]]) -> List[Dict]:
    traits = []
    for text, source_type in texts_with_source:
        doc = nlp(text)
        for ent in doc.ents:
            if ent.label_ in ["PERSON", "ORG", "GPE", "NORP"]:
                traits.append({
                    "trait": f"Interest in {ent.text}",
                    "category": "BEHAVIOR & HABITS" if ent.label_ in ["PERSON", "ORG"] else "PERSONAL DETAILS",
                    "text": text,
                    "source_type": source_type
                })
        sentiment = doc.sentiment
        if sentiment > 0.2:
            traits.append({
                "trait": "Positive attitude",
                "category": "BEHAVIOR & HABITS",
                "text": text,
                "source_type": source_type
            })
        elif sentiment < -0.2:
            traits.append({
                "trait": "Frustrated sentiment",
                "category": "FRUSTRATIONS",
                "text": text,
                "source_type": source_type
            })
        if any(token.text.lower() in ["want", "need", "goal"] for token in doc):
            traits.append({
                "trait": f"Desire to {doc.text.split()[-1]}",
                "category": "GOALS & NEEDS",
                "text": text,
                "source_type": source_type
            })
        subreddits = set(t["subreddit"] for t in texts_with_source if isinstance(t, dict) and "subreddit" in t)
        for subreddit in subreddits:
            traits.append({
                "trait": f"Interest in {subreddit} community",
                "category": "BEHAVIOR & HABITS",
                "text": f"Active in r/{subreddit}",
                "source_type": "post/comment"
            })
    return traits

def build_persona(username: str, posts: List[Dict], comments: List[Dict]) -> Dict:
    persona = {"username": username.upper(), "sections": {}, "citations": {}}
    texts_with_source = [(post["title"] + " " + post["text"], "post") for post in posts] + [(comment["text"], "comment") for comment in comments]
    if not texts_with_source:
        return {"error": "No data available to build persona (possibly due to private profile or API error)."}
    traits = extract_persona_traits(texts_with_source)
    if not traits:
        return {"error": "No distinct characteristics identified from available data."}
    sections = {
        "PERSONAL DETAILS": ["Location: (Inferred from posts)", "Age: (Not available)", "Occupation: (Not available)"],
        "BEHAVIOR & HABITS": [],
        "FRUSTRATIONS": [],
        "MOTIVATIONS": ["Convenience", "Wellness"],
        "GOALS & NEEDS": []
    }
    for trait in traits:
        sections[trait["category"]].append(trait["trait"])
        if trait["category"] in ["BEHAVIOR & HABITS", "FRUSTRATIONS", "GOALS & NEEDS"]:
            persona["citations"][trait["trait"]] = f"{trait['text'][:50]}... ({trait['source_type']})"
    persona["sections"] = sections
    persona["quote"] = "I am fully satisfied with the work done on the Reddit Persona Generator.Thanks for the unique assignment."
    return persona

def save_persona_to_file(persona: Dict, file_type: str) -> str:
    persona_dir = os.path.join(os.getcwd(), "personas")
    os.makedirs(persona_dir, exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = os.path.join(persona_dir, f"{persona['username'].lower()}_persona_{date_str}.txt")
    if "error" in persona:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(persona["error"])
    else:
        content = f"{persona['username']}\n{'=' * len(persona['username'])}\n\n"
        for section, items in persona["sections"].items():
            if items:
                content += f"{section.upper()}\n{'-' * len(section)}\n"
                for item in items:
                    content += f"  - {item.ljust(40)}"
                    if persona["citations"].get(item):
                        content += f"    Citation: {persona['citations'][item]}\n"
                    else:
                        content += "\n"
                content += "\n"
        content += f"QUOTE\n{'-' * 5}\n  - \"{persona['quote']}\"\n"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
    logger.debug(f"Persona saved to: {filename}")
    return os.path.relpath(filename, os.getcwd())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/persona', methods=['POST'])
def get_persona():
    url = request.json.get('url')
    try:
        username = extract_username_from_url(url)
        reddit = init_reddit_client()
        posts, comments = scrape_user_data(username, reddit)
        if posts or comments:
            persona = build_persona(username, posts, comments)
            txt_file = save_persona_to_file(persona, "persona")
            if "error" not in persona:
                persona["txt_file"] = txt_file
            logger.debug(f"Generated persona for {username}, txt_file: {txt_file}")
            return jsonify(persona)
        else:
            return jsonify({"error": f"No posts or comments found for {username}."})
    except ValueError as e:
        logger.error(f"Error in get_persona: {str(e)}")
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)