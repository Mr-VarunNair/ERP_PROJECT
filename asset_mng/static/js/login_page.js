function togglePassword() {
    var passwordField = document.getElementById("password");
    var passwordFieldType = passwordField.getAttribute("type");
    var toggleEyeIcon = document.getElementById("toggle-eye");
    if (passwordFieldType === "password") {
        passwordField.setAttribute("type", "text");
        toggleEyeIcon.classList.remove("fa-eye");
        toggleEyeIcon.classList.add("fa-eye-slash");
    } else {
        passwordField.setAttribute("type", "password");
        toggleEyeIcon.classList.remove("fa-eye-slash");
        toggleEyeIcon.classList.add("fa-eye");
    }
}
var navLinks = document.querySelectorAll('.navbar a');
navLinks.forEach(function(link) {
    link.addEventListener('click', function() {
        navLinks.forEach(function(navLink) {
            navLink.classList.remove('active');
        });
        this.classList.add('active');
    });
});
