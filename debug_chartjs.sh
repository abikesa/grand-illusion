#!/bin/bash

echo "🔍 Debugging Chart.js setup..."

# Check if static directory exists
if [ ! -d "static" ]; then
    echo "❌ static directory doesn't exist, creating it..."
    mkdir -p static
fi

# Check current Chart.js files
echo "📁 Current static directory contents:"
ls -la static/

# Check if chart.js exists and its size
if [ -f "static/chart.js" ]; then
    echo "📊 chart.js file info:"
    ls -lh static/chart.js
    echo "📝 First few lines of chart.js:"
    head -n 5 static/chart.js
    echo "..."
    echo "📝 Last few lines of chart.js:"
    tail -n 5 static/chart.js
else
    echo "❌ chart.js not found"
fi

# Download fresh Chart.js
echo "📥 Downloading fresh Chart.js..."
curl -L -o static/chart.js https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.min.js

# Verify download
if [ -f "static/chart.js" ]; then
    FILE_SIZE=$(stat -f%z static/chart.js 2>/dev/null || stat -c%s static/chart.js 2>/dev/null)
    echo "✅ Downloaded chart.js - Size: $FILE_SIZE bytes"
    
    # Check if it's actually Chart.js content
    if grep -q "Chart" static/chart.js; then
        echo "✅ File contains Chart.js content"
    else
        echo "❌ File doesn't appear to contain Chart.js content"
        echo "📝 First 200 characters:"
        head -c 200 static/chart.js
    fi
else
    echo "❌ Failed to download chart.js"
fi

# Also create chart.min.js as a symlink/copy
cp static/chart.js static/chart.min.js 2>/dev/null || echo "Could not create chart.min.js copy"

echo "🔍 Final static directory:"
ls -la static/
