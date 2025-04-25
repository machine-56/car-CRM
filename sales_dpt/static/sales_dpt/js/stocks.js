document.addEventListener('DOMContentLoaded', function() {
    const filterCategory = document.getElementById('filterCategory');
    const rows = document.querySelectorAll('#stockTable tbody tr');

    filterCategory.addEventListener('change', function() {
        const selected = this.value;

        rows.forEach(row => {
            const category = row.getAttribute('data-category');
            if (selected === 'all' || category === selected) {
                row.style.display = '';
            } else {
                row.style.display = 'none';
            }
        });
    });
});
