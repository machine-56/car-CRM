document.addEventListener("DOMContentLoaded", function () {
    const printPageBtn = document.getElementById('btnPrintPage');
    const printPdfBtn = document.getElementById('btnPrint');
    const excelBtn = document.getElementById('btnExcel');
    const tableId = (printPdfBtn && printPdfBtn.dataset.table) ||
                    (excelBtn && excelBtn.dataset.table) ||
                    'exportTable';
    const table = document.getElementById(tableId);

    if (printPageBtn) {
        printPageBtn.addEventListener('click', function (e) {
            e.stopPropagation();
            document.documentElement.classList.add('print-mode');
            document.documentElement.classList.remove('print-pdf');
            window.print();
            setTimeout(() => {
                document.documentElement.classList.remove('print-mode');
            }, 500);
        });
    }

    if (printPdfBtn && table) {
        printPdfBtn.addEventListener('click', function (e) {
            e.stopPropagation();
            document.documentElement.classList.add('print-pdf');
            document.documentElement.classList.remove('print-mode');
            window.print();
            setTimeout(() => {
                document.documentElement.classList.remove('print-pdf');
            }, 500);
        });
    }

    if (excelBtn && table) {
        excelBtn.addEventListener('click', function () {
            const wb = XLSX.utils.book_new();
            let sheetData = [];

            if (window.customExcelHeader) {
                sheetData = window.customExcelHeader;
            }

            const headers = Array.from(table.querySelectorAll('thead th')).map(th => th.innerText);
            sheetData.push(headers);

            table.querySelectorAll('tbody tr').forEach(row => {
                const rowData = Array.from(row.querySelectorAll('td')).map(td => td.innerText);
                sheetData.push(rowData);
            });

            const ws = XLSX.utils.aoa_to_sheet(sheetData);
            XLSX.utils.book_append_sheet(wb, ws, "Sheet1");

            XLSX.writeFile(wb, "exported_data.xlsx");
        });
    }
});
