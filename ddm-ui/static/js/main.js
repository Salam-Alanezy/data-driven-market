let selectedProduct = ""; // Variable to store the selected product
let scanner = null; // Variable to store the scanner instance
let isScanning = false;  // Add this line

document.addEventListener('DOMContentLoaded', async (event) =>  {
    document.getElementById("start-button").addEventListener("click", startScanning);

    // Fetch storage data when the page is loaded
    await fetch('/get-storage', {  // Update your route as well
        method: 'GET',
    })
    .then(response => response.json())
    .then(data => {
        data.forEach(product => {
            addProductToTable(product);
        });
    })
    .catch(error => console.error('Error:', error));
});

// Add a product to the product table
function addProductToTable(product) {
    let productTable = document.getElementById("product-table");
    let row = productTable.insertRow();
    let cell1 = row.insertCell(0);
    let cell2 = row.insertCell(1);
    let cell3 = row.insertCell(2);
    let cell4 = row.insertCell(3);
    let cell5 = row.insertCell(4);
    let cell6 = row.insertCell(5);
    let cell7 = row.insertCell(6);
    let cell8 = row.insertCell(7);  // Create a new cell for 'Delete' button
    let cell9 = row.insertCell(8);  // Create a new cell for 'Delete' button

    cell1.textContent = product.ean;
    cell2.textContent = product.name;
    cell3.textContent = product.brand;
    cell4.textContent = product.count + ' stk.';
    cell5.textContent = product.price + ' ,-';
    cell6.textContent = product.earliestExDate;
    cell7.textContent = product.status;
    cell8.innerHTML = '<button class="btn btn-warning">Endre</button>';  // Use 'btn-danger' class for red color
    cell8.classList.add("edit-button");  // Add 'delete-button' class to the cell
    cell9.innerHTML = '<button class="btn btn-danger">Slett</button>';  // Use 'btn-danger' class for red color
    cell9.classList.add("delete-button");  // Add 'delete-button' class to the cell
}

window.onload = function() {
    var now = new Date();
    var year = now.getFullYear();
    var month = String(now.getMonth() + 1).padStart(2, '0');
    var date = String(now.getDate()).padStart(2, '0');
    var hours = String(now.getHours()).padStart(2, '0');
    var minutes = String(now.getMinutes()).padStart(2, '0');

    var dateTime = year + '-' + month + '-' + date + 'T' + hours + ':' + minutes;

    


};

$("#manual-input-button").click(function() {
    // Open the product info form
    $("#product-info-form").show();
});


function addProduct(product) {
    fetch('/saveStorageProducts', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(product)
    })
    .then(response => response.json())
    .then(data => {
        addProductToTable(data);
    })
    .catch(error => console.error('Error:', error));
}

function deleteProduct(ean) {
    fetch('/deleteFromStorage', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ ean: ean })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Product deleted');
    })
    .catch(error => console.error('Error:', error));
}

// Event delegation for deleting product rows and editing product rows
document.querySelector("#product-table").addEventListener("click", function(e) {
    let row = e.target.closest("tr");  // Get the closest 'tr' element (table row)
    if (e.target && e.target.matches(".delete-button button")) {  // Modify this line
        let ean = row.cells[0].textContent;
        deleteProduct(ean);
        row.parentNode.removeChild(row);
    } else if (e.target && e.target.matches(".edit-button button")) {
        let product = {
            ean: row.cells[0].textContent,
            name: row.cells[1].textContent,
            brand: row.cells[2].textContent,
            count: row.cells[3].textContent,
            price: row.cells[4].textContent,
            earliestExDate: row.cells[5].textContent,
            status: row.cells[6].textContent
        };
        // Show the edit product modal
        showEditProductModal(product, row);
    }
});

function startScanning() {

    if (isScanning) {
        stopScanning(); // Stop scanning if it is already running
        return;
    } 

    // Get the start button
    let startButton = document.getElementById('start-button');

    // Change the button to 'Scanning...' and turn it green
    startButton.innerHTML = '<i class="fas fa-barcode"></i> Scanning...';
    startButton.classList.remove('btn-primary');
    startButton.classList.add('btn-success');

    setTimeout(() => {
        // After 1 second, change the button to 'Stop Scanning' and turn it red
        startButton.innerHTML = '<i class="fas fa-barcode"></i> Stop Scanning';
        startButton.classList.remove('btn-success');
        startButton.classList.add('btn-danger');
    }, 1000);

    if (scanner) {
        scanner.stop();
    }

    // Initialize Quagga barcode scanner
    Quagga.init(
        {
            inputStream: {
                name: "Live",
                type: "LiveStream",
                target: document.querySelector("#scanner"),
                constraints: {
                    width: { min: 600 },
                    height: { min: 450 },
                    aspectRatio: { min: 1, max: 10 },
                    facingMode: "environment",
                },
            },
            locator: {
                patchSize: "medium",
                halfSample: true,
            },
            numOfWorkers: 2,
            frequency: 10,
            decoder: {
                readers: ["ean_reader"],
                debug: {
                    drawBoundingBox: false,
                    showFrequency: false,
                    drawScanline: false,
                    showPattern: false,
                },
                multiple: false,
            },
            locate: true,
        },
        function (err) {
            if (err) {
                console.log(err);
                return;
            }
            scanner = Quagga;
            scanner.start();
            isScanning = true; // Set isScanning flag to true

            // Find the video element within the #scanner element and adjust its size
            let videoElement = document.querySelector("video");
            if (videoElement) {
                videoElement.style.width = "100%";
                videoElement.style.height = "100%";
            }
        }
    );

    // Event listener for barcode scanning completion
    Quagga.onDetected(function (result) {
        if (result && result.codeResult && result.codeResult.code) {
            let ean = result.codeResult.code;
            scanner.stop();
            onBarcodeScanned(ean);
        }
    });
}


document.getElementById('error-close-button').addEventListener('click', function () {
    let errorContainer = document.getElementById('error-container');
    errorContainer.style.display = 'none';
});


function updateProduct(newProduct) {
    fetch('/update-storage-products', {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(newProduct)
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Dataene er oppdatert vellykket
            showSuccessMessage("Produktet er oppdatert.");
        } else {
            // Feilmelding fra serveren, vis en feilmelding
            showError('Feil ved oppdatering av produkt.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        showError('Noe gikk galt. Vennligst prøv igjen senere.');
    });
}

function showEditProductModal(product, row) {
    let editProductModal = document.querySelector("#edit-product-modal");
    editProductModal.innerHTML = `
    <div class="modal-content">
    <h4>Edit Product</h4>
    <form id="edit-product-form">
        <div class="form-group">
            <label for="edit-ean-input">EAN</label>
            <input type="text" id="edit-ean-input" class="form-control" value="${product.ean}">
        </div>
        <div class="form-group">
            <label for="edit-name-input">Product Name</label>
            <input type="text" id="edit-name-input" class="form-control" value="${product.name}">
        </div>
        <div class="form-group">
            <label for="edit-brand-input">Brand</label>
            <input type="text" id="edit-brand-input" class="form-control" value="${product.brand}">
        </div>
        <div class="form-group">
            <label for="edit-count-input">Count</label>
            <input type="text" id="edit-count-input" class="form-control" value="${product.count}">
        </div>
        <div class="form-group">
            <label for="edit-price-input">Price</label>
            <input type="text" id="edit-price-input" class="form-control" value="${product.price}">
        </div>
        <div class="form-group">
            <label for="edit-earliestExDate-input">Earliest Expiry Date</label>
            <input type="text" id="edit-earliestExDate-input" class="form-control" value="${product.earliestExDate}">
        </div>
        <div class="form-group">
            <label for="edit-createdAt-input">Created At</label>
            <input type="text" id="edit-createdAt-input" class="form-control" value="${product.status}">
        </div>
    </form>
    <div class="mt-3">
        <button class="btn btn-primary" id="edit-product-button">OK</button>
        <button class="btn btn-secondary" id="edit-product-cancel-button">Cancel</button>
    </div>
</div>

    `;
    editProductModal.style.display = "block";

    document.querySelector("#edit-product-button").addEventListener("click", function () {
        let newProduct = {
            ean: document.getElementById("edit-ean-input").value,
            // Repeat for other fields...
        };
        editProductModal.style.display = "none";
        // Update the product in the row
        row.cells[0].textContent = newProduct.ean;
        // Repeat for other fields...
        // Update the product in the server-side storage
        updateProduct(newProduct);
         // Oppdater siden (refresh)
        
    });

    document.querySelector("#edit-product-cancel-button").addEventListener("click", function () {
        editProductModal.style.display = "none";
        location.reload();
    });
}

document.getElementById("start-button").addEventListener("click", startScanning);

function showProductSelection(productNames) {
    let productSelectionModal = document.querySelector("#product-selection");
    productSelectionModal.innerHTML = `
        <div class="modal-content">
            <h4>Select Product</h4>
            <form id="product-form">
                ${productNames.map((productName, index) => `
                    <div class="form-check">
                        <input class="form-check-input" type="radio" name="product" id="product${index}" value="${productName}">
                        <label class="form-check-label" for="product${index}">
                            ${productName}
                        </label>
                    </div>
                `).join('')}
            </form>
            <div class="mt-3">
                <button class="btn btn-primary" id="product-selection-button">OK</button>
                <button class="btn btn-secondary" id="product-selection-cancel-button">Cancel</button>
            </div>
        </div>
    `;
    productSelectionModal.style.display = "block";

    document.querySelector("#product-selection-button").addEventListener("click", function () {
        selectedProduct = document.querySelector('input[name="product"]:checked').value;
        productSelectionModal.style.display = "none";
        showQuantitySelectionModal();
    });

    document.querySelector("#product-selection-cancel-button").addEventListener("click", function () {
        productSelectionModal.style.display = "none";
        startScanning();
    });
}

function onEanInputChange(ean) {
    $.ajax({
        url: '/product/' + ean,
        method: 'GET',
        success: function(data) {
            if (data.data && data.data.products && data.data.products.length > 0) {
                let product = data.data.products[0]; // Take the first product from the array
                document.getElementById('name-input').value = product.name || '';
                document.getElementById('brand-input').value = product.brand || '';
                // You can also get the EAN like this if needed:
                // let ean = data.data.ean;
            } else {
                // No matching products found
                console.error('No matching products found for EAN:', ean);
                console.log('Response data:', data); // Log the entire response data
                showError('Failed to retrieve product information. Please try again or enter the information manually.');
            }
        },
        error: function(jqXHR, textStatus, errorThrown) {
            console.error('Error:', errorThrown);
            showError('Failed to retrieve product information. Please try again or enter the information manually.');
        }
    });
}
function onEanInputChange(ean) {
    $.ajax({
        url: '/product/' + ean,
        method: 'GET',
        success: function(data) {
            if (data.data && data.data.products && data.data.products.length > 0) {
                let product = data.data.products[0]; // Take the first product from the array
                document.getElementById('name-input').value = product.name || '';
                document.getElementById('brand-input').value = product.brand || '';
                // You can also get the EAN like this if needed:
                // let ean = data.data.ean;
            } else {
                // No matching products found
                console.error('No matching products found for EAN:', ean);
                console.log('Response data:', data); // Log the entire response data
                showError('Failed to retrieve product information. Please try again or enter the information manually.');
            }
        },
        error: function(jqXHR, textStatus, errorThrown) {
            console.error('Error:', errorThrown);
            showError('Failed to retrieve product information. Please try again or enter the information manually.');
        }
    });
}

function showSuccessMessage(message) {
    let successContainer = document.getElementById('success-container');
    let successMessage = document.getElementById('success-message');
    successMessage.textContent = message;
    successContainer.style.display = 'block';

    setTimeout(function() {
        successContainer.style.display = 'none';
    }, 3000); // Skjul meldingen etter 3 sekunder (3000 millisekunder)
}

function onBarcodeScanned(ean) {

    let startButton = document.getElementById('start-button');

    // Change the button back to 'Start Scanning' and turn it blue
    startButton.innerHTML = '<i class="fas fa-barcode"></i> Start Scanning';
    startButton.classList.remove('btn-danger');
    startButton.classList.add('btn-primary');

    // Set isScanning to false
    isScanning = false;

    fetch('/product/' + ean, {
        method: 'GET'
    })
        .then(function (response) {
            if (!response.ok) {
                throw new Error('Failed to get product info');
            }
            return response.json();
        })
        .then(function (data) {
            let productNames = data.data.products.map(function (product) {
                return product.name;
            });
            setTimeout(() => {
                showProductSelection(productNames);
            }, 200);
        })
        .catch(function (error) {
            console.error('Error:', error);
            showError('Failed to retrieve product information. Please try again.');
        });
}

function showError(message) {
    let errorContainer = document.getElementById('error-container');
    let errorMessage = document.getElementById('error-message');
    errorMessage.textContent = message;
    errorContainer.style.display = 'block';

    setTimeout(function() {
        errorContainer.style.display = 'none';
    }, 3000); // Time is in milliseconds (15000 milliseconds = 15 seconds)
}

document.getElementById('error-close-button').addEventListener('click', function () {
    let errorContainer = document.getElementById('error-container');
    errorContainer.style.display = 'none';
});


function showQuantitySelectionModal() {
    let quantitySelectionModal = document.querySelector("#quantity-selection");
    quantitySelectionModal.innerHTML = `
        <div class="modal-content">
            <h4>Enter Quantity</h4>
            <form>
                <div class="form-group">

                <div class="col-md-6"> 
                <input type="number" id="quantity-input" class="form-control" placeholder="Legg til antall">
                </div>
                    
                <div class="col-md-6"> 
                <input type="text" id="brand-input" class="form-control" placeholder="Legg til leverandør">
                </div>


                <div class="col-md-6"> 
                <input type="number" id="price-input" class="form-control" placeholder="Legg til pris">
                </div>


                <div class="col-md-6"> 
                <input type="number" id="quantity-input" class="form-control" placeholder="Antall">
                </div>


                <div class="col-md-6"> 
                <input type="number" id="quantity-input" class="form-control" placeholder="Antall">
                </div>


                <div class="col-md-6"> 
                <input type="number" id="quantity-input" class="form-control" placeholder="Antall">
                </div>

                </div>
            </form>
            <div class="mt-3">
                <button class="btn btn-primary" id="quantity-selection-button">OK</button>
                <button class="btn btn-secondary" id="quantity-selection-cancel-button">Cancel</button>
            </div>
        </div>
    `;
    quantitySelectionModal.style.display = "block";

    document.querySelector("#quantity-selection-button").addEventListener("click", function () {
        let quantity = document.getElementById("quantity-input").value;

        if (quantity === '') {
            showError('Please enter a quantity.');
            return;
        }

        quantitySelectionModal.style.display = "none";
        addProduct(selectedProduct, quantity);
    });
    
    document.querySelector("#quantity-selection-cancel-button").addEventListener("click", function () {
        quantitySelectionModal.style.display = "none";
        startScanning();
    });
}

function addProduct(product, quantity) {
    let productTable = document.getElementById("product-table");
    let row = productTable.insertRow();
    let cell1 = row.insertCell(0);
    let cell2 = row.insertCell(1);
    let cell3 = row.insertCell(2);
    let cell4 = row.insertCell(3);  // Create a new cell for 'Delete' button

    cell1.textContent = product;
    cell2.textContent = quantity;
    cell3.textContent = "Delete";
    cell3.classList.add("delete-button");

    // Create a new 'Delete' button
    cell4.innerHTML = '<button class="btn btn-danger">Delete</button>';  // Use 'btn-danger' class for red color
    cell4.classList.add("delete-button");  // Add 'delete-button' class to the cell

    startScanning();
}

function stopScanning() {
    let startButton = document.getElementById('start-button');

    // Change the button back to 'Start Scanning' and turn it blue
    startButton.innerHTML = '<i class="fas fa-barcode"></i> Start Scanning';
    startButton.classList.remove('btn-danger');
    startButton.classList.add('btn-primary');

    // Stop the scanner and set the flag to false
    if (scanner) {
        scanner.stop();
        isScanning = false;
    }
}

// Event delegation for deleting product rows
document.querySelector("#product-table").addEventListener("click", function(e) {
    if (e.target && e.target.matches("td.delete-button")) {
        let row = e.target.parentNode;
        row.parentNode.removeChild(row);
    }
});

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




// document.getElementById("send-email-button").addEventListener("click", function() {
//     let email = document.getElementById("email-input").value; // Get the entered email

//     let productTable = document.getElementById("product-table"); // Get the product table
//     let products = Array.from(productTable.rows).map(row => ({
//         ean: row.cells[0].textContent,
//         name: row.cells[1].textContent,
//         brand: row.cells[2].textContent,
//         count: row.cells[3].textContent,
//         price: row.cells[4].textContent,
//         earliestExDate: row.cells[5].textContent,
//         createdAt: row.cells[6].textContent
//     })); // Extract product information from the table

//     fetch('/send_products', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify({
//             email: email,
//             products: products
//         }) // Send the email and product data as JSON
//     })
//     .then(response => response.json())
//     .then(data => {
//         if (data.status === 'success') {
//             alert('Email sent successfully!');
//             $('#email-modal').modal('hide'); // Hide the email modal
//         } else {
//             showError('Failed to send email. Please try again.');
//         }
//     })
//     .catch(() => {
//         showError('Failed to send email. Please try again.');
//     });
// });


// Event delegation for deleting product rows

document.querySelector("#product-table").addEventListener("click", function(e) {
    if (e.target && e.target.matches(".delete-button button")) {  // Modify this line
        let row = e.target.closest("tr");  // Get the closest 'tr' element (table row)
        let ean = row.cells[0].textContent;
        deleteProduct(ean);
        row.parentNode.removeChild(row);
    }
});
