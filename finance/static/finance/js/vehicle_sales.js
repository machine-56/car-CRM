document.addEventListener("DOMContentLoaded", function () {
    const table = document.getElementById("vehicleSalesTable");
    const chartCanvas = document.getElementById("vehicleSalesChart");

    // Provide custom Excel header
    window.customExcelHeader = [
        ["Vehicle Sales Report"],
        ["Generated on:", new Date().toLocaleDateString()],
        [] // blank row for spacing
    ];

    const labels = [];
    const unitsSold = [];
    const revenues = [];

    for (let i = 1; i < table.rows.length; i++) {
        const row = table.rows[i];
        labels.push(row.cells[0].innerText);
        unitsSold.push(parseInt(row.cells[1].innerText));
        revenues.push(parseInt(row.cells[2].innerText.replace(/[₹,]/g, '')));
    }

    new Chart(chartCanvas, {
        type: "bar",
        data: {
            labels: labels,
            datasets: [
                {
                    label: "Vehicles Sold",
                    data: unitsSold,
                    backgroundColor: "rgba(54, 162, 235, 0.6)",
                    borderColor: "rgba(54, 162, 235, 1)",
                    borderWidth: 1,
                },
                {
                    label: "Revenue (₹)",
                    data: revenues,
                    backgroundColor: "rgba(255, 206, 86, 0.6)",
                    borderColor: "rgba(255, 206, 86, 1)",
                    borderWidth: 1,
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
