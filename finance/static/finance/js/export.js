document.addEventListener("DOMContentLoaded", function () {
    const printPageBtn = document.getElementById('btnPrintPage');
    const printPdfBtn = document.getElementById('btnPrint');
    const excelBtn = document.getElementById('btnExcel');
    const tableId = (printPdfBtn && printPdfBtn.dataset.table) ||
                    (excelBtn && excelBtn.dataset.table) ||
                    'exportTable';
    const table = document.getElementById(tableId);
    const pageTitle = document.querySelector('h2') ? document.querySelector('h2').innerText : 'Report';
    const canvas = document.querySelector('canvas');

    // PRINT PAGE (with preview)
    if (printPageBtn) {
        printPageBtn.addEventListener('click', function () {
            document.documentElement.classList.add('print-mode', 'print-pdf');
            window.print();
            setTimeout(() => {
                document.documentElement.classList.remove('print-mode', 'print-pdf');
            }, 500);
        });
    }

    // DOWNLOAD PDF
    if (printPdfBtn && table) {
        printPdfBtn.addEventListener('click', async function () {
            const { jsPDF } = window.jspdf;
            const doc = new jsPDF('p', 'pt', 'a4');

            // Add page title
            doc.setFontSize(18);
            doc.text(pageTitle, 40, 40);
            let yPos = 60;

            // Add graph if present
            if (canvas) {
                const canvasImg = canvas.toDataURL('image/png', 1.0);
                doc.addImage(canvasImg, 'PNG', 40, yPos, 500, 200);
                yPos += 220;
            }

            // Add table with Rs. fix
            doc.autoTable({
                html: '#' + tableId,
                startY: yPos,
                styles: { fontSize: 10 },
                headStyles: { fillColor: [211, 47, 47] },
                didParseCell: function (data) {
                    if (typeof data.cell.text[0] === 'string' && data.cell.text[0].includes('₹')) {
                        data.cell.text[0] = data.cell.text[0].replace(/₹/g, 'Rs.');
                    }
                }
            });

            const safeTitle = pageTitle.replace(/\s+/g, '_').toLowerCase();
            doc.save(`${safeTitle}.pdf`);
        });
    }

    // DOWNLOAD EXCEL
    if (excelBtn && table) {
        excelBtn.addEventListener('click', function () {
            const wb = XLSX.utils.book_new();
            let sheetData = [[pageTitle], ['Generated on:', new Date().toLocaleDateString()], []];

            const headers = Array.from(table.querySelectorAll('thead th')).map(th => th.innerText);
            sheetData.push(headers);

            table.querySelectorAll('tbody tr').forEach(row => {
                const rowData = Array.from(row.querySelectorAll('td')).map(td => td.innerText);
                sheetData.push(rowData);
            });

            const ws = XLSX.utils.aoa_to_sheet(sheetData);
            XLSX.utils.book_append_sheet(wb, ws, "Sheet1");

            const safeTitle = pageTitle.replace(/\s+/g, '_').toLowerCase();
            XLSX.writeFile(wb, `${safeTitle}.xlsx`);
        });
    }
});
