let hour = 0;
let mnt = 0;
let sec = 0;
function asc() {


    sec++;

    if (sec > 59) {
        sec = 0;
        mnt = mnt + 1;
    }
    if (mnt > 59) {
        mnt = 0;
        hour = hour + 1;
    }
    if (hour > 24) {
        sec = 0;
        mnt = 0;
        hour = 0;
    }

    document.getElementById("sec").innerHTML = sec;
    document.getElementById("mnt").innerHTML = mnt + " : ";
    document.getElementById("hour").innerHTML = hour + " : ";
}
setInterval(asc, 100);