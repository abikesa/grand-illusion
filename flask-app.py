from flask import Flask, render_template
import yaml
import random

app = Flask(__name__)

@app.route("/")
def dashboard():
    # Load the metaphysical YAML stack
    try:
        with open("stack.yaml", "r") as f:
            data = yaml.safe_load(f)
        stack_data = data.get("stack", [])
    except Exception as e:
        stack_data = []
        print("Error loading stack.yaml:", e)

    # Quotes engine
    quotes = [
        "The simulacrum is never that which conceals the truth—it is the truth which conceals that there is none. – Baudrillard",
        "You may imagine the universe, but you cannot grasp it. – Jean Renoir",
        "Free will is biology’s illusion. – Robert Sapolsky",
        "Il n'y a pas de hors-texte. – Jacques Derrida",
        "Power is everywhere… – Michel Foucault",
        "Time is how you spend your love. – Zadie Smith"
    ]
    random.shuffle(quotes)

    return render_template("dashboard.html", stack=stack_data, quotes=quotes)

@app.route("/other")
def other():
    return render_template("other.html")

if __name__ == "__main__":
    app.run(debug=True)
