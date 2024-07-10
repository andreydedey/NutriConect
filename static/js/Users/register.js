document.getElementById('register-form').addEventListener('submit', function(event) {
    let username = document.getElementById('username').value;
    let email = document.getElementById('email').value;
    let password = document.getElementById('password').value;
    let confirmPassword = document.getElementById('confirm-password').value;

    if (username == '') {
        event.preventDefault();
        alert('The field username is empty');
        return;
    }
    
    if (email == '') {
        event.preventDefault();
        alert('The field email is empty');
        return;
    }

    if (password !== confirmPassword) {
        event.preventDefault();
        alert('The passwords must be the same');
        return;
    }
})