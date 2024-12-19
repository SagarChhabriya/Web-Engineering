<?php
include("dbcon.php");
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
    <form action="index.php" method="GET">
    
    <label for="empid">Employee ID</label>
    <input type="text" name="empid">

    <label for="ename">Employee Name</label>
    <input type="text" name="ename">

    <label for="salary">Employee Salary</label>
    <input type="text" name="salary">

    <button type="submit" name="delete">Delete</button>
    <button type="reset">Reset</button>


    </form>


    <?php

    $empid = $ename = $salary = "";
    if(isset($_GET['delete'])){
        $empid = $_GET['empid'];
        $ename = $_GET['ename'];
        $salary = $_GET['salary'];

        $result = mysqli_query($conn, "SELECT * FROM temp");
        if(mysqli_num_rows($result) > 0){
            $deleteQuery = "DELETE FROM test where empid='$empid'";
            if(mysqli_query($conn, $deleteQuery)){
                echo "Record Deleted Successfully";
            }
            else{
                echo "Error : " . mysqli_error($conn);
            }
        }
        else{
            echo "ID Not Found";
        }


    }
    
    ?>

</body>
</html>