function loadFile() {
    let x = new XMLHttpRequest();
    x.open("GET", "sample.txt", true);
    x.onreadystatechange = function () {
        document.querySelector(".data").innerHTML = this.responseText;
    }
    x.send();
}