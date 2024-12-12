function loadFile() {
    let request = new XMLHttpRequest(); 
    request.open("GET", "sample.txt", true);
    request.onreadystatechange = function () {
        document.querySelector(".data").innerHTML = this.responseText;
    }
    request.send();
}