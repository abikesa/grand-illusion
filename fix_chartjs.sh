#!/bin/bash

# Download Chart.js if it doesn't exist
if [ ! -f static/chart.js ]; then
    echo "📊 Downloading Chart.js..."
    curl -o static/chart.js https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.min.js
    echo "✅ Chart.js downloaded successfully"
fi

# Also create chart.min.js as a copy since your HTML references it
if [ ! -f static/chart.min.js ]; then
    echo "📊 Creating chart.min.js reference..."
    cp static/chart.js static/chart.min.js
    echo "✅ chart.min.js created"
fi

echo "🔍 Verifying Chart.js files:"
ls -la static/chart*
