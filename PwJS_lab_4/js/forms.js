function checkForm() {
    var error = false;
    var contactName = document.getElementById("contactName");
    var contactSurname = document.getElementById("contactSurname");
    var contactEmail = document.getElementById("contactEmail");
    var contactInfo = document.getElementById("contactInfo");

    if (contactName.value == "") {
        document.getElementById("errorName").className = "alert alert-danger";
        error = true;
    }

    if (contactSurname.value == "") {
        document.getElementById("errorSurname").className = "alert alert-danger";
        error = true;
    }
 
    if(contactEmail.value == "") {
        document.getElementById("errorEmail").className = "alert alert-danger";
        error = true;
    } else {
        var email = contactEmail.value;
        var regex = /^[a-zA-Z0-9._-]+@([a-zA-Z0-9.-]+\.)+[a-zA-Z0-9.-]{2,4}$/;
        if(regex.test(email) == false) {
            document.getElementById("errorEmail").innerHTML = "Zły format adresu e-mail!";
            document.getElementById("errorEmail").className = "alert alert-danger";
            error = true;
        }
    }

    if (contactInfo.value == "") {
        document.getElementById("errorInfo").className = "alert alert-danger";
        error = true;
    }

    if (!error) {
        return true;
    }
    else {
        return false;
    }
}