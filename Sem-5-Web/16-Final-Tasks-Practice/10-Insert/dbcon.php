<?php
$host = "localhost";
$user = "root";
$pass = "";
$db = "test";

$conn = mysqli_connect($host, $user, $pass,$db);
if($conn){
    echo "Connection Established Successfully";
}

?>