// Client-side JS to fetch CSV and update Chart.js every minute
let chart;

function fetchAndRenderChart() {
    fetch('/static/data/formatted.csv')
        .then(response => response.text())
        .then(data => {
            const lines = data.trim().split('\n').slice(1);
            const labels = lines.map(l => l.split(',')[0]);
            const values = lines.map(l => +l.split(',')[2]);

            if (!chart) {
                const ctx = document.getElementById('illusionChart').getContext('2d');
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
                            y: { beginAtZero: true }
                        }
                    }
                });
            } else {
                chart.data.labels = labels;
                chart.data.datasets[0].data = values;
                chart.update();
            }
        });
}

// Initial load and interval polling
window.onload = fetchAndRenderChart;
setInterval(fetchAndRenderChart, 60000);