# Table of Contents

1. [Variables in PHP](#variables-in-php)
2. [String Data Types](#string-data-types)
3. [var_dump() Function](#var_dump-function)
4. [String Functions](#string-functions)
5. [Arithmetic Operations](#arithmetic-operations)
6. [Logical Operators](#logical-operators)
7. [Control Structures](#control-structures)
   - [If-Else Statement](#if-else-statement)
   - [If-Elseif-Else Statement](#if-elseif-else-statement)
   - [Switch Case](#switch-case)
8. [Loops](#loops)
   - [While Loop](#while-loop)
   - [For Loop](#for-loop)
   - [Do-While Loop](#do-while-loop)
   - [Foreach Loop](#foreach-loop)
9. [Functions](#functions)
10. [Dates in PHP](#dates-in-php)
11. [Associative Arrays](#associative-arrays)
12. [GET and POST Requests](#get-and-post-requests)

---

## Variables in PHP

PHP is a loosely typed language, meaning you do not need to declare the data type of a variable.

## String Data Types

1. **String**
2. **Integer**
3. **Float**
4. **Boolean**
5. **Object**
6. **Array**
7. **NULL**

## `var_dump()` Function

Displays structured information (type and value) about one or more variables.

```php
var_dump() function

$friends = array("sagar", "qadeer", "kamlesh", "deepak");
echo var_dump($friends);

string concatenation
echo "The length of my string is " . strlen($name);


str_word_count($variable)
str_rev($variable)
str_pos($variable, position)
str_replace()
str_repeat($variable, number_of_repeatations )

ltrim, rtrim("<pre> this is      string with space </pre>")

echo "For a + b, the result is ". ($a + $b) . "<br>";
echo "For a - b, the result is ". ($a - $b) . "<br>";
echo "For a * b, the result is ". ($a * $b) . "<br>";
echo "For a / b, the result is ". ($a / $b) . "<br>";
echo "For a % b, the result is ". ($a / $b) . "<br>";
echo "For a ** b, the result is ". ($a ** $b) . "<br>";

logical operators
<>
and -- && 
or  -- ||

Control Sturcture in PHP
```php
    if($a > 78){
        echo "a is greater than 78";
    }
    else{
        echo "a is not greater than 78";
    }
```
<br>
    
```php
$age = 54;

if ($age >18 ) {
    echo "You can drink water with chai and alcohol";
}
elseif($age>13){
    echo "You can drink chai only with water. No alcohol for you";
}
else{
    echo "You can drink water only";
}
```

- Switch Case in PHP
```php
<? php



$age = 67;

switch($age){
case 12:
echo "You are 12 years old";
    break;
case 45:
echo "You are 45 years old";
    break;
case 56:
echo "You are 56 years old boy";
    break;
default:
echo "Your age is weird";
    break;
}
?>
```


While Loops in PHP
```php
$i = 0;
while ($i<5) {
    echo $i;
    echo "<br>";
    $i++;
}
```

For loops in PHP
```php
<? php

echo "This is for loop in action <br>";

for ($index=1; $index < 6; $index++) {
echo "The number is $index <br>";
}
?>
```


do-while loops
```php
<? php
echo "Welcome to do while loops <br>";

/*
do {
    some lines of code to be executed here;
} while(condition);
*/

$i =89;
do{
    echo "$i <br>";
}while($i<5);
?>
```

For Each loops
```php

<? php
echo "Welcome to the world of foreach loops <br>";
$arr = array("bananas", "apples", "Harpic", "Bread");

for($i=0; $i < count($arr); $i++) {
    echo $arr[$i];
    echo "<br>";
}
// Better way to do this - foreach loops
foreach ($arr as $value) {
echo "$value <br>";
}
?>
```

Functions in PHP
```php
<? php
echo "Welcome to php tutorial on functions";

function processMarks ($marksArr){
$sum = 0;
foreach ($marksArr as $value) {
$sum += $value;
}
return $value;
}
$rohanDas = [34, 98, 45, 12, 98, 93];
$sumMarks = processMarks($rohanDas);
echo "Total marks scored by rohan out of 600 is $sumMarks";

?>
```


Dates in PHP
```php
<?php  
echo = "Welcom to the world of dates<br>";
$d = date("d l");
echo "Todays date is $d <br>";
?>
```
-mktime() function in php

// Associative arrays
$favCol = array(
'shubham' => 'red',
'rohan'=> 'green',
'harry'=> 'red'
) 



get and post in Php
- index.php
```php
<?php
// Function to handle the display of results
function displayResults($method) {
    $email = '';
    $password = '';

    if ($method == 'GET') {
        // Handle GET request
        $email = filter_input(INPUT_GET, 'email', FILTER_SANITIZE_EMAIL);
        $password = filter_input(INPUT_GET, 'password', FILTER_SANITIZE_STRING);
        echo "<h1>GET Request Result</h1>";
    } elseif ($method == 'POST') {
        // Handle POST request
        $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
        $password = filter_input(INPUT_POST, 'password', FILTER_SANITIZE_STRING);
        echo "<h1>POST Request Result</h1>";
    } else {
        echo "Invalid request method.";
        return;
    }

    // Display the results
    echo "Email: " . htmlspecialchars($email) . "<br>";
    echo "Password: " . htmlspecialchars($password) . "<br>";
}

// Determine the request method and handle accordingly
if ($_SERVER["REQUEST_METHOD"] == "GET") {
    displayResults('GET');
} elseif ($_SERVER["REQUEST_METHOD"] == "POST") {
    displayResults('POST');
} else {
    // Display the form if no GET or POST request is made
    displayForm();
}

// Function to display the HTML form
function displayForm() {
    echo <<<HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form Example</title>
</head>
<body>
    <h1>Submit Form</h1>
    <!-- Form for GET request -->
    <form action="" method="get">
        <label for="email_get">Email:</label>
        <input type="email" id="email_get" name="email" required><br><br>
        <label for="password_get">Password:</label>
        <input type="password" id="password_get" name="password" required><br><br>
        <input type="submit" value="Submit GET">
    </form>

    <hr>

    <!-- Form for POST request -->
    <form action="" method="post">
        <label for="email_post">Email:</label>
        <input type="email" id="email_post" name="email" required><br><br>
        <label for="password_post">Password:</label>
        <input type="password" id="password_post" name="password" required><br><br>
        <input type="submit" value="Submit POST">
    </form>
</body>
</html>
HTML;
}
?>

```

