## Sept_04_24
1. Automated Picture Changer
2. Time Watch
3. Use setInterval(asc,1000) ; + setInterval();

```js
var k=1;
function asc(){
    k = k + 1;
    if(k>10){
        k=1;
    }
    document.getElementById("id").innerHTML = k;
}

setInterval(asc,1000);
```