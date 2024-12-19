// Initialize the counter GLOBAL variable
let counter = 1;

function updateImage() {

    let image = document.getElementById("image").src = `${counter++}.png`;

    if (counter > 5)
        counter = 1;

}

setInterval(updateImage, 100);