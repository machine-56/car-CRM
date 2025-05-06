document.addEventListener("DOMContentLoaded", function () {
    const table = document.getElementById("partsSalesTable");
    const chartCanvas = document.getElementById("partsSalesChart");

    const labels = [];
    const unitsSold = [];
    const revenues = [];

    for (let i = 1; i < table.rows.length; i++) {
        const row = table.rows[i];
        labels.push(row.cells[0].innerText); // Date
        unitsSold.push(parseInt(row.cells[1].innerText));
        revenues.push(parseInt(row.cells[2].innerText.replace(/[₹,]/g, '')));
    }

    new Chart(chartCanvas, {
        type: "line",
        data: {
            labels: labels,
            datasets: [
                {
                    label: "Units Sold",
                    data: unitsSold,
                    borderColor: "rgba(75, 192, 192, 1)",
                    backgroundColor: "rgba(75, 192, 192, 0.2)",
                    tension: 0.3,
                },
                {
                    label: "Revenue (₹)",
                    data: revenues,
                    borderColor: "rgba(255, 99, 132, 1)",
                    backgroundColor: "rgba(255, 99, 132, 0.2)",
                    tension: 0.3,
                },
            ],
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true,
                },
            },
        },
    });
});
