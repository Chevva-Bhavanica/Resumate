function showPage(page){

let pages=document.querySelectorAll(".page")

pages.forEach(p=>{
p.style.display="none"
})

document.getElementById(page).style.display="block"

}

showPage("home")

function login(){

let email=document.getElementById("email").value
let password=document.getElementById("password").value

console.log("Login attempt:",email,password)

/* Later connect to backend */

}
