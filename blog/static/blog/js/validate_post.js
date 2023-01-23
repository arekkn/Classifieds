function validateForm() {
    var form = document.getElementById('myform');
    var name = form.elements.title;
    if (name.value.length < 4) {
      alert('Title must be at least 4 characters long.');
      event.preventDefault();
    }
}

var form = document.getElementById('myform');
form.addEventListener('submit', validateForm);