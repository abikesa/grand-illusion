from flask import Flask, render_template, send_from_directory
import yaml
import os

app = Flask(__name__)

@app.route("/")
def dashboard():
    with open("render.yaml", "r") as f:
        data = yaml.safe_load(f)
    quotes = ['“The real is no longer what it used to be.” – Baudrillard', '“Everyone has their reasons.” – Jean Renoir', '“Free will is a biological illusion.” – Robert Sapolsky', '“Il n’y a pas de hors-texte.” (There is no outside-text.) – Jacques Derrida', '“Power is everywhere... because it comes from everywhere.” – Michel Foucault', '“The illusion of freedom is part of the machinery of control.” – Zadie Smith']
    return render_template("dashboard.html", stack=data["stack"], quotes=quotes)

@app.route("/static/data/<path:filename>")
def data_file(filename):
    return send_from_directory("data", filename)

if __name__ == "__main__":
    app.run(debug=True)