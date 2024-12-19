let counter = 0;
function next() {

    counter++;
    if (counter > 10)
        counter = 1;
    document.querySelector(".data").innerHTML = counter;

}

function prev() {

    counter--;
    if (counter < 0)
        counter = 10;

    document.querySelector(".data").innerHTML = counter;
}