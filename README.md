# 🎭 Grande Illusion Stack

This is a poetic-engineering Flask + CSV + YAML stack inspired by Jean Renoir, Baudrillard, and the metaphysics of user interface illusion.

## 📂 Structure

```
.
├── flask-app.py
├── render.yaml
├── templates/
│   ├── dashboard.html
│   └── other.html
├── engine/
│   ├── process.py
│   ├── time.py
│   └── static.py
├── data/
│   ├── generated_hour.csv
│   ├── ...
│   └── master.csv
```

## 🧠 Layers

| Emoji | Filetype | Concept   | Description                                      |
|-------|----------|-----------|--------------------------------------------------|
| 🌊    | `.csv`   | Renoir    | Raw impressions, generated every time scale     |
| ❤️    | `.py`    | Règle     | Logic and deterministic processing              |
| 🔁    | `.jinja` | Du Jeu    | Templates that appear to offer freedom          |
| 🎭    | `.html`  | Grande    | The UI mask where illusion becomes visible      |
| 📡    | `.yaml`  | Illusion  | Schema/config architecture hidden in plain sight|

## 🚀 Running

1. Install dependencies (Flask, PyYAML)
```bash
pip install flask pyyaml
```

2. Start the app
```bash
python flask-app.py
```

3. Generate data and update master CSV:
```bash
python engine/process.py
python engine/time.py
python engine/static.py
```

## ⏰ Automation (crontab)

See `crontab.txt` for scheduling hourly/daily/weekly jobs.

---
> “The real is no longer what it used to be.” – Jean Baudrillard