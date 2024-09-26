function loadfile() {
    let obj = XMLHttpRequest();
    obj.open("GET", "sample.txt", true);
    obj.readystatechange = function(){
        console.log(this.responseText);
    }
}