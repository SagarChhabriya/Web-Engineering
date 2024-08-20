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
