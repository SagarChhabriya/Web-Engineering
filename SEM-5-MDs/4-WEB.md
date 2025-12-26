# WEB

## Practical

1. index.php; Process of executing a program> VS Code, XAMPP
2. Biodata Program using div, selectors: tag, class, id; image tag, embed tag;
3. CSS, and JS: Inline, Internal, Externel
4. Centering a div, div inside a div, 
5. CSS: display-felx, justify-content, align-items, flex-direction, width, height
6. Accessing HTML Objects: innerHTML, 
7. Incrementer
8. Image Changer
9. Timer
10. AJAX and Asynchronization Concept
11. Lambda Function
12. PHP LoadFile


## Theory
1. Software VS Website
2. Types of Web Applications
3. Engineering, Regression Testing, Web Centric, Browser
4. Architectures: One-Tier, Two-Tier, Three-Tier(Web)
5. Scripting Language: Cliend Side, Server Side
6. Programming: Synchronize, Asynchronize
7. HyperText, HyperLinks, Links
8. JS Control Structure
9. DOM
10. Asynchronous Programming: Side Stack and Main Stack

MISC: How Internet Works, Static VS Dynamic, 
 



## 7. Incrementer
```js
      function update() {
            var value = document.querySelector(".value");
            var currentValue = parseInt(value.innerHTML);
            if (currentValue < 10) {
                value.innerHTML = currentValue + 1;
            } else {
                value.innerHTML = 1;
            }
        }

    </script>
</head>

<body>
    <div class="container">
        <p class="value">1</p>
        <button class="btn" onclick="update()">Next</button>
    </div>

</body>

```




## 8. Image Changer
```js
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        img {
            width: 80vh;
            height: 50vh;

        }
    </style>
    <script>

        counter = 1;

        function asc() {

            if (counter > 3) {
                counter = 1;
            }
            path = `/100-Days-of-Code/Week-1/images/work-${counter}.png`;
            image = document.getElementsByClassName("image")[0].src = path;
            console.log(document.getElementsByClassName("image")[0]);
            counter = counter + 1;

        }

        setInterval(asc, 1000); 
 


    </script>
</head>

<body>
    <div class="container">
        <img class="image" src="/100-Days-of-Code/Week-1/images/work-1.png" alt="">

    </div>
</body>

</html>
```

## 9. Timer
```js
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Timer</title>
    <link rel="stylesheet" href="style.css">
    <script src="app.js"></script>
</head>

<body>

    <div class="timer">
        <p id="min"></p>
        <p id="sec"></p>
    </div>
</body>

</html>

```

```js
let min = 0;
let sec = 0;
function asc() {
    minTag = document.getElementById("min");
    secTag = document.getElementById("sec");

    secTag.innerHTML = sec;
    sec = sec + 1;
    if (sec > 59) {
        sec = 0;
        min = min + 1;
        minTag.innerHTML = min + " : ";
    }

}
setInterval(asc, 100);
```

## 11. Lambda Function
```js
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <p id="para"></p>



    <script>
        let x = () => { return "SIBA"; }
        document.querySelector("#para").innerHTML = x();
    </script>
</body>

</html>
```

## 12. PHP LoadFile

```html
<script src="app.js"></script>
<p class="content"></p>
<button onclick="loadfile()"></button>
```

```js
function loadfile() {
    let obj = XMLHttpRequest();
    obj.open("GET", "sample.txt", true);
    obj.readystatechange = function(){
        // console.log(this.responseText);
        document.querySelector(".content").innerHTML = this.responseText;
    
    }

    obj.send();

}
```











<hr>

Web Application Development Languages
- HTML: Hyper Text Markup Lanuguage
- CSS: Cascading Style Sheet
- JavaScript: Client-Side Scripting Language
- PHP: Server-Side Scripting Language
- MySQL: Database Language



<!-- Lecture-1 -->
1. Software Engineering
- Process of analyzing user requirements and then designing, building, and testing software application, which will satisfy those requirements.
- Concerned with all aspects of software production
- SE is science and art of building a good and effiecient software system that are on time, on budget, with correct operations, acceptable and good performance.

2. Web Engineering
- Web Engineering is study of processes, conecpts, methods, and techniques used to create high quality web applications.
- Web Engineering is the applciation of systematic and computable approaches to cost effective requirements analysis, design, implementation, testing, operation, and maintenance of high-quality web applications. 

#### The Case for Web Engineering
- Web Engineering is multi-disciplinary, no single discipline.
- Web development process is different and unique.
- Individual Experience
- Little or no documentation for code/design.
- Short-term savings lead to long-term problems in operation, maintenance, usability, etc.
- Root causes of poor design
    - Development as an authoring activity
    - Development is "easy"
    - Techniques that should not be used are misapplied.
    - Techniques that should be used or not.
- Particularly alarming given...
    - Most projects are now web based.
    - More "mission-critical" apps moving to the web.
- Top Projects Pitfalls
    - 84% -Failure to meet business objectives
    - 79% -Project Shedule delays
    - 60% -Budget overrun
    - 53% -Lack of functionality

<!-- Lecture 2 -->
#### Categories of Web Applications 
(WID-CUPS)
1. Document-Centric Web Sites
1. Interactive & Transactional
1. Workflow-Based Applications
1. Collaborative & Social Web
1. Portal-Oriented
1. Ubiquitous
1. Semantic Web
<br><br>

##### Let's Discuss Each Category
1. Document-Centric Web Sites
    - Static HTML Documents
    - Manual Updates
    - Simple, stable, short response times
    - High management costs for frequent updates & large collections
    - More inconsistent/redundant info.

2. Interactive & Transactional
    - Simple interativity
    - Dynamic page creation
    - Content Updates
    - Support Transactions
    - Decentralized
    - Database Connectivity
    - Increased Complexity

3. Workflow-Based Applications
    - Designed to handle business process across departments, organizations & enterprise
    - Business logic defines the structure
    - The role of web services was standards-based
    - High complexity: autonomous entities
 
4. Collaborative & Social Web
    - Unstructured, cooperative environments
    - Interpersonal communication

    **The Social Web**<br>
    - Traditionally characterized WWW
    - Moving towards communities interest
    - Examples: Blogs, collaborative filtering systems, social bookmarking
    - Integration with other forms of web applications

5. Portal-Oriented
    - Single points-of-entry to hetrogeneous information like Yahoo!, my.pitt.edu   
    - Data warehousing: user fires query to a large database and extract information
    **Specialized Portals**<br>
    - Business portals like employee portal
    - Marketplace portals
    - Community portals (trageted groups)


6. Ubiquitous (yoo-bi-kwuh-tuhs)
    - Customized services delivered anywhere via multiple devices
    **HCI is critical**<br>
    - Limitations of devices like screen size and bandwidth
    - Context of use
    **Still an emerging fiels; most devices have single focus:**<br>
    - Personalization
    - Location aware
    - Multi-platform delivery

7. Semantic Web
    - Information on the web should be readable to machines, as well as humans
    - Using metadata to facilitate knowledge management across the WWW
    - Content syndication promotes re-use of knowledge
    - Seamless integration of data based on different conceptual models




#### Summary | Categories of Web Applications

1. **Document-Centric Web Sites**: Static websites with manual updates and simple content delivery, often resulting in high management costs for frequent changes.

2. **Interactive & Transactional**: Dynamic sites with interactive features and database connectivity supporting transactions and content updates.

3. **Workflow-Based Applications**: Systems designed to manage and automate complex business processes across departments or organizations.

4. **Collaborative & Social Web**: Platforms for unstructured, cooperative interactions, including social media and collaborative tools.

5. **Portal-Oriented**: Entry points to diverse information sources and services, often customized for specific user groups or functions.

6. **Ubiquitous**: Services accessible from various devices and contexts, focusing on personalization and multi-platform delivery.

7. **Semantic Web**: A web where information is structured with metadata to be easily processed by machines, enhancing data integration and reuse.


## Categories of Web Applications

1. **Document-Centric Web Sites**: Simple websites with fixed content that needs manual updates, often costly to maintain.
   - **Example**: [Wikipedia](https://www.wikipedia.org) - A static site with a vast collection of articles that are manually updated.

2. **Interactive & Transactional**: Websites with features that allow users to interact, update content, and perform transactions.
   - **Example**: [Amazon](https://www.amazon.com) - A dynamic e-commerce site where users can browse, interact, and make purchases.

3. **Workflow-Based Applications**: Systems designed to help manage and automate business tasks across different departments.
   - **Example**: [Salesforce](https://www.salesforce.com) - A platform that helps businesses manage their sales processes and customer relationships.

4. **Collaborative & Social Web**: Platforms for people to work together and communicate, like social media and group tools.
   - **Example**: [Facebook](https://www.facebook.com) - A social media site for sharing updates, communicating, and collaborating with friends and groups.

5. **Portal-Oriented**: Websites that provide access to a lot of different information or services, often tailored for specific groups.
   - **Example**: [Yahoo!](https://www.yahoo.com) - A portal that provides access to news, email, and other information in one place.

6. **Ubiquitous**: Services available on many different devices, focusing on personalizing and adapting to various contexts.
   - **Example**: [Google Maps](https://maps.google.com) - A service that works on various devices and provides personalized location-based information.

7. **Semantic Web**: A web where information is organized in a way that computers can easily understand and use, improving data sharing.
   - **Example**: [Schema.org](https://schema.org) - A site that provides structured data formats to help search engines understand and integrate web content.





<!-- Lecture 3 -->
##  Attributes of Web 
### What is Web?
- WWW is also known as web.
- Collection of websites or web pages stored in web servers and accessable to local computers through the internet.

### Attibtue of Web Applciations
1. Network Intensive
2. Content Driven
3. Continuous Evolution
4. Security
5. Immediacy
6. Aesthetic/Attractive
7. Usability: access to disable
8. Privacy




# Virtual Uni
1. Client Server Model: Load Balancers
2. How internet works
3. Web Job Roles: Sys Admin (H/W), DB Admin, UI/UX, Front End, Q & A, SEO, Project Management
4. Internet Protocols: 
5. URL: Protocol, Domain, Path, Query, Fragement
6. How a Web Browser Works: Fetch HTML > Fetch External Files; Browser Caching
    - Extension: Lighthouse, React Developers tools, 
7. Web Server: Computer that responds to HTTP
    - Web servers must choose and application stack to run a website. This application stack will include an 
        - Operating System
        - Web Server Software
        - A database
        - Scripting Language for dynamic request
    - Application Stack: Most Commonly used: LAMP
        - Linux Operating System
        - Apache Web Server
        - MySQL database
        - PHP Scripting Language
        - Others: WAMP, WISA, MEAN

8. HTML Code Validation: https://validator.w3.org/
    - Element, Attribute, Content, empty element (img), Nesting of elements, inline elements, block elements
9. Links, Selectors(Element, Class, ID)
