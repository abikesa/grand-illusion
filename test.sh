#!/bin/bash

echo "🧪 Testing Grande Illusion Setup"
echo "================================"

# Check files exist
echo "📁 Checking required files..."
FILES=("flask-app.py" "static/chart.js" "templates/dashboard.html")
for file in "${FILES[@]}"; do
    if [ -f "$file" ]; then
        echo "✅ $file exists"
    else
        echo "❌ $file missing"
    fi
done

# Check Chart.js file
if [ -f "static/chart.js" ]; then
    SIZE=$(stat -f%z static/chart.js 2>/dev/null || stat -c%s static/chart.js 2>/dev/null)
    echo "📊 Chart.js size: $SIZE bytes"
    
    if grep -q "Chart" static/chart.js; then
        echo "✅ Chart.js contains Chart code"
    else
        echo "❌ Chart.js doesn't contain Chart code"
    fi
fi

echo ""
echo "🚀 Starting Flask app test..."
echo "Press Ctrl+C to stop the test"
echo ""

# Start Flask app in background for testing
python flask-app.py &
FLASK_PID=$!

# Wait for Flask to start
sleep 3

echo "🔍 Testing endpoints..."

# Test main page
if curl -s http://127.0.0.1:5000/ > /dev/null; then
    echo "✅ Main page accessible"
else
    echo "❌ Main page not accessible"
fi

# Test static file
if curl -s http://127.0.0.1:5000/static/chart.js > /dev/null; then
    echo "✅ Static files accessible"
else
    echo "❌ Static files not accessible"
fi

# Test debug endpoint
echo "📊 Debug info:"
curl -s http://127.0.0.1:5000/debug/static

# Clean up
kill $FLASK_PID 2>/dev/null

echo ""
echo "✅ Test complete! If all checks passed, your setup should work."
echo "🚀 Run: python flask-app.py"
echo "🌐 Then visit: http://127.0.0.1:5000"
