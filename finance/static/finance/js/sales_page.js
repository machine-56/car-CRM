document.addEventListener('DOMContentLoaded', function () {
    const labels = [];
    const carData = [];
    const spareData = [];

    document.querySelectorAll('#salesTable tbody tr').forEach(row => {
        labels.push(row.cells[0].innerText);
        carData.push(+row.cells[1].innerText);
        spareData.push(+row.cells[2].innerText);
    });

    const ctx = document.getElementById('salesChart').getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [
                { label: 'Car Sales', data: carData, borderColor: 'blue', fill: false },
                { label: 'Spare Parts Sales', data: spareData, borderColor: 'green', fill: false }
            ]
        },
        options: {
            responsive: true,
            plugins: { legend: { position: 'top' } }
        }
    });
});
