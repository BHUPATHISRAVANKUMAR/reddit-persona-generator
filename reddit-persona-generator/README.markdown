# Reddit Persona Generator

A web-based application that generates user personas based on Reddit profile activity using Python, Flask, and spaCy for NLP analysis.

## Overview

This project analyzes a Reddit user's recent posts and comments to create a persona profile, including personal details, behaviors, frustrations, motivations, goals, and personality traits. The output is displayed on a user-friendly interface and can be downloaded as a text file.

## Features
- Scrapes Reddit posts and comments via the PRAW API.
- Uses spaCy for natural language processing to extract traits.
- Provides a web UI to input Reddit URLs and view results.
- Downloads organized text files with citations and quotes.

## Prerequisites
- Python 3.8+
- Required packages: `flask`, `praw`, `spacy`, `en_core_web_sm`
- Valid Reddit API credentials

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/reddit-persona-generator.git
   cd reddit-persona-generator
   ```

2. Set up a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
   ```

3. Configure Reddit API credentials:
   - Create a Reddit app at https://www.reddit.com/prefs/apps.
   - Update `app.py` with your `client_id`, `client_secret`, and `user_agent`.

4. Run the application:
   ```bash
   python app.py
   ```

5. Access the UI at `http://localhost:5000`.

## Usage

1. Enter a Reddit profile URL (e.g., `https://www.reddit.com/user/kojied`) in the input field.
2. Click "Generate Persona" to process the data.
3. View the persona details on the UI, including sections like "BEHAVIOR & HABITS" and "QUOTE".
4. Download the text file using the "Download as Text" button.

## Output Example

### UI Display
```
KOJIED
PERSONAL DETAILS
  - Location: (Inferred from posts)
  - Age: (Not available)
  - Occupation: (Not available)

BEHAVIOR & HABITS
  - Interest in Technology    Citation: Love using tech gadgets... (post)
  - Positive attitude         Citation: Really enjoyed the update... (comment)

FRUSTRATIONS
  - Frustrated sentiment      Citation: This bug is annoying... (post)

MOTIVATIONS
  - Convenience
  - Wellness

GOALS & NEEDS
  - Desire to improve         Citation: Need to learn more... (comment)

PERSONALITY
  - Practical
  - Adaptable
  - Spontaneous
  - Active

QUOTE: "I want to spend less time ordering and more time enjoying my meal."
```

### Downloaded Text File (`kojied_persona_2025-07-15.txt`)
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
  - Interest in Technology    Citation: Love using tech gadgets... (post)
  - Positive attitude         Citation: Really enjoyed the update... (comment)

FRUSTRATIONS
------------
  - Frustrated sentiment      Citation: This bug is annoying... (post)

MOTIVATIONS
-----------
  - Convenience               
  - Wellness                  

GOALS & NEEDS
-------------
  - Desire to improve         Citation: Need to learn more... (comment)

PERSONALITY
-----------
  - Practical                 
  - Adaptable                 
  - Spontaneous               
  - Active                    

QUOTE
-----
  - "I want to spend less time ordering and more time enjoying my meal."
```

## Contributing

- Fork the repository.
- Create a feature branch (`git checkout -b feature-branch`).
- Commit changes (`git commit -m "Add new feature"`).
- Push to the branch (`git push origin feature-branch`).
- Open a pull request.

## License

MIT License - See the [LICENSE](LICENSE) file for details (add a `LICENSE` file with MIT text).

## Contact

For questions, open an issue or reach out via [your GitHub profile](https://github.com/yourusername).