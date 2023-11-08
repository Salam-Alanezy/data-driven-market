function addProduct(product, quantity) {
    let productTable = document.getElementById("product-table");
    let row = productTable.insertRow();
    let cell1 = row.insertCell(0);
    let cell2 = row.insertCell(1);
    let cell3 = row.insertCell(2); // Create a new cell for 'Delete' button
  
    cell1.textContent = product;
    cell2.textContent = quantity;
    cell3.textContent = "Delete";
    cell3.classList.add("delete-button");
  
    // Create a new 'Delete' button
    cell3.innerHTML = '<button class="btn btn-danger">Delete</button>'; 
    cell3.classList.add("delete-button");
  
    startScanning();
  }
  


  document.getElementById("product-info-cancel-button").addEventListener("click", function () {
    // Close the modal without saving data when the "Avslutt" button is clicked
    let productInfoFormModal = document.getElementById("product-info-form");
    productInfoFormModal.style.display = "none";
  });