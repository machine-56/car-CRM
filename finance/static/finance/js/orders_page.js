document.addEventListener("DOMContentLoaded", function () {
    const ctx = document.getElementById('ordersChart').getContext('2d');

    const categories = {};
    document.querySelectorAll('#ordersTable tbody tr').forEach(row => {
        const category = row.cells[2].innerText;
        const expense = parseFloat(row.cells[4].innerText);
        categories[category] = (categories[category] || 0) + expense;
    });

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: Object.keys(categories),
            datasets: [{
                label: 'Expense',
                data: Object.values(categories),
                backgroundColor: '#d32f2f'
            }]
        },
        options: {
            responsive: true,
            plugins: { legend: { display: false } },
            scales: { y: { beginAtZero: true } },
            elements: {
                bar: {
                    maxBarThickness: 100,
                    minBarLength: 5
                }
            }
        }
    });
});
