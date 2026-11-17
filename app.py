import os
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request

from ai_service import generate_ai_response
from prompt_builder import build_prompt
from text_utils import clean_text

load_dotenv()

app = Flask(__name__)
MAX_NOTES_CHARS = 12000
ALLOWED_TASKS = {"summary", "explain", "questions"}


@app.get("/")
def home():
    return render_template("index.html")


@app.post("/analyze")
def analyze():
    data = request.get_json(silent=True) or {}
    notes = clean_text(data.get("notes", ""))
    task = str(data.get("task", "summary")).strip().lower()

    if not notes:
        return jsonify({"error": "Please paste your study notes first."}), 400

    if len(notes) > MAX_NOTES_CHARS:
        return jsonify({
            "error": f"Your notes are too long. Please keep them under {MAX_NOTES_CHARS} characters."
        }), 400

    if task not in ALLOWED_TASKS:
        return jsonify({"error": "Please select a valid task."}), 400

    try:
        prompt = build_prompt(notes, task)
        result = generate_ai_response(prompt)
        return jsonify({"result": result})
    except RuntimeError as error:
        app.logger.error("Configuration problem: %s", error)
        return jsonify({"error": str(error)}), 500
    except Exception:
        app.logger.exception("The Groq request failed.")
        return jsonify({
            "error": (
                "The AI request failed. Check your internet connection, Groq API key, "
                "model name, and Groq account limits, then try again."
            )
        }), 502


if __name__ == "__main__":
    debug_mode = os.getenv("FLASK_DEBUG", "0").strip() == "1"
    app.run(host="127.0.0.1", port=5000, debug=debug_mode)
