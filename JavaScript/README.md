## JavaScript basics


## What is JavaScript?
JavaScript is a powerful programming language that can add interactivity to a website. It was invented by Brendan Eich.
[MDN](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)


Note: The reason the instructions (above) place the` <script>` element near the bottom of the HTML file is that the browser reads code in the order it appears in the file.

If the JavaScript loads first and it is supposed to affect the HTML that hasn't loaded yet, there could be problems. Placing JavaScript near the bottom of an HTML page is one way to accommodate this dependency. To learn more about alternative approaches, see [Script loading strategies](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript#script_loading_strategies).

## Document Object Model (DOM)
The Document Object Model (DOM) connects web pages to scripts or programming languages by representing the structure of a document. <br>
The DOM represents a document with a logical tree. Each branch of the tree ends in a node, and each node contains objects. DOM methods allow programmatic access to the tree. With them, you can change the document's structure, style, or content.<br>
Nodes can also have event handlers attached to them. Once an event is triggered, the event handlers get executed.<br>

## DOM interfaces  
- Document, AbortController, AbortSignal.
- The Document interface represents any web page loaded in the browser and serves as an entry point into the web page's content, which is the DOM tree.

## HTML DOM
A document containing HTML is described using the Document interface, which is extended by the HTML specification to include various HTML-specific features. In particular, the Element interface is enhanced to become HTMLElement and various subclasses, each representing one of (or a family of closely related) elements.<br>

The HTML DOM API provides access to various browser features such as tabs and windows, CSS styles and stylesheets, browser history, etc. These interfaces are discussed further in the HTML DOM API documentation.<br>





# anonymous - lambda - arrow function - callback


# 1. Solution to JavaScript and CSS Issue

## Problem

When including JavaScript and CSS in your HTML, ensure that the JavaScript runs after the DOM is fully loaded. Otherwise, your script might try to manipulate elements before they are available.

## Original HTML and JavaScript

### HTML

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="19-Practice.css">
    <script src="19-Practice.js"></script>
</head>

<body>

</body>

</html>
```

```javascript
let para1 = document.createElement("p");
para1.innerText = 'I am a paragraph';
document.querySelector('body').append(para1);

para1.classList.add('red');
```

```css
.red {
    color: red;
}
```


# Operators in JavaScript

An operator is a mathematical symbol that produces a result based on two values (or variables). Below is a summary of some basic operators with examples.

| Operator                | Explanation                                                            | Symbol(s) | Example                       |
|-------------------------|------------------------------------------------------------------------|-----------|-------------------------------|
| Addition                | Adds two numbers or concatenates two strings.                          | `+`       | `6 + 9;`<br>`'Hello ' + 'world!';` |
| Subtraction, Multiplication, Division | Performs basic arithmetic operations.                             | `-, *, /` | `9 - 3;`<br>`8 * 2;`<br>`9 / 3;` |
| Assignment              | Assigns a value to a variable.                                         | `=`       | `let myVariable = 'Bob';`     |
| Strict Equality         | Tests if two values are equal and of the same type (returns Boolean).| `===`     | `let myVariable = 3;`<br>`myVariable === 4;` |
| Not, Does-Not-Equal     | Negates a value or checks if two values are not equal.                | `!, !==`  | `!(myVariable === 3);`<br>`myVariable !== 3;` |

### Note:
Mixing data types can lead to unexpected results. For example:
- `'35' + '25'` results in `'3525'` (string concatenation).
- `35 + 25` results in `60` (number addition).

Always ensure variables are of the expected type to avoid confusion.
