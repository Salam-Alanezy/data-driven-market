let selectedProduct = ""; // Variable to store the selected product
let scanner = null; // Variable to store the scanner instance
let isScanning = false;  // Add this line


window.onload = function() {
  var now = new Date();
  var year = now.getFullYear();
  var month = String(now.getMonth() + 1).padStart(2, '0');
  var date = String(now.getDate()).padStart(2, '0');
  var hours = String(now.getHours()).padStart(2, '0');
  var minutes = String(now.getMinutes()).padStart(2, '0');

  var dateTime = year + '-' + month + '-' + date + 'T' + hours + ':' + minutes;
  // document.getElementById('createdAt-input').value = dateTime;
  

  // Add event listener to the EAN input field
  let eanInput = document.getElementById('ean');  // Replace 'ean-input' with the actual ID of your EAN input field
  eanInput.addEventListener('change', function() {
      onEanInputChange(eanInput.value);
  });


};


document.addEventListener('DOMContentLoaded', async (event) => {
  document.getElementById("start-button").addEventListener("click", startScanning);
  
  // Fetch storage data when the page is loaded
  await fetch('/get-storage', { // Update your route as well
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
    let cell8 = row.insertCell(7);  
    let cell9 = row.insertCell(8);  // Create a new cell for 'Delete' button
    let cell10 = row.insertCell(9);  // Create a new cell for 'Delete' button
    
    let imageSrc = product.image ? product.image : "https://ecommerce.laraship.com/assets/corals/images/default_product_image.png";
    cell1.innerHTML = `<img src="${imageSrc}" alt="Product Image" style="width: 50px; height: 50px;">`;
    cell2.textContent = product.ean;
    cell3.textContent = product.name;
    cell4.textContent = product.brand;
    cell5.textContent = product.count + ' stk.';
    cell6.textContent = product.price + ' ,-';
    cell7.textContent = product.earliestExDate;
    cell8.textContent = product.status;
    cell9.innerHTML = '<button class="btn btn-warning">Endre</button>';  // Use 'btn-danger' class for red color
    cell9.classList.add("edit-button");  // Add 'delete-button' class to the cell
    cell10.innerHTML = '<button class="btn btn-danger">Slett</button>';  // Use 'btn-danger' class for red color
    cell10.classList.add("delete-button");  // Add 'delete-button' class to the cell
}


$("#manual-input-button").click(function() {
    // Open the product info form
    $("#product-info-form").show();
});


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
    success: function (data) {
      if (data.data && data.data.products && data.data.products.length > 0) {
        let product = data.data.products[0]; // Take the first product from the array
        document.getElementById('name-input').value = product.name || '';
        document.getElementById('brand-input').value = product.brand || '';

        // Update the image preview with the product image URL
        let imagePreview = document.getElementById('image-preview');
        imagePreview.src = product.image || 'https://ecommerce.laraship.com/assets/corals/images/default_product_image.png';

        // You can also get the EAN like this if needed:
        let ean = data.data.ean;
      } else {
        // No matching products found
        console.error('No matching products found for EAN:', ean);
        showError('Failed to retrieve product information. Please try again or enter the information manually.');
      }
    },
    error: function (jqXHR, textStatus, errorThrown) {
      console.error('Error:', errorThrown);
      showError('Failed to retrieve product information. Please try again or enter the information manually.');
    }
  });
}


function showError(message) {
  let errorContainer = document.getElementById('error-container');
  let errorMessage = document.getElementById('error-message');
  errorMessage.textContent = message;
  errorContainer.style.display = 'block';

  setTimeout(function () {
    errorContainer.style.display = 'none';
  }, 3000); // Time is in milliseconds (15000 milliseconds = 15 seconds)
}

document.getElementById('error-close-button').addEventListener('click', function () {
  let errorContainer = document.getElementById('error-container');
  errorContainer.style.display = 'none';
});



document.getElementById("product-info-cancel-button").addEventListener("click", function () {
  // Close the modal without saving data when the "Avslutt" button is clicked
  let productInfoFormModal = document.getElementById("product-info-form");
  productInfoFormModal.style.display = "none";
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
 // Find the video element within the #scanner element and adjust its size
 

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
      let videoElement = document.querySelector("video");
      // videoElement.style.height = "100%";
      videoElement.style.width = "100%";
      isScanning = true; // Set isScanning flag to true
      
      
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

// Event delegation for deleting product rows and editing product rows
document.querySelector("#product-table").addEventListener("click", function (e) {
  let row = e.target.closest("tr"); // Get the closest 'tr' element (table row)
  if (e.target && e.target.matches(".delete-button button")) { // Modify this line
    let ean = row.cells[1].textContent;
    deleteProduct(ean);
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
      image: row.cells[0].querySelector("img").src,
    };


    // Show the edit product modal
    showEditProductModal(product, row);
  }
});
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
// Event delegation for deleting product rows
document.querySelector("#product-table").addEventListener("click", function (e) {
  if (e.target && e.target.matches("td.delete-button")) {
    let row = e.target.parentNode;
    row.parentNode.removeChild(row);
  }
});

document.querySelector("#product-table").addEventListener("click", function (e) {
  if (e.target && e.target.matches(".delete-button button")) { // Modify this line
    let row = e.target.closest("tr"); // Get the closest 'tr' element (table row)
    let ean = row.cells[1].textContent;
    deleteProduct(ean);
    row.parentNode.removeChild(row);
  }
});
