let counter = 0;

function asc() {

    counter++;
    if (counter > 10)
        counter = 0;

    document.querySelector(".data").innerHTML = counter;
}
setInterval(asc, 1000);