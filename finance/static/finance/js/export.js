document.addEventListener("DOMContentLoaded", function () {
    const printBtn = document.getElementById('btnPrint');
    const excelBtn = document.getElementById('btnExcel');

    const tableId = (printBtn && printBtn.dataset.table) || 
                    (excelBtn && excelBtn.dataset.table) || 
                    'exportTable';
    const table = document.getElementById(tableId);

    const staffName = document.getElementById('staffName') ? document.getElementById('staffName').innerText : '';
    const staffDept = document.getElementById('staffDept') ? document.getElementById('staffDept').innerText : '';

    if (printBtn) {
        printBtn.addEventListener('click', function () {
            window.print();
        });
    }

    if (excelBtn && table) {
        excelBtn.addEventListener('click', function () {
            const wb = XLSX.utils.book_new();

            // Convert table to array of arrays
            const tableData = [];
            const rows = table.querySelectorAll('tr');
            rows.forEach(row => {
                const rowData = [];
                row.querySelectorAll('th, td').forEach(cell => {
                    rowData.push(cell.innerText);
                });
                tableData.push(rowData);
            });

            // Build final data
            const finalData = [
                [staffName],         // Row 0
                [staffDept],         // Row 1
                [],                  // Row 2 (empty)
                [],                  // Row 3 (empty)
                ...tableData         // Table content
            ];

            const ws = XLSX.utils.aoa_to_sheet(finalData);

            // Add merges for first two rows (colspan = 3)
            ws['!merges'] = [
                { s: { r:0, c:0 }, e: { r:0, c:2 } }, // merge A1:C1
                { s: { r:1, c:0 }, e: { r:1, c:2 } }  // merge A2:C2
            ];

            XLSX.utils.book_append_sheet(wb, ws, 'Sheet1');
            XLSX.writeFile(wb, 'exported_data.xlsx');
        });
    }
});
