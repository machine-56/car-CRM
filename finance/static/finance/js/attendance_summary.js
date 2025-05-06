document.addEventListener("DOMContentLoaded", function () {
    const name = document.querySelector('#staffName') ? document.querySelector('#staffName').innerText : "N/A";
    const department = document.querySelector('#staffDept') ? document.querySelector('#staffDept').innerText : "N/A";
    const table = document.getElementById('attendanceTable');

    let totalDays = 0;
    let presentDays = 0;
    let absentDays = 0;

    table.querySelectorAll('tbody tr').forEach(row => {
        totalDays++;
        const status = row.children[1].innerText.trim().toLowerCase();
        if (status === 'present') presentDays++;
        if (status === 'absent') absentDays++;
    });

    // Prepare the custom header for Excel export
    window.customExcelHeader = [
        ["Name: " + name],
        ["Department: " + department],
        [""],
        ["Total Days: " + totalDays, "Present: " + presentDays, "Absent: " + absentDays],
        [""]
    ];
});
