let min = 0;
let sec = 0;
function asc() {
    minTag = document.getElementById("min");
    secTag = document.getElementById("sec");

    secTag.innerHTML = sec;
    sec = sec + 1;
    if (sec > 59) {
        sec = 0;
        min = min + 1;
        minTag.innerHTML = min + " : ";
    }

}
setInterval(asc, 100);