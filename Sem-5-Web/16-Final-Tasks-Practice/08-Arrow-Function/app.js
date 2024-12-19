function greet() {
    const greet = () => "Hello World";
    document.querySelector(".greet_again").innerHTML = `Message: ${greet()}`;
}

function add() {
    const add = (a, b) => a + b;
    document.querySelector(".add_again").innerHTML = `Sum of 2 and 3 is ${add(2, 3)}`;
}