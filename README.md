Reddit Persona Generator 🎉
A web-based application that generates user personas based on Reddit profile activity using Python, Flask, and spaCy for NLP analysis. 📊
Overview 🌟
This project analyzes a Reddit user's recent posts and comments to create a detailed persona profile, including personal details, behaviors, frustrations, motivations, goals, and personality traits. The output is displayed on a user-friendly interface and can be downloaded as a well-organized text file. 🚀
Features ✨

Scrapes Reddit posts and comments via the PRAW API. 📝
Uses spaCy for natural language processing to extract traits. 🤖
Provides a web UI to input Reddit URLs and view results. 🌐
Downloads organized text files with citations and quotes. 📥

Prerequisites 🛠️

Python 3.8+ 🐍
Required packages: flask, praw, spacy, en_core_web_sm 📦
Valid Reddit API credentials 🔑

Installation Guide 🏁
Step 1: Clone the Repository 📥
Clone this repository to your local machine:
git clone https://github.com/yourusername/reddit-persona-generator.git
cd reddit-persona-generator

Step 2: Set Up a Virtual Environment 🌱
Create and activate a virtual environment to manage dependencies:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Step 3: Install Required Libraries 📚
Install the necessary Python packages and download the spaCy model:
pip install -r requirements.txt
python -m spacy download en_core_web_sm

Step 4: Obtain Reddit API Credentials 🔐
To access Reddit data, you need API credentials. Follow these steps:

Create a Reddit Account 😊 - If you don’t have one, sign up at reddit.com.
Log In 🔑 - Go to reddit.com and log in.
Access Developer Settings ⚙️ - Click your profile picture (top right) > "User Settings" > "Developer Settings" (you may need to enable it under "Are you a developer?" if not visible).
Create an App 📱 - 
Go to https://www.reddit.com/prefs/apps.
Scroll down to "Developed applications" and click "Create App" or "Create another app".
Fill in:
Name: e.g., "RedditPersonaGenerator"
Description: Optional, e.g., "A tool to generate user personas"
Redirect URI: Use http://localhost:5000 (or any local URL).
App Type: Select "script".


Click "Create App".


Copy Credentials 📋 - After creation, you’ll see:
client_id: A 14-character string (found below the app name).
client_secret: A long string provided after app creation.
user_agent: Set this to something like PersonaAnalyzer/0.1 by u/your_reddit_username (replace with your Reddit username).


Update app.py ✏️ - Open app.py and replace the placeholder values:client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
user_agent = "PersonaAnalyzer/0.1 by u/your_reddit_username"



Step 5: Run the Application 🚀
Start the Flask server:
python app.py

Step 6: Access the UI 🌐
Open your web browser and go to http://localhost:5000. 🎈
Usage 🚦

Enter a Reddit profile URL (e.g., https://www.reddit.com/user/kojied) in the input field. 📎
Click "Generate Persona" to process the data. 🔍
View the persona details on the UI, including sections like "BEHAVIOR & HABITS" and "QUOTE". 👀
Download the text file using the "Download as Text" button. 💾

Project Structure 📂
reddit-persona-generator/
├── app.py                # Main Flask application
├── templates/            # HTML templates
│   └── index.html        # Frontend UI
├── personas/             # Directory for output files (gitignored)
├── static/               # Optional for CSS/JS (not used here)
├── .gitignore            # Ignore files like venv and personas
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies

Output Example 🎨
UI Display
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

Downloaded Text File (kojied_persona_2025-07-15.txt)
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

Contributing 🤝

Fork the repository. 🍴
Create a feature branch (git checkout -b feature-branch). 🌿
Commit changes (git commit -m "Add new feature"). 💾
Push to the branch (git push origin feature-branch). 🚀
Open a pull request. 📩

License 📜
MIT License

Copyright (c) [2025] [BHUPATHI SRAVAN KUMAR]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

Contact 📧
For questions, open an issue or reach out via your GitHub profile.
Notes 📝

Current date and time: 11:41 AM IST, Tuesday, July 15, 2025. ⏰
Ensure the personas directory is writable by the server process. 🔧
