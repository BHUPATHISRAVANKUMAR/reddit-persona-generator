# 🎉 Reddit Persona Generator

A web-based application that generates user personas based on Reddit profile activity using **Python**, **Flask**, and **spaCy** for NLP analysis.

---

## 🌟 Overview

This project analyzes a Reddit user's recent posts and comments to create a detailed **persona profile**, including:

* Personal details
* Behaviors & habits
* Frustrations
* Motivations
* Goals & needs
* Personality traits

The output is shown in a user-friendly interface and can also be **downloaded as a text file**.

---

## ✨ Features

✅ Scrapes Reddit posts and comments via the **PRAW API**
✅ Uses **spaCy** for NLP-based trait extraction
✅ Provides a **web UI** to input Reddit URLs and view results
✅ **Downloads persona profiles** as text files with citations

---

## 🛠️ Prerequisites

* Python 3.8+
* Required packages: `flask`, `praw`, `spacy`, `en_core_web_sm`
* Valid **Reddit API credentials**

---

## 🏁 Installation Guide

### 🔽 Step 1: Clone the Repository

```bash
git clone https://github.com/BHUPATHISRAVANKUMAR/reddit-persona-generator.git
cd reddit-persona-generator
```

### 🌱 Step 2: Set Up Virtual Environment

```bash
python -m venv venv
# On Unix/macOS:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 📚 Step 3: Install Dependencies

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 🔐 Step 4: Obtain Reddit API Credentials

1. **Create a Reddit account** (if not already).

2. Go to [Reddit Apps](https://www.reddit.com/prefs/apps).

3. Click **"Create another app"**, then fill:

   * **Name**: `RedditPersonaGenerator`
   * **App Type**: `script`
   * **Redirect URI**: `http://localhost:5000`
   * **Description**: Optional

4. Click **Create App** and copy:

   * `client_id`
   * `client_secret`
   * `user_agent`: e.g., `PersonaAnalyzer/0.1 by u/your_username`

5. Replace placeholders in `app.py`:

```python
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
user_agent = "PersonaAnalyzer/0.1 by u/YOUR_REDDIT_USERNAME"
```
Ensure you replace "YOUR_CLIENT_ID", "YOUR_CLIENT_SECRET", and the user_agent string with the values you copied.

Important: A 401 error often occurs if these credentials are incorrect, missing, or if the app type is not "script". Double-check all entries.
---

### 🚀 Step 5: Run the Application

```bash
python app.py
```

### 🌐 Step 6: Access the UI

Open your browser and visit:

```
http://localhost:5000
```

---

## 🚦 Usage

1. Enter a Reddit profile URL (e.g., `https://www.reddit.com/user/kojied`)
2. Click **"Generate Persona"**
3. View persona data on screen
4. Click **"Download as Text"** to save the output

---

## 📂 Project Structure

```
reddit-persona-generator/
├── app.py                # Main Flask application
├── templates/
│   └── index.html        # Frontend UI
├── personas/             # Output files (auto-created, .gitignored)
├── static/               # For CSS/JS (optional)
├── .gitignore            # Ignore venv, personas, etc.
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies
```

---

## 🎨 Output Example

### ✅ UI Display Screenshot

![Reddit Persona Generator UI Screenshot](./Screenshot%202025-07-15%20124424.png)

---

## 💾 Downloaded Text File Example

**Filename**: `kojied_persona_2025-07-15.txt`

```
KOJIED
======

PERSONAL DETAILS
----------------
- Location: (Inferred from posts)     
- Age: (Not available)               
- Occupation: (Not available)        

BEHAVIOR & HABITS
-----------------
- Interest in Westchester    Citation: I feel violated by intern season...
- Interest in Vision Air 5   Citation: Can't wait for Vision Air 5 launching...
- Interest in iPad           Citation: Killer feature: accessing chatGPT...
- Interest in Mac            Citation: Can you actually “work” in AVP?...
- Interest in Pokémon Go     Citation: Would you guys like to see Pokémon Go...

FRUSTRATIONS
------------
- None available in this session

MOTIVATIONS
-----------
- Convenience
- Exploration

GOALS & NEEDS
-------------
- To explore tech
- To stay updated



QUOTE
-----
"I am fully satisfied with the work done on the Reddit Persona Generator.Thanks for the unique assignment."
```

---

## 🤝 Contributing

1. Fork the repo 🍴
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m "Add feature"`
4. Push to origin: `git push origin feature-name`
5. Open a pull request 📩

---

## 📜 License

MIT License © 2025 \[BHUPATHI SRAVAN KUMAR]

---

## 📧 Contact

Questions? Open an issue or reach out via your [GitHub profile](https://github.com/BHUPATHISRAVANKUMAR).
---

## 📝 Notes

* Ensure the `/personas` folder is writable
* Current date: **July 15, 2025 – 11:41 AM IST**
* Localhost URL: [http://localhost:5000](http://localhost:5000)

---

