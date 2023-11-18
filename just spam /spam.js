const { name } = require("body-parser");

const name = document.querySelector(".form-control form-control-lg");
const email = document.querySelector(".form-control form-control-lg"); 
const password = document.querySelector(".form-control form-control-lg"); 
const retypePassword = document.querySelector(".form-outline mb-4");
const submitButton = document.querySelector(".btn btn-success btn-block btn-lg signup-btn ps-5 pe-5"); 
            
if (name == null) {
    submitButton.addEventListener("click", (e) => {
        fetch("/login-user", {
            method: "post",
            headers: new Headers({'content-type': 'application/json'}),
            body: JSON.stringify({
                email: email.value,
                password: password.value,
        })
        .then(res => res.json())
        .then(data => {
            vaildateData(data);
        })
})})} 
else {
    submitButton.addEventListener("click", (e) => {
        fetch("/register-user", {
            method: "post",
            headers: new Headers({'content-type': 'application/json'}),
            body: JSON.stringify({
                name: name.value,
                email: email.value,
                password: password.value,
                retypePassword: retypePassword.value
        })
        .then(res => res.json())
        .then(data => {
            vaildateData(data);


        })
})})}


const vaildateData = (data) => {
    if(!data.name){
        alertBox(data);
    } else {
        sessionStorage.name = data.name;
        sessionStorage.email = data.email;
        location.href = "/";

    }
}

const alertBox = (data) => {
    const alertContainer = document.querySelector(".alert-box");
    const alertMsg = document.querySelector(".alert");
    alertMsg.innerHTML = data;
    alertContainer.style.top = "5%";
    setTimeout(() => {
        alertContainer.style.top = "null";
    }, 5000);
}