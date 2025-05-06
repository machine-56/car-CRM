document.addEventListener("DOMContentLoaded", function () {
    const filter = document.getElementById('filterCategory');
    const rows = document.querySelectorAll('#stockTable tbody tr');
    const orderButtons = document.querySelectorAll('.btn-order');
    const modal = new bootstrap.Modal(document.getElementById('orderModal'));
    const orderPartName = document.getElementById('orderPartName');
    const orderQuantity = document.getElementById('orderQuantity');
    const confirmOrder = document.getElementById('confirmOrder');
    const messageContainer = document.getElementById('messageContainer');
    let selectedPart = '';

    // Highlight low stock
    document.querySelectorAll('.stock-cell').forEach(cell => {
        const qty = parseInt(cell.dataset.qty);
        if (qty < 5) {
            cell.classList.add('low-stock');
        }
    });

    // Filter rows
    filter.addEventListener('change', () => {
        const category = filter.value;
        rows.forEach(row => {
            if (category === 'all' || row.dataset.category === category) {
                row.style.display = '';
            } else {
                row.style.display = 'none';
            }
        });
    });

    // Handle order button click
    orderButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            selectedPart = btn.dataset.part;
            orderPartName.textContent = `Ordering: ${selectedPart}`;
            orderQuantity.value = '';
            modal.show();
        });
    });

    // Confirm order and show success message
    confirmOrder.addEventListener('click', () => {
        const qty = orderQuantity.value;
        if (qty && qty > 0) {
            modal.hide();
            messageContainer.innerHTML = `<div class="alert alert-success alert-dismissible fade show" role="alert">
                Order placed for <strong>${qty}</strong> units of <strong>${selectedPart}</strong>!
                <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
            </div>`;
        }
    });

    // Initialize Chart.js graph
    const ctx = document.getElementById('sparePartsChart').getContext('2d');
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Braking System', 'Engine', 'Electrical'],
            datasets: [
                { label: 'Earnings', data: [5000, 8000, 3000], backgroundColor: '#000000' },
                { label: 'Expenses', data: [2000, 5000, 1500], backgroundColor: '#d32f2f' }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { position: 'top' } },
            scales: { y: { beginAtZero: true } }
        }
    });
});
