
# CSS and HTML Reference

## Table of Contents

1. [Void Elements](#1-void-elements)
2. [Boolean Attributes](#2-boolean-attributes)
3. [The `<head>` Element](#3-the-head-element)
4. [Adding a Title](#4-adding-a-title)
5. [Document Fragments](#5-document-fragments)
6. [Download Attribute](#6-download-attribute)
7. [Navigation Menu](#7-navigation-menu)
8. [HTML for Structuring Content](#8-html-for-structuring-content)
9. [HTML Elements Reference](#9-html-elements-reference)
10. [Non-Semantic Wrappers](#10-non-semantic-wrappers)
11. [HTML Validation](#11-html-validation)
12. [Exercise](#12-exercise)
13. [CSS Specifications](#13-css-specifications)
14. [Link and Visited States](#14-link-and-visited-states)
15. [Combinators](#15-combinators)
16. [The `href` Attribute](#16-the-href-attribute)
17. [Valid Selectors](#17-valid-selectors)
18. [CSS Declarations](#18-css-declarations)
19. [Using `calc()` Function](#19-using-calc-function)
20. [Transform Functions](#20-transform-functions)
21. [CSS Rules](#21-css-rules)
22. [Shorthand Properties](#22-shorthand-properties)
23. [Types of Selectors](#23-types-of-selectors)
24. [Attribute Selectors](#24-attribute-selectors)
25. [Presence Selector](#25-presence-selector)
25. [Substring Matching Selectors](#26-substring-matching-selectors)
27. [Pseudo-Classes and Pseudo-Elements](#27-pseudo-classes-and-pseudo-elements)
28. [The Universal Selector](#28-the-universal-selector)
29. [Selectors and Combinators](#29-selectors-and-combinators)
30. [Targeting Classes on Particular Elements](#30-targeting-classes-on-particular-elements)
31. [Targeting Elements with Multiple Classes](#31-targeting-elements-with-multiple-classes)
32. [ID Selectors](#32-id-selectors)
33. [Pseudo-Classes](#33-pseudo-classes)
34. [User-Action Pseudo-Classes](#34-user-action-pseudo-classes)
35. [Pseudo-Elements](#35-pseudo-elements)
36. [Combining Pseudo-Classes and Pseudo-Elements](#36-combining-pseudo-classes-and-pseudo-elements)
37. [Generating Content with `::before` and `::after`](#37-generating-content-with-before-and-after)
38. [Descendant Combinator](#38-descendant-combinator)
39. [Child Combinator](#39-child-combinator)
40. [Next-Sibling Combinator](#40-next-sibling-combinator)
41. [Subsequent-Sibling Combinator](#41-subsequent-sibling-combinator)
42. [Creating Complex Selectors with Nesting](#42-creating-complex-selectors-with-nesting)


---

## 1 Void Elements

Void elements, also known as self-closing elements, do not have closing tags. Examples include:

- `<img>` (for images)
- `<br>` (for line breaks)
- `<hr>` (for horizontal rules)

## 2 Boolean Attributes

Boolean attributes can be either present or absent. If present, they are treated as true. The attribute's value is typically the same as its name. Example:

```html
<input type="checkbox" checked />
```

In this example, the `checked` attribute is a boolean attribute. It indicates that the checkbox is selected when the page loads.

## 3 The `<head>` Element

The `<head>` section of an HTML document contains metadata and links to resources like stylesheets and favicons. The content of `<head>` is not displayed on the page itself but provides information for rendering the page correctly. Examples of what you can include in the `<head>`:

- `<title>`: Defines the title of the page.
- `<link>`: Links to external CSS files or favicons.
- `<meta>`: Provides metadata such as the author and description.

```html
<head>
  <title>Page Title</title>
  <link rel="stylesheet" href="styles.css" />
  <meta charset="UTF-8" />
  <meta name="description" content="A description of the page" />
</head>
```

## 4 Adding a Title

The `<h1>` element is used to mark up the main title of your page content. It is usually used once per page to represent the primary heading. For example:

```html
<h1>Welcome to My Website</h1>
```

## 5 Document Fragments

A document fragment is a way to link to a specific part of a page. This is done using the `id` attribute and a fragment identifier in the URL. Example:

```html
<h2 id="Mailing_address">Mailing Address</h2>
<p>
  Want to write us a letter? Use our
  <a href="contacts.html#Mailing_address">mailing address</a>.
</p>
```

## 6 Download Attribute

Use the `download` attribute on `<a>` elements to suggest a filename for the file being downloaded. This attribute can be used to trigger a file download when a link is clicked. Example:

```html
<a href="https://example.com/file.zip" download="filename.zip">Download File</a>
```

## 7 Navigation Menu

A navigation menu is typically a list of links that help users navigate through different sections of a site. This can be structured with `<ul>` and `<li>` elements inside a `<nav>` element. Example:

```html
<nav>
  <ul>
    <li><a href="#home">Home</a></li>
    <li><a href="#about">About</a></li>
    <li><a href="#contact">Contact</a></li>
  </ul>
</nav>
```

## 8 HTML for Structuring Content

Use semantic HTML elements to structure your content logically:

- Header: `<header>` for introductory content or navigational links.
- Navigation Bar: `<nav>` for navigation links.
- Main Content: `<main>` for the primary content, with `<article>`, `<section>`, and `<div>` for further division.
- Sidebar: `<aside>` for related content, often placed inside `<main>`.
- Footer: `<footer>` for footer content.

```html
<header>
  <h1>Page Title</h1>
</header>
<nav>
  <!-- Navigation links -->
</nav>
<main>
  <article>
    <h2>Article Title</h2>
    <p>Article content...</p>
  </article>
  <aside>
    <p>Related content...</p>
  </aside>
</main>
<footer>
  <p>Footer content...</p>
</footer>
```

## 9 HTML Elements Reference

For a detailed list of HTML elements, visit the [MDN HTML Elements Reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Element).

## 10 Non-Semantic Wrappers

When no semantic element is appropriate for grouping elements, use `<div>` and `<span>`. These elements help group content for styling or scripting purposes. Apply classes to make them easier to target with CSS or JavaScript.

```html
<div class="container">
  <p>This is some text inside a div.</p>
</div>
```

## 11 HTML Validation

To ensure your HTML is correct and follows standards, use the [W3C Markup Validation Service](https://validator.w3.org/). Validating your HTML helps catch errors and improve compatibility across browsers.

## 12 Exercise

Practice your HTML skills with these exercises:

[Marking up a Letter](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Marking_up_a_letter)
[Structuring a Page of Content](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Structuring_a_page_of_content)

## 13 CSS Specifications

Explore CSS specifications to understand the latest features and best practices for styling web pages.

## 14 Link and Visited States

You can style links differently based on their state:

```css
a:link {
  color: pink; /* Unvisited links */
}

a:visited {
  color: green; /* Visited links */
}

a:hover {
  text-decoration: none; /* Links when hovered */
}
```

## 15 Combinators

CSS combinators define the relationship between selectors:

- Descendant Combinator: article p span selects `<span>` inside `<p>` inside `<article>`.
- Adjacent Sibling Combinator: `h1 + ul + p` selects `<p>` that immediately follows a `<ul>`, which follows an `<h1>`.

## 16 The href Attribute

The href attribute specifies the path to a linked resource. Here are examples of different paths:

```html
<link rel="stylesheet" href="styles/style.css" />
<!-- Same directory -->
<link rel="stylesheet" href="styles/general/style.css" />
<!-- Subdirectory -->
<link rel="stylesheet" href="../styles/style.css" />
<!-- Parent directory -->
```

## 17 Valid Selectors

Examples of valid CSS selectors:

- `h1` (selects all `<h1>` elements)
- `a:link` (selects all unvisited links)
- `.manythings` (selects all elements with class "manythings")
- `#onething` (selects the element with ID "onething")
- `*` (universal selector, selects all elements)
- `.box p` (selects all `<p>` elements inside an element with class "box")
- `.box p:first-child` (selects the first `<p>` child of elements with class "box")
- `h1, h2, .intro` (selects all `<h1>`, `<h2>`, and elements with class "intro")

## 18 CSS Declarations

A CSS declaration consists of a property and its value. Declarations are enclosed in curly braces {}. Example:

```css
p {
  color: red; /* Property: color, Value: red */
  font-size: 16px; /* Property: font-size, Value: 16px */
}
```

## 19 Using calc() Function

The `calc()` function allows for mathematical calculations in CSS. Example:

```css
.box {
  width: calc(90% - 30px); /* Width is 90% of the container minus 30 pixels */
}
```

## 20 Transform Functions

Transform functions apply transformations to elements. Example:

```css
.box {
  transform: rotate(0.8turn); /* Rotate the element by 0.8 turns */
}
```

## 21 CSS Rules

CSS rules include `@`-rules for special instructions. Examples:

- `@import`: Imports another stylesheet.
- `@media`: Creates media queries for responsive design.

```css
@import "styles2.css"; /* Imports styles from another stylesheet */

@media (max-width: 600px) {
  .box {
    width: 100%; /* Styles for screens smaller than 600px */
  }
}
```

## 22 Shorthand Properties

Shorthand properties allow setting multiple values in one line. Examples include:

- `padding: 10px 15px 20px;` /_ Sets padding for top, right, bottom, and left _/
- `margin: 5px 10px;` /_ Sets margin for top/bottom and right/left _/
- `border: 1px solid black;` /_ Sets border width, style, and color _/

## 23 Types of Selectors

CSS selectors can be:

- **Type Selector**: Selects elements by their tag name.
- **Class Selector**: Selects elements by their class name.
- **ID Selector**: Selects an element by its ID.

```css
h1 {
  /* Type selector */
  color: blue;
}

.highlight {
  /* Class selector */
  background-color: yellow;
}

#unique {
  /* ID selector */
  font-size: 20px;
}
```

## 24 Attribute Selectors

Attribute selectors target elements based on attributes:

Attribute selectors target elements based on their attributes:

```css
a[title] {
  color: blue; /* Applies to all <a> elements with a title attribute */
}

a[href^="https"] {
  color: green; /* Applies to all <a> elements with href starting with "https" */
}
```


## 25 Presence Selector
- Presence Selector: Selects elements with a specific attribute.


| Selector         | Example                       | Description                                                                                     |
|------------------|-------------------------------|-------------------------------------------------------------------------------------------------|
| `[attr]`         | `a[title]`                    | Matches elements with an `attr` attribute (whose name is the value in square brackets).|
|`[attr=value]`|`a[href="https://example.com"]`| Matches elements with an `attr` attribute whose value is exactly `value` — the string inside the quotes.|
| `[attr~=value]`  | `p[class~="special"]`         | Matches elements with an `attr` attribute whose value is exactly `value`, or contains `value` in its (space-separated) list of values. | 
|`[attr\|=value]`|`div[lang\|="zh"]`| Matches elements with an `attr` attribute whose value is exactly `value` or begins with `value` immediately followed by a hyphen. |

In the example below you can see these selectors being used:

- `li[class]` matches any list item with a class attribute. This matches all of the list items except the first one.
- `li[class="a"]` matches a selector with a class of `a`, but not a selector with a class of `a` that includes another space-separated class as part of the value. It selects the second list item.
- `li[class~="a"]` will match a class of `a` but also a value that contains `a` as part of a whitespace-separated list. It selects the second and third list items.

![](/Apna-College/1-MDN/images/presence-selector.png)

```css
li[class] {
  font-size: 200%;
}

li[class="a"] {
  background-color: yellow;
}

li[class~="a"] {
  color: red;
}
```

```html
<h1>Attribute presence and value selectors</h1>
<ul>
  <li>Item 1</li>
    <li class="a">Item 2</li>
    <li class="a b">Item 3</li>
    <li class="ab">Item 4</li>
</ul>
```


## 26 Substring Matching Selectors

These selectors allow for more advanced matching of substrings inside the value of your attribute. For example, if you had classes of `box-warning` and `box-error` and wanted to match everything that started with the string `box-`, you could use `[class^="box-"]` to select them both (or `[class|="box"]` as described in the section above).

| Selector         | Example               | Description                                                                                               |
|------------------|-----------------------|-----------------------------------------------------------------------------------------------------------|
| `[attr^=value]`  | `li[class^="box-"]`   | Matches elements with an `attr` attribute whose value begins with `value`.                               |
| `[attr$=value]`  | `li[class$="-box"]`   | Matches elements with an `attr` attribute whose value ends with `value`.                                 |
| `[attr*=value]`  | `li[class*="box"]`    | Matches elements with an `attr` attribute whose value contains `value` anywhere within the string.        |

(Aside: It may help to note that `^` and `$` have long been used as anchors in so-called regular expressions to mean "begins with" and "ends with" respectively.)

### Example Usage

- `li[class^="a"]` matches any attribute value which starts with `a`, so it matches the first two list items.
- `li[class$="a"]` matches any attribute value that ends with `a`, so it matches the first and third list items.
- `li[class*="a"]` matches any attribute value where `a` appears anywhere in the string, so it matches all of the list items.

![](/Apna-College/1-MDN/images/substring-matching.png)

```css
li[class^="a"] {
  font-size: 200%;
}

li[class$="a"] {
  background-color: yellow;
}

li[class*="a"] {
  color: red;
}
```

```html
<h1>Attribute substring matching selectors</h1>
<ul>
  <li class="a">Item 1</li>
  <li class="ab">Item 2</li>
  <li class="bca">Item 3</li>
  <li class="bcabc">Item 4</li>
</ul>
```



```css
a[title] {
  color: blue;
}
```

- Value Selector: Selects elements with a specific attribute value.

```css
Value Selector: Selects elements with a specific attribute value.
```

## 27 Pseudo-Classes and Pseudo-Elements

- **Pseudo-Classes**: Apply styles based on element states, e.g., `:hover`.

```css
a:hover {
  color: orange; /* Styles for links when hovered */
}
```

- **Pseudo-Elements**: Style specific parts of an element, e.g., `::first-line`.

```css
p::first-line {
  font-weight: bold; /* Styles the first line of paragraphs */
}
```

## 28 The Universal Selector

The universal selector `*` targets all elements on a page. For example:

```css
* {
  box-sizing: border-box; /* Applies box-sizing to all elements */
}
```

## 29 Selectors and Combinators

Selectors combined with combinators allow more precise targeting of elements:

- **Descendant Combinator**: Selects elements nested inside other elements.

```css
article p {
  color: blue; /* Selects <p> elements inside <article> */
}
```

- **Adjacent Sibling Combinator**: Selects elements directly following other elements.

```css
h1 + p {
  margin-top: 0; /* Selects <p> that immediately follows an <h1> */
}
```

## 30 Targeting Classes on Particular Elements

Apply styles to elements with specific classes:

```css
h1.highlight {
  background-color: pink; /* Applies to <h1> elements with class "highlight" */
}

span.highlight {
  background-color: yellow; /* Applies to <span> elements with class "highlight" */
}
```

## 31 Targeting Elements with Multiple Classes

Style elements with multiple classes by combining class selectors:

```css
.notebox {
  border: 4px solid #666; /* Base style for .notebox */
}

.notebox.warning {
  border-color: orange; /* Style for .notebox with additional "warning" class */
}

.notebox.danger {
  border-color: red; /* Style for .notebox with additional "danger" class */
}
```

## 32ID Selectors

ID selectors target unique elements identified by their ID attribute:

```css
#one {
  background-color: yellow; /* Applies to element with ID "one" */
}

h1#heading {
  color: rebeccapurple; /* Applies to <h1> element with ID "heading" */
}
```


## 33 Pseudo-Classes

Pseudo-classes style elements based on their state:

```css
a:hover {
  text-decoration: underline; /* Applies when the mouse is over the link */
}

input:focus {
  border-color: blue; /* Applies when the input field is focused */
}
```

## 34 User-Action Pseudo-Classes

These pseudo-classes apply styles based on user actions:

```css
button:active {
  background-color: grey; /* Styles button when it is pressed */
}

input:checked {
  background-color: green; /* Styles checkbox when checked */
}
```

## 35 Pseudo-Elements

Pseudo-elements style specific parts of an element:

```css
p::first-line {
  font-weight: bold; /* Styles the first line of <p> elements */
}

p::first-letter {
  font-size: 2em; /* Styles the first letter of <p> elements */
}
```

## 36 Combining Pseudo-Classes and Pseudo-Elements

You can combine pseudo-classes and pseudo-elements to target more specific states and parts:

```css
a:hover::after {
  content: " (hovered)"; /* Adds text after links when hovered */
}

p:first-child::before {
  content: "Note: "; /* Adds text before the first <p> child */
}
```

## 37 Generating Content with `::before` and `::after`

Use `::before` and `::after` to insert content before or after an element's actual content:

```css
.box::before {
  content: "Start - "; /* Adds "Start - " before the content of .box */
}

.box::after {
  content: " - End"; /* Adds " - End" after the content of .box */
}
```

## Combinators [MDN](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors/Combinators)

The final selectors we will look at are called combinators, because they combine other selectors in a way that gives them a useful relationship to each other and the location of content in the document.

## 38 Descendant combinator

The descendant combinator — typically represented by a single space (" ") character — combines two selectors such that elements matched by the second selector are selected if they have an ancestor (parent, parent's parent, parent's parent's parent, etc.) element matching the first selector. Selectors that utilize a descendant combinator are called descendant selectors.

```css
body article p
```

Example:

```css
.box p {
  color: red;
}
```

```html
<div class="box"><p>Text in .box</p></div>
<p>Text not in .box</p>
```

## 39 Child combinator

The child combinator (>) is placed between two CSS selectors. It matches only those elements matched by the second selector that are the direct children of elements matched by the first. Descendant elements further down the hierarchy don't match. For example, to select only `<p>` elements that are direct children of `<article>` elements:

```css
article > p
```

In this next example, we have an ordered list `<ol>` nested inside an unordered list `<ul>`. The child combinator selects only those `<li>` elements which are direct children of a `<ul>`, and styles them with a top border.<br>

If you remove the > that designates this as a child combinator, you end up with a descendant selector and all `<li>` elements will get a red border.<br>

![Child Combinator](/Apna-College/1-MDN/images/child-combinator.png)

```css
ul > li {
  border-top: 5px solid red;
}
```

```html
<ul>
  <li>Unordered item</li>
  <li>
    Unordered item
    <ol>
      <li>Item 1</li>
      <li>Item 2</li>
    </ol>
  </li>
</ul>
```

## 40 Next-sibling combinator

The next-sibling combinator (+) is placed between two CSS selectors. It matches only those elements matched by the second selector that are the next sibling element of the first selector. For example, to select all `<img>` elements that are immediately preceded by a `<p>` element:

```css
p + img
```

A common use case is to do something with a paragraph that follows a heading, as in the example below. In that example, we are looking for any paragraph which shares a parent element with an `<h1>`, and immediately follows that `<h1>`.<br><br>

If you insert some other element such as a `<h2>` in between the `<h1>` and the `<p>`, you will find that the paragraph is no longer matched by the selector and so does not get the background and foreground color applied when the element is adjacent.

![Next-Sibling-Combinator](/Apna-College/1-MDN/images/next-sibling-combinator.png)

```css
h1 + p {
  font-weight: bold;
  background-color: #333;
  color: #fff;
  padding: 0.5em;
}
```

```html
<article>
  <h1>A heading</h1>
  <p>
    Veggies es bonus vobis, proinde vos postulo essum magis kohlrabi welsh onion
    daikon amaranth tatsoi tomatillo melon azuki bean garlic.
  </p>

  <p>
    Gumbo beet greens corn soko endive gumbo gourd. Parsley shallot courgette
    tatsoi pea sprouts fava bean collard greens dandelion okra wakame tomato.
    Dandelion cucumber earthnut pea peanut soko zucchini.
  </p>
</article>
```

## 41 Subsequent-sibling combinator

If you want to select siblings of an element even if they are not directly adjacent, then you can use the subsequent-sibling combinator (~). To select all `<img>` elements that come anywhere after `<p>` elements, we'd do this:

```css
p ~ img
```

In the example below we are selecting all `<p>` elements that come after the `<h1>`, and even though there is a `<div>` in the document as well, the `<p>` that comes after it is selected.

![Subsequent-sibling-combinator](/Apna-College/1-MDN/images/subsequent-sibling-combinator.png)

```css
h1 ~ p {
  font-weight: bold;
  background-color: #333;
  color: #fff;
  padding: 0.5em;
}
```

```html
<article>
  <h1>A heading</h1>
  <p>I am a paragraph.</p>
  <div>I am a div</div>
  <p>I am another paragraph.</p>
</article>
```

## 42 Creating complex selectors with nesting

[MDN](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors/Combinators#creating_complex_selectors_with_nesting)
