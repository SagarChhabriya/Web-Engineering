<?php
$host = "localhost";
$user = "root";
$password = "";
$database = "test";


$connection = mysqli_connect($host, $user,$password,$database);

if($connection){
    echo "Connection Established Successfully.";
}

?>