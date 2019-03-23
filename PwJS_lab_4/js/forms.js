function checkForm() {
    var error = false;
    var contactName = document.getElementById("contactName");
    var contactSurname = document.getElementById("contactSurname");
    var contactEmail = document.getElementById("contactEmail");
    var contactInfo = document.getElementById("contactInfo");

    if (contactName.value == "") {
        document.getElementById("name").className = "form-group has-error";
        document.getElementById("errorName").className = "alert alert-danger";
        error = true;
    } else {
        document.getElementById("name").className = "form-group has-success";
    }

    if (contactSurname.value == "") {
        document.getElementById("surname").className = "form-group has-error";
        document.getElementById("errorSurname").className = "alert alert-danger";
        error = true;
    } else {
        document.getElementById("surname").className = "form-group has-success";
    }
 
    if (contactEmail.value == "") {
        document.getElementById("email").className = "form-group has-error";
        document.getElementById("errorEmail").className = "alert alert-danger";
        error = true;
    } else {
        var email = contactEmail.value;
        var regex = /^[a-zA-Z0-9._-]+@([a-zA-Z0-9.-]+\.)+[a-zA-Z0-9.-]{2,4}$/;
        if (regex.test(email) == false) {
            document.getElementById("email").className = "form-group has-error";
            document.getElementById("errorEmail").innerHTML = "Zły format adresu e-mail!";
            document.getElementById("errorEmail").className = "alert alert-danger";
            error = true;
        } else {
            document.getElementById("email").className = "form-group has-success";
        }
    }

    if (contactInfo.value == "") {
        document.getElementById("info").className = "form-group has-error";
        document.getElementById("errorInfo").className = "alert alert-danger";
        error = true;
    } else {
        document.getElementById("info").className = "form-group has-success";
    }

    if (!error) {
        return true;
    }
    else {
        return false;
    }
}
}