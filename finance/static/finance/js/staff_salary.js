document.addEventListener("DOMContentLoaded", function () {
    const departmentSelect = document.getElementById('department');
    const staffSelect = document.getElementById('staff_name');

    departmentSelect.addEventListener('change', function () {
        staffSelect.innerHTML = '<option value="">Select Staff</option>';
        let selectedStaff = [];
        const deptValue = this.value.trim().toLowerCase();

        if (deptValue === 'sales') {
            selectedStaff = window.salesStaff;
        } else if (deptValue === 'service') {
            selectedStaff = window.serviceStaff;
        }

        selectedStaff.forEach(function (name) {
            const option = document.createElement('option');
            option.value = name;
            option.textContent = name;
            staffSelect.appendChild(option);
        });
    });
});
