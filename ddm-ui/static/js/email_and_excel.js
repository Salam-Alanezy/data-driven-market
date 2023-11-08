document.getElementById("download-button").addEventListener("click", function() {
    let productTable = document.getElementById("product-table"); // Get the product table
    let products = Array.from(productTable.rows).map(row => ({
        id: row.cells[0].textContent,
        name: row.cells[1].textContent,
        quantity: row.cells[2].textContent
    })); // Extract product information from the table
    
    let ws = XLSX.utils.json_to_sheet(products); // Convert JSON to sheet
    let wb = XLSX.utils.book_new(); // Create new workbook
    XLSX.utils.book_append_sheet(wb, ws, "Products"); // Append sheet to workbook
    XLSX.writeFile(wb, "products.xlsx"); // Write workbook to file
});

document.getElementById("send-button").addEventListener("click", function() {
    $('#email-modal').modal('show'); // Show the email modal
});

document.getElementById("send-email-button").addEventListener("click", function(e) {
    e.preventDefault(); // Prevent the default form submission action

    let email = document.getElementById("email-input").value; // Get the entered email

    let productTable = document.getElementById("product-table"); // Get the product table
    let products = Array.from(productTable.rows).map(row => ({
        ean: row.cells[0].textContent ,
        name: row.cells[1].textContent ,
        brand: row.cells[2].textContent ,
        count: row.cells[3].textContent ,
        price: row.cells[4].textContent ,
        earliestExDate: row.cells[5].textContent ,
        createdAt: row.cells[6].textContent 
    })); // Extract product information from the table

    fetch('/send-products', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            email: email,
            products: products
        }) // Send the email and product data as JSON
    })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                $('#email-modal').modal('hide'); // Hide the email modal
                $('#email-response-modal').modal('show'); // Show the success modal
                setTimeout(function() {
                    $('#email-response-modal').modal('hide'); // Hide the success modal after 3 seconds
                }, 3000);
            } else {
                showError('Failed to send email. Please try again.');
            }
        })
        .catch(() => {
            showError('Failed to send email. Please try again.');
        });

    $('#email-modal').modal('hide'); // Hide the email modal
});