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
    <p>Enter the Employee ID and update the record.</p>    

    <form action="index.php" method="GET">
        <label for="empid">Employee ID</label>
        <input type="text" name="empid" >

        <label for="ename">Employee Name</label>
        <input type="text" name="ename" id="">

        <label for="salary">Employee salary </label>
        <input type="text" name="salary" id="">

        <button type="submit" name="sbt">Submit</button>
        <button type="reset"> Reset </button>

    </form>


    <?php
    
    $empid = $ename = $salary = "";

    if(isset($_GET['sbt'])){
        $empid = $_GET['empid'];
        $ename = $_GET['ename'];
        $salary = $_GET['salary'];

        // Check the record
        $result = mysqli_query($conn,"select * from temp where empid='$empid'");

        if(mysqli_num_rows($result)>0){
            $query = "Update table temp SET ename='$ename' and salary='$salary' where empid='$empid'";

            if(mysqli_query($conn,$query)){
                echo "Record Updated Successfully";
            }
            else{
                echo "Error: ". mysqli_error($conn);
            }
        }
        else{
            echo "No Such ID Found";
        }

    }
    
    
    
    
    ?>


</body>
</html>