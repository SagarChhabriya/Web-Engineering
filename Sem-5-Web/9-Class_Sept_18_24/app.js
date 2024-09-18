function ld() {

    var x = new XMLHttpRequest();
    x.open("GET", "content.txt", true);
    x.onreadystatechange = function () {
        console.log(this.responseText);

        document.querySelector("#q").innerHTML = this.responseText;

    };
    x.send();
}