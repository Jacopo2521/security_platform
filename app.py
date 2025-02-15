from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Funzione per caricare il JSON
def load_summary():
    with open("data/summary.json", "r", encoding="utf-8") as file:
        return json.load(file)

@app.route("/")
def index():
    return render_template("index.html")

# API per ottenere i dati dal JSON
@app.route("/api/summary")
def api_file():
    data = load_summary()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
