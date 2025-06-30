#!/bin/bash
# Verify static/chart.js exists
if [ ! -f static/chart.js ]; then
    echo "Error: static/chart.js not found. Please download from https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.min.js and save as static/chart.js"
    exit 1
fi

# Ensure data directory exists
mkdir -p data

cd engine || { echo "Error: engine directory not found"; exit 1; }
[ -f process.py ] && python process.py || { echo "Error: process.py not found"; exit 1; }
[ -f time.py ] && python time.py || { echo "Error: time.py not found"; exit 1; }
[ -f static.py ] && python static.py || { echo "Error: static.py not found"; exit 1; }
cd .. || { echo "Error: cannot return to parent directory"; exit 1; }
[ -f flask-app.py ] && python flask-app.py || { echo "Error: flask-app.py not found"; exit 1; }