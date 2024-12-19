function updateImage() {
    let counter = 1;
    if (coutner > 5)
        coutner = 1;
    document.getElementById("img").src = counter + ".png";
    counter++;
}
setInterval(updateImage, 100);