from flask import Flask, render_template, send_from_directory
import yaml
import random
import traceback
import os

app = Flask(__name__)

@app.route("/")
def dashboard():
    try:
        with open("stack.yaml", "r") as f:
            data = yaml.safe_load(f)
        stack_data = data.get("stack", []) if data else []
    except Exception as e:
        print(f"Error loading stack.yaml: {e}")
        print(traceback.format_exc())
        stack_data = []

    quotes = [
        "The simulacrum is never that which conceals the truth—it is the truth which conceals that there is none. – Baudrillard",
        "You may imagine the universe, but you cannot grasp it. – Jean Renoir",
        "Free will is biology's illusion. – Robert Sapolsky",
        "Il n'y a pas de hors-texte. – Jacques Derrida",
        "Power is everywhere… – Michel Foucault",
        "Time is how you spend your love. – Zadie Smith"
    ]
    random.shuffle(quotes)

    try:
        return render_template("dashboard.html", stack=stack_data, quotes=quotes)
    except Exception as e:
        print(f"Error rendering dashboard.html: {e}")
        print(traceback.format_exc())
        return "Server error: Failed to render dashboard", 500

@app.route("/other")
def other():
    try:
        return render_template("other.html")
    except Exception as e:
        print(f"Error rendering other.html: {e}")
        print(traceback.format_exc())
        return "Server error: Failed to render other page", 500

@app.route("/data/<path:filename>")
def serve_data(filename):
    try:
        return send_from_directory("data", filename)
    except Exception as e:
        print(f"Error serving file {filename}: {e}")
        return "File not found", 404

# Explicit static file serving - THIS IS THE KEY FIX
@app.route("/static/<path:filename>")
def serve_static(filename):
    try:
        static_path = os.path.join(app.root_path, "static")
        print(f"Serving static file: {filename} from {static_path}")
        return send_from_directory(static_path, filename)
    except Exception as e:
        print(f"Error serving static file {filename}: {e}")
        print(traceback.format_exc())
        return "Static file not found", 404

# Debug route to check static files
@app.route("/debug/static")
def debug_static():
    try:
        static_path = os.path.join(app.root_path, "static")
        files = os.listdir(static_path) if os.path.exists(static_path) else []
        
        info = {
            "static_path": static_path,
            "static_exists": os.path.exists(static_path),
            "files": files,
            "chart_js_exists": os.path.exists(os.path.join(static_path, "chart.js")),
            "chart_js_size": os.path.getsize(os.path.join(static_path, "chart.js")) if os.path.exists(os.path.join(static_path, "chart.js")) else 0
        }
        
        return f"<pre>{yaml.dump(info, default_flow_style=False)}</pre>"
    except Exception as e:
        return f"Debug error: {e}"

if __name__ == "__main__":
    app.run(debug=True)