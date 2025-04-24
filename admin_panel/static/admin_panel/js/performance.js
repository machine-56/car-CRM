const salesCtx = document.getElementById('salesChart').getContext('2d');
new Chart(salesCtx, {
    type: 'bar',
    data: {
        labels: ['Sedan', 'SUV', 'Sports', 'Luxury'],
        datasets: [{
            label: 'Cars Sold',
            data: [25, 40, 15, 5],
            backgroundColor: ['#ff0000', '#d32f2f', '#a9a9a9', '#c0c0c0'],
        }]
    },
    options: {
        responsive: true,
        plugins: { legend: { display: false } }
    }
});

const revenueCtx = document.getElementById('revenueChart').getContext('2d');
new Chart(revenueCtx, {
    type: 'line',
    data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
        datasets: [{
            label: 'Revenue (in lakhs)',
            data: [12, 19, 10, 15, 20],
            borderColor: '#ff0000',
            fill: false,
            tension: 0.4
        }]
    },
    options: {
        responsive: true,
        plugins: { legend: { display: true } }
    }
});

const serviceCtx = document.getElementById('serviceChart').getContext('2d');
new Chart(serviceCtx, {
    type: 'pie',
    data: {
        labels: ['Paint', 'Body Repairs', 'Electrical', 'Insurance'],
        datasets: [{
            data: [30, 25, 20, 25],
            backgroundColor: ['#ff0000', '#d32f2f', '#a9a9a9', '#c0c0c0'],
        }]
    },
    options: {
        responsive: true
    }
});
