<?php
$host = "local";
$user = "root";
$password="";
$db = "test";


$connection = mysqli_connect($host,$user,$password,$db);

if($connection){
    echo "Connection Successful"
}

?>