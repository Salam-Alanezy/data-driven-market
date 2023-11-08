let dataset = {};

// Helper function to format date in DD.MM.YYYY format
function formatDate(dateString) {
    const [day, month, year] = dateString.split(".");
    return `${day.padStart(2, "0")}.${month.padStart(2, "0")}.${year}`;
}

// Event delegation for handling 'Edit' and 'Delete' actions
document.querySelector("#product-table").addEventListener("click", function (e) {
    let row = e.target.closest("tr"); // Get the closest 'tr' element (table row)

    if (e.target && e.target.matches(".delete-button button")) {
        let ean = row.cells[1].textContent;
        row.parentNode.removeChild(row);
    } else if (e.target && e.target.matches(".edit-button button")) {
        let product = {
            ean: row.cells[1].textContent,
            name: row.cells[2].textContent,
            brand: row.cells[3].textContent,
            count: row.cells[4].textContent,
            price: row.cells[5].textContent,
            earliestExDate: row.cells[6].textContent,
            status: row.cells[7].textContent,
            image: row.cells[0].querySelector("img").src, // Get the image source from the image tag
        };

        // Show the edit product modal
        showEditProductModal(product, row);
    }
});

// Function to show the edit product modal with pre-filled values
function showEditProductModal(product, row) {
  
    let editProductModal = document.querySelector("#edit-product-modal");
    let imageSrc = product.image ? product.image : "https://ecommerce.laraship.com/assets/corals/images/default_product_image.png";
  
    editProductModal.innerHTML = `
        <div class="modal-content">
            <h4 class="text-center">Endre produkt</h4>
         
            <form id="edit-product-form">
                <div class="form-group">
        
           
                </div>
              
                    
                        <div class="row">
                                        <div class="col-12">
                                            <div class="form-group text-center" style="padding-top:10vh; padding-bottom:10vh;">
                                                <!-- Add a new input element for image file -->
                                                <input type="file" id="edit-image-input" accept="image/*" style="display: none;" onchange="previewImage(event)">
                                                <label for="edit-image-input" >
                                                    <img id="edit-image-preview" src="${product.image}" alt="Product Image" width="100vh;" height="100vh;" >
                                                </label>
                                                <p style="text-align:center;"> Klikk på bilde for å legge til ett nytt bilde</p>
                                            </div>
                                        </div>
                
                </div>

                    <div class="row">
                    <div class="col-6">
                        <div class="form-group">
                            <label for="edit-ean-input">EAN</label>
                            <input type="text" id="edit-ean-input" class="form-control" value="${product.ean}">
                        </div>
                        </div>

                
                <div class="col-6">
                <div class="form-group">
                    <label for="edit-name-input">Product Name</label>
                    <input type="text" id="edit-name-input" class="form-control" value="${product.name}">
                </div>
                </div>
                </div>

                <div class="row">
                <div class="col-6">
                <div class="form-group">
                    <label for="edit-brand-input">Brand</label>
                    <input type="text" id="edit-brand-input" class="form-control" value="${product.brand}">
                </div></div>
                <div class="col-6">
                <div class="form-group">
                    <label for="edit-count-input">Count</label>
                    <input type="text" id="edit-count-input" class="form-control" value="${product.count}">
                </div></div></div>


                <div class="row">
                <div class="col-4">
                <div class="form-group">
                    <label for="edit-price-input">Price</label>
                    <input type="text" id="edit-price-input" class="form-control" value="${product.price}">
                </div>
                </div>
                
                <div class="col-4">
                <div class="form-group">
                    <label for="edit-earliestExDate-input">Earliest Expiration Date</label>
                    <input type="text" id="edit-earliestExDate-input" class="form-control" value="${product.earliestExDate}">
                </div>
                </div>
                
                <div class="col-4">
                <div class="form-group">
                    <label for="edit-status-input">Status</label>
                    <input type="text" id="edit-status-input" class="form-control" value="${product.status}">
                </div>
                </div></div>
            </form>
            <div class="mt-3">
                <button class="btn btn-primary" id="edit-product-button">OK</button>
                <button class="btn btn-secondary" id="edit-product-cancel-button">Cancel</button>
            </div>
        </div>
    `;
    editProductModal.style.display = "block";
    
    document.querySelector("#edit-product-button").addEventListener("click", function () {
        // Retrieve the productID from the table row data attribute
        let updatedProduct = {
            id: dataset.id,
            ean: document.getElementById("edit-ean-input").value,
            name: document.getElementById("edit-name-input").value,
            brand: document.getElementById("edit-brand-input").value,
            count: document.getElementById("edit-count-input").value,
            price: document.getElementById("edit-price-input").value,
            earliestExDate: document.getElementById("edit-earliestExDate-input").value,
            status: document.getElementById("edit-status-input").value,
            image: document.getElementById('edit-image-input').value || dataset.image,
        };

        // Send the updated product data as a 'PUT' request to the server-side endpoint for updating
        fetch("/update-storage-products", {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(updatedProduct),
        })
        .then(response => response.json())
        .then(data => {
            console.log(updatedProduct);
           
            if (data.status === 'success') {
                // Data updated successfully, update the table row
                console.log('Product data updated successfully');
                row.cells[0].innerHTML = `<img src="${updatedProduct.image}" alt="Product Image" style="width: 50px; height: 50px;" class="text-center">`;
                row.cells[1].textContent = updatedProduct.ean;
                row.cells[2].textContent = updatedProduct.name;
                row.cells[3].textContent = updatedProduct.brand;
                row.cells[4].textContent = updatedProduct.count;
                row.cells[5].textContent = updatedProduct.price;
                row.cells[6].textContent = formatDate(updatedProduct.earliestExDate);
                row.cells[7].textContent = updatedProduct.status;

                // Close the edit form modal if needed
                editProductModal.style.display = "none";
            } else {
                console.error('Failed to update product data');
            }
        })
        .catch(error => {
            console.error('Failed to update product data:', error);
        });
    });
    
    document.querySelector("#edit-product-cancel-button").addEventListener("click", function () {
        editProductModal.style.display = "none";
    });
}

$("#manual-input-button").click(function() {
    // Open the product info form
    $("#product-info-form").show();
    $("#product-info-form");
});
// Add a product to the product table
function addProductToTable(product) {

  
    // Format the earliestExDate to display in DD.MM.YYYY format
    let formattedEarliestExDate = formatDate(product.earliestExDate);

    // Format the price to display as a decimal number
    let formattedPrice =product.price;
   
    let productTable = document.getElementById("product-table");
    productTable.insertRow()
    let row = productTable.insertRow();
    let cell1 = row.insertCell(0);
    let cell2 = row.insertCell(1);
    let cell3 = row.insertCell(2);
    let cell4 = row.insertCell(3);
    let cell5 = row.insertCell(4);
    let cell6 = row.insertCell(5);
    let cell7 = row.insertCell(6);
    let cell8 = row.insertCell(7);
    let cell9 = row.insertCell(8); // Create a new cell for 'Edit' button
    let cell10 = row.insertCell(9); // Create a new cell for 'Delete' button
  
    if (product.image == null || product.image == ""){
    // Check if product.image is available, else use the default image URL
    let imageSrc = product.image ? product.image : "https://ecommerce.laraship.com/assets/corals/images/default_product_image.png";
    cell1.innerHTML = `<img src="${imageSrc}" alt="Product Image" style="width: 50px; height: 50px;" class="text-center">`;
}else{
    cell1.innerHTML = `<img src="${product.image }" alt="Product Image" style="width: 50px; height: 50px;" class="text-center">`;
}

    
    cell2.textContent = product.ean;
    cell3.textContent = product.name;
    cell4.textContent = product.brand;
    cell5.textContent = product.count;
    cell6.textContent = formattedPrice;
    cell7.textContent = formattedEarliestExDate;
    cell8.textContent = product.status;

    cell9.innerHTML = '<button class="btn btn-warning">Edit</button>'; // Use 'btn-warning' class for yellow color
    cell9.classList.add("edit-button"); // Add 'edit-button' class to the cell
    cell10.innerHTML = '<button class="btn btn-danger">Delete</button>'; // Use 'btn-danger' class for red color
    cell10.classList.add("delete-button"); // Add 'delete-button' class to the cell
}

// Helper function to format date in DD.MM.YYYY format
function formatDate(dateString) {
    const [day, month, year] = dateString.split(".");
    return `${day.padStart(2, "0")}.${month.padStart(2, "0")}.${year}`;
}

// Helper function to format price as a decimal number
function formatPrice(price) {
    return parseFloat(price).toFixed(2);
}

// Event delegation for handling 'Edit' and 'Delete' actions
document.querySelector("#product-table").addEventListener("click", function (e) {
    // The same code as before, without any changes
    let row = e.target.closest("tr"); // Get the closest 'tr' element (table row)
    if (e.target && e.target.matches(".delete-button button")) { // Modify this line
        let ean = row.cells[1].textContent;
   
        row.parentNode.removeChild(row);
   
    } else if (e.target && e.target.matches(".edit-button button")) {
        let product = {
        
            ean: row.cells[1].textContent,
            name: row.cells[2].textContent,
            brand: row.cells[3].textContent,
            count: row.cells[4].textContent,
            price: row.cells[5].textContent,
            earliestExDate: row.cells[6].textContent,
            status: row.cells[7].textContent,
            image: row.cells[0].querySelector("img").src, // Get the image source from the image tag
        };

        // Show the edit product modal
        showEditProductModal(product, row);
    }
});
