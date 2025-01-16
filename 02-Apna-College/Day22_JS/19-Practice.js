let para1 = document.createElement("p");
para1.innerText = 'I am a paragraph';
document.querySelector('body').append(para1);

para1.classList.add('red');


let h3 = document.createElement("h3");
h3.innerText = "I am a blue h3!";

document.querySelector("body").append(h3);
h3.classList.add("blue");


let div = document.createElement("div");
div.innerText = "Div";

let h1 = document.createElement("h1");
h1.innerText = "I'm in a div";

let p = document.createElement("p");
p.innerText = "Me Too";

div.append(h1)
div.append(p);
div.classList.add("container");
document.querySelector("body").append(div);
