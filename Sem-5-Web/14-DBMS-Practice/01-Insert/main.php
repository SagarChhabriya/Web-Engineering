<?php

include("dbcon.php");

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <script src="app.js"></script>


    <title>Document</title>
</head>
<body>
    
    <div class="container" style="background-color:#f1f1f1" >
        <h2>Users entries with password</h2>
    </div>

    <div class="imgcontainer">

    </div>

    <div class="container">

        <form action="main.php" method="GET">

            User Name: <input  type="text" placeholder="Enter Username" name="muname"  required>

            <label for="mupassw"><b>Password</b></label>
            <input type="password" name="mupassw" placeholder="Enter Password" required>

            <label for="mudes"><b>User Description</b></label>
            <input type="text" name="mudes" placeholder="Enter Description" required>

            <button type="submit" name="sbt">Save</button>


        </form>

    </div>



<?php

if(isset($_GET['sbt'])){

    $tuname = $_GET['muname'];
    $tupassw = $_GET['mupassw'];
    $tudes = $_GET['mudes'];


    $query = "insert into temp(empid, ename,salary) values('$tuname','$tupassw','$tudes')";
    $executQuery = mysqli_query($connection,$query);

    if($executQuery){
        echo "<script> alert('Data Saved') </script>"
    }

}



</body>
</html>