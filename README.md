# AI Study Material Analyzer

A beginner-friendly Flask web app that uses the Groq API to summarize notes, explain concepts in simple language, or generate practice questions.

## Requirements
- Python 3.10 or newer
- A Groq account and API key
- Internet connection for AI requests

## Setup on Windows (PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install --upgrade pip
py -m pip install -r requirements.txt
Copy-Item .env.example .env
```

Open `.env` and replace the placeholder with your own Groq API key. Never share the key or upload `.env` to GitHub. If the configured model is unavailable in your Groq Console, set `GROQ_MODEL` to a currently available chat model.

Start the app:

```powershell
py app.py
```

Open http://127.0.0.1:5000 in your browser. Keep the terminal open while using the app. Press `Ctrl+C` to stop Flask.

## Features
- Summary of supplied notes
- Beginner-friendly explanation
- Practice questions with an answer key
- Input validation (empty notes, unsupported task, and 12,000-character limit)
- Loading state, error messages, and copy-result button

## Project structure

```text
AI_Study_Material_Analyzer/
├── app.py
├── ai_service.py
├── prompt_builder.py
├── text_utils.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── script.js
```

## GitHub safety
The `.gitignore` excludes `.env` and virtual-environment files. Before committing, run `git status` and confirm that `.env` is not listed. If a key is ever exposed, revoke it in Groq Console immediately and create a replacement.

Uploading to GitHub does not deploy the application.
