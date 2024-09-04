

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