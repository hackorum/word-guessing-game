from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

templates = [
    {"inputs": 5, "category": "Sports", "word": "Chess"},
    {"inputs": 6, "category": "European Country Name", "word": "France"},
]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get-words")
def get_words():
    return jsonify({"status": "success", "word": random.choice(templates)})


if __name__ == "__main__":
    app.run(debug=True, port=8080)
