// Client-side JS to fetch CSV and update Chart.js every minute
let chart;

function fetchAndRenderChart() {
    if (typeof Chart === 'undefined') {
        console.error('Chart.js not loaded');
        const canvas = document.getElementById('illusionChart');
        if (canvas) {
            canvas.insertAdjacentHTML('afterend', '<p style="color: red;">Failed to load graph: Chart.js not available</p>');
        }
        return;
    }

    fetch('/data/formatted.csv')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok: ' + response.status);
            }
            return response.text();
        })
        .then(data => {
            const lines = data.trim().split('\n');
            if (lines.length <= 1) {
                throw new Error('CSV is empty or has no data rows');
            }
            const labels = lines.slice(1).map(l => {
                const cols = l.split(',');
                return cols[0] ? cols[0].slice(0, 10) : 'Unknown';
            });
            const values = lines.slice(1).map(l => {
                const cols = l.split(',');
                return cols[2] ? +cols[2] : 0;
            });
            if (labels.length === 0 || values.some(v => isNaN(v))) {
                throw new Error('Invalid CSV format: missing or invalid labels/values');
            }
            const ctx = document.getElementById('illusionChart')?.getContext('2d');
            if (!ctx) {
                console.error('Canvas element not found');
                return;
            }
            if (!chart) {
                chart = new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: labels,
                        datasets: [{
                            label: 'Perceived Interaction Value',
                            data: values,
                            borderColor: '#ff4081',
                            borderWidth: 2,
                            fill: false
                        }]
                    },
                    options: {
                        responsive: true,
                        scales: {
                            y: { beginAtZero: true },
                            x: {
                                title: {
                                    display: true,
                                    text: 'Date'
                                }
                            }
                        }
                    }
                });
            } else {
                chart.data.labels = labels;
                chart.data.datasets[0].data = values;
                chart.update();
            }
        })
        .catch(error => {
            console.error('Error fetching or rendering chart:', error);
            const canvas = document.getElementById('illusionChart');
            if (canvas) {
                canvas.insertAdjacentHTML('afterend', '<p style="color: red;">Failed to load graph: ' + error.message + '</p>');
            }
        });
}

// Initial load and interval polling
window.onload = fetchAndRenderChart;
setInterval(fetchAndRenderChart, 60000);