// Qs1. Try out the following events in Event Listener on your own :
// - mouseout
// - keypress
// - Scroll
// - load
// [Use MDN for help]

window.addEventListener("load", (event) => {
    console.log("page is fully loaded");
});


// Qs2. Create a button on the page using JavaScript. Add an event listener to the button
// that changes the button’s color to green when it is clicked

button = document.createElement("button");
button.innerHTML = "Click Me!";
document.querySelector("body").append(button);

function changeColor() {
    this.style.backgroundColor = "blue";
}

button.addEventListener("click", changeColor);


// Qs3. Create an input element on the page with a placeholder ”enter your name” and an
// H2 heading on the page inside HTML.

// The purpose of this input element is to enter a user’s name so it should only input
// letters from a-z, A-Z and space (all other characters should not be detected).
// Whenever the user inputs their name, their input should be dynamically visible inside
// the heading.
// [Please note that no other character apart from the allowed characters should be
// visible in the heading]


let inputElement = document.createElement("input");
inputElement.placeholder = "enter your name";
document.querySelector("body").append(inputElement);

let h2 = document.createElement("h2");
document.body.append(h2)

inputElement.addEventListener("input", function () {
    h2.innerText = inputElement.value;
});


