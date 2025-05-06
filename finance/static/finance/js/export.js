document.addEventListener("DOMContentLoaded", function () {
    const printBtn = document.getElementById('btnPrint');
    const excelBtn = document.getElementById('btnExcel');

    const tableId = (printBtn && printBtn.dataset.table) ||
                    (excelBtn && excelBtn.dataset.table) ||
                    'exportTable';
    const table = document.getElementById(tableId);

    if (printBtn) {
        printBtn.addEventListener('click', function () {
            window.print();
        });
    }

    if (excelBtn && table) {
        excelBtn.addEventListener('click', function () {
            // Prepare data from table
            const wb = XLSX.utils.book_new();
            let sheetData = [];

            // Check if page-specific data is provided
            if (window.customExcelHeader) {
                sheetData = window.customExcelHeader;
            }

            // Add table headers
            const headers = Array.from(table.querySelectorAll('thead th')).map(th => th.innerText);
            sheetData.push(headers);

            // Add table body rows
            table.querySelectorAll('tbody tr').forEach(row => {
                const rowData = Array.from(row.querySelectorAll('td')).map(td => td.innerText);
                sheetData.push(rowData);
            });

            // Create worksheet and workbook
            const ws = XLSX.utils.aoa_to_sheet(sheetData);
            XLSX.utils.book_append_sheet(wb, ws, "Sheet1");

            // Export as Excel .xlsx
            XLSX.writeFile(wb, "exported_data.xlsx");
        });
    }
});
