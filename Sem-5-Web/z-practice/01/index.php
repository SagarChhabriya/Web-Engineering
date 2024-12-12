<!-- Step1: Inclde Libraries/Files -->
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
    <input type="text" name="empid" id="empid"  required/>

    <label for="ename">Employee Name</label>
    <input type="text" name="ename" id="ename" required />

    <label for="salary">Salary</label>
    <input type="text" name="salary" id="salary" required/>

    <input type="submit" name="sbt" id="sbt" value="Submit">
    <button type="reset"> Reset </button>


    </form>


    <?php
    // 1. Initialize Variables
    $empid = $ename = $salary = "";

    if(isset($_GET['sbt'])){


        $empid = $_GET['empid'];
        $ename = $_GET['ename'];
        $salary = $_GET['salary'];

        $query = "INSERT into temp(empid, ename, salary) values('$empid', '$ename','$salary')";

        if(mysqli_query($connection, $query)){
            echo "New Record Inserted Successfully.";
        }
        else{
            echo "Error" . mysqli_error($connection);
        }
    }
    
    $result = mysqli_query($connection, "SELECT empid, ename, salary from temp");
    ?>

    <table border="1px" width="px">
    <tr>
        <th>Employee ID</th>
        <th>Employee Name</th>
        <th>Salary</th>
    </tr>

    <?php
        if(mysqli_num_rows($result) > ){

            while($row = mysqli_fetch_assoc($result)){
                echo "<tr>"
                        "<td>" . $row['empid'] . "</td>"
                        "<td>" . $row['ename'] . "</td>"
                        "<td>" . $row["salary"] . "</td>"
                    "</tr>";
            }
        }
        else{
            echo "No records found";
        }
    
    
    ?>

    </table>

        <?php
        mysqli_close($connection);
        ?>

</body>
</html>