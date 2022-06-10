from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", name="iftach bar", hobbies="drums, bass, music, cooking", skills="python, html, css, js", strengths="patient, smart, beautiful", weaknesses="none")

if __name__ == "__main__":
    app.run(debug=True)