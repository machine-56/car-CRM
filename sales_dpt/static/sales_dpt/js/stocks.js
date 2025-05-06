document.addEventListener('DOMContentLoaded', function() {
    const filterCategory = document.getElementById('filterCategory');
    const rows = document.querySelectorAll('#stockTable tbody tr');
    const orderButtons = document.querySelectorAll('.btn-order');
    const orderPartName = document.getElementById('orderPartName');
    const modalPartName = document.getElementById('modalPartName');

    filterCategory.addEventListener('change', function() {
        const selected = this.value;
        rows.forEach(row => {
            const category = row.getAttribute('data-category');
            row.style.display = (selected === 'all' || category === selected) ? '' : 'none';
        });
    });

    orderButtons.forEach(button => {
        button.addEventListener('click', () => {
            const part = button.getAttribute('data-part');
            orderPartName.textContent = `Ordering: ${part}`;
            modalPartName.value = part;
        });
    });
});
