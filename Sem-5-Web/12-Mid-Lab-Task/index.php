<!-- <?php include("main.php")?> -->


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
        <label for="">Employee ID</label>
        <input type="text" name="empid" id="empid" />

        <label>Employee Name</label>
        <input type="text" name="ename" id="ename">
        
        <label>Employee Address</label>
        <input type="text" name="address" id="address">
        <br> <br>
        
        <input type="submit" name="sbt" value="Submit">
        <button type="reset">Reset</button>
    </form>


    <?php
    if(isset($_GET['sbt'])){  //if button is clicked
        $empid = $_GET['empid'];
        $ename  = $_GET['ename'];
        $address = $_GET['address'];
    }
    ?> 


<table border='1' width="300px" height="100px">
    <tr>
        <td>Rno</td>
        <td>Name</td>
        <td>Address</td>
    </tr>
    <tr>
        <td><?php echo $empid ;?></td>
        <td><?php echo $ename ;?></td>
        <td><?php echo $address ;?></td>
    </tr> 
    </table>




</body>

</html>