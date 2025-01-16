// Qsl. Create a new input and button element on the page using JavaScript only. Set the  
// text of button to "Click me' 


let inputElement = document.createElement("input");
let btn = document.createElement("button");

btn.innerText = "Click Me";

document.querySelector("body").append(inputElement);
document.querySelector("body").append(btn);

// Qs2. Add following attributes to the element : 
//  Change placeholder value of input to "username" 
//  Change the id of button to "btn'


// inputElement.type = "text";
// inputElement.placeholder = "username";

inputElement.setAttribute("placeholder", "username")
btn.setAttribute("id", "btn")


// Qs3. Access the btn using the querySelector and button id. Change the button background
// color to blue and text color to white.
document.querySelector("#btn").classList.add("btn-style");




// Qs4. Create an hl element on the page and set its text to "DOM Practice" underlined.
// Change its color to purple.

let h1 = document.createElement("h1");

// Using innerText
// h1.innerText = "DOM Practice";
// h1.classList.add("underline");

// Using innerHTML
h1.innerHTML = "<u>DOM Practice</u>"

document.querySelector("body").append(h1);





// Qs5. Create a p tag on the page and set its text to "Apna College Delta Practice",
// where Delta is bold. 

let p = document.createElement("p");
p.innerHTML = "<strong>Apna College Delta Practice<strong>";
document.querySelector("body").append(p);

