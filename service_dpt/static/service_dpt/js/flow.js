document.addEventListener('DOMContentLoaded', () => {
    // Initialize SortableJS
    const lists = document.querySelectorAll('.kanban-list');
    lists.forEach(list => {
        Sortable.create(list, {
            group: 'kanban',
            animation: 150,
        });
    });

    // Modal Trigger
    document.querySelectorAll('.kanban-card').forEach(card => {
        card.addEventListener('click', () => {
            const vehicleNo = card.getAttribute('data-vehicle');
            const customerName = card.getAttribute('data-customer');
            const department = card.getAttribute('data-department');

            document.getElementById('modalVehicleNo').innerText = vehicleNo;
            document.getElementById('modalCustomerName').innerText = customerName;
            document.getElementById('modalDepartment').innerText = department;

            const modal = new bootstrap.Modal(document.getElementById('vehicleModal'));
            modal.show();
        });
    });
});
