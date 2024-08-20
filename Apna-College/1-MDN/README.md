# CSS and HTML Reference

## Table of Contents

1. [Void Elements](#void-elements)
2. [Boolean Attributes](#boolean-attributes)
3. [The `<head>` Element](#the-head-element)
4. [Adding a Title](#adding-a-title)
5. [Document Fragments](#document-fragments)
6. [Download Attribute](#download-attribute)
7. [Navigation Menu](#navigation-menu)
8. [HTML for Structuring Content](#html-for-structuring-content)
9. [HTML Elements Reference](#html-elements-reference)
10. [Non-Semantic Wrappers](#non-semantic-wrappers)
11. [HTML Validation](#html-validation)
12. [Exercise](#exercise)
13. [CSS Specifications](#css-specifications)
14. [Link and Visited States](#link-and-visited-states)
15. [Combinators](#combinators)
16. [The `href` Attribute](#the-href-attribute)
17. [Valid Selectors](#valid-selectors)
18. [CSS Declarations](#css-declarations)
19. [Using `calc()` Function](#using-calc-function)
20. [Transform Functions](#transform-functions)
21. [CSS Rules](#css-rules)
22. [Shorthand Properties](#shorthand-properties)
23. [Types of Selectors](#types-of-selectors)
24. [Attribute Selectors](#attribute-selectors)
25. [Pseudo-Classes and Pseudo-Elements](#pseudo-classes-and-pseudo-elements)
26. [The Universal Selector](#the-universal-selector)
27. [Selectors and Combinators](#selectors-and-combinators)
28. [Targeting Classes on Particular Elements](#targeting-classes-on-particular-elements)
29. [Targeting Elements with Multiple Classes](#targeting-elements-with-multiple-classes)
30. [ID Selectors](#id-selectors)
31. [Attribute Selectors](#attribute-selectors)
32. [Pseudo-Classes](#pseudo-classes)
33. [User-Action Pseudo-Classes](#user-action-pseudo-classes)
34. [Pseudo-Elements](#pseudo-elements)
35. [Combining Pseudo-Classes and Pseudo-Elements](#combining-pseudo-classes-and-pseudo-elements)
36. [Generating Content with `::before` and `::after`](#generating-content-with-before-and-after)

---

## Void Elements

Void elements, also known as self-closing elements, do not have closing tags. Examples include:

- `<img>` (for images)
- `<br>` (for line breaks)
- `<hr>` (for horizontal rules)

## Boolean Attributes

Boolean attributes can be either present or absent. If present, they are treated as true. The attribute's value is typically the same as its name. Example:

```html
<input type="checkbox" checked />
```

In this example, the `checked` attribute is a boolean attribute. It indicates that the checkbox is selected when the page loads.

## The `<head>` Element

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

## Adding a Title

The `<h1>` element is used to mark up the main title of your page content. It is usually used once per page to represent the primary heading. For example:

```html
<h1>Welcome to My Website</h1>
```

## Document Fragments

A document fragment is a way to link to a specific part of a page. This is done using the `id` attribute and a fragment identifier in the URL. Example:

```html
<h2 id="Mailing_address">Mailing Address</h2>
<p>
  Want to write us a letter? Use our
  <a href="contacts.html#Mailing_address">mailing address</a>.
</p>
```

## Download Attribute

Use the `download` attribute on `<a>` elements to suggest a filename for the file being downloaded. This attribute can be used to trigger a file download when a link is clicked. Example:

```html
<a href="https://example.com/file.zip" download="filename.zip">Download File</a>
```

## Navigation Menu

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

## HTML for Structuring Content

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

## HTML Elements Reference

For a detailed list of HTML elements, visit the [MDN HTML Elements Reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Element).

## Non-Semantic Wrappers

When no semantic element is appropriate for grouping elements, use `<div>` and `<span>`. These elements help group content for styling or scripting purposes. Apply classes to make them easier to target with CSS or JavaScript.

```html
<div class="container">
  <p>This is some text inside a div.</p>
</div>
```

## HTML Validation

To ensure your HTML is correct and follows standards, use the [W3C Markup Validation Service](https://validator.w3.org/). Validating your HTML helps catch errors and improve compatibility across browsers.

## Exercise

Practice your HTML skills with these exercises:

[Marking up a Letter](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Marking_up_a_letter)
[Structuring a Page of Content](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Structuring_a_page_of_content)

## CSS Specifications

Explore CSS specifications to understand the latest features and best practices for styling web pages.

## Link and Visited States

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
