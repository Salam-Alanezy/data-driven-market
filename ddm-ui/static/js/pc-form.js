function openPopupForm() {
  var popupForm = document.getElementById('popupForm');
  popupForm.style.display = 'block';
  document.addEventListener('click', closePopupFormOutside, true);
}

function closePopupForm() {
  var popupForm = document.getElementById('popupForm');
  popupForm.style.display = 'none';
  document.removeEventListener('click', closePopupFormOutside, true);
}

function closePopupFormOutside(event) {
  var popupForm = document.getElementById('popupForm');
  var isInsideForm = popupForm.contains(event.target);
  var isCloseButton = event.target.classList.contains('popup-form-close-button');
  if (!isInsideForm || isCloseButton) {
    closePopupForm();
  }
}

window.addEventListener('DOMContentLoaded', function() {
  var contactButton = document.querySelector('.contact-button');
  contactButton.addEventListener('click', openPopupForm);

  var cancelButton = document.createElement('button');
  cancelButton.textContent = 'Cancel';
  cancelButton.classList.add('popup-form-button');
  cancelButton.addEventListener('click', closePopupForm);

  var saveButton = document.querySelector('.btn.btn-warning'); // Update this selector based on your HTML structure
  saveButton.insertAdjacentElement('beforebegin', cancelButton);

  var form = document.querySelector('form');
  form.addEventListener('submit', function(event) {
    event.preventDefault();
    sendEmail();
  });
});

async function sendEmail() {
  var firstname = document.getElementById('firstname').value;
  var lastname = document.getElementById('lastname').value;
  var city = document.getElementById('city').value;
  var zipcode = document.getElementById('zipcode').value;
  var country = document.getElementById('country').value;
  var phone = document.getElementById('phone').value;
  var email = document.getElementById('email').value;

  // Create the email data object
  var emailData = {
    firstname: firstname,
    lastname: lastname,
    city: city,
    zipcode: zipcode,
    country: country,
    phone: phone,
    email: email
  };

  try {
    var response = await fetch(apiURL+"/email/send", {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(emailData)
    });

    if (response.ok) {
      console.log('Email sent successfully');
      // Display a success message or perform any other desired actions
      showPopupMessage('success', 'Your message has been sent. One of our support team members will contact you in a few days.');
      closePopupForm();
    } else {
      console.error('Error sending email:', response.status);
      // Handle the error and display an error message if needed
      showPopupMessage('error', 'Something went wrong. Please try again.');
    }
  } catch (error) {
    console.error('Error sending email:', error);
    // Handle the error and display an error message if needed
    showPopupMessage('error', 'Something went wrong. Please try again.');
  }
}

function showPopupMessage(type, message) {
  var popupMessage = document.createElement('div');
  popupMessage.classList.add('popup-message');
  popupMessage.classList.add(type);
  popupMessage.textContent = message;

  var body = document.querySelector('body');
  body.appendChild(popupMessage);

  // Center the popup message vertically
  popupMessage.style.top = '50%';
  popupMessage.style.transform = 'translateY(-50%)';

  setTimeout(function() {
    body.removeChild(popupMessage);
  }, 3000); // Remove the popup message after 3 seconds (adjust the duration as needed)
}
