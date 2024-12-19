<?php include("dbcon.php"); ?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Employee Form</title>
</head>
<body>

    <form action="index.php" method="GET">
        <!-- GET: If you refresh the page, the data in url will be added again and again -->
        <!-- POST: The page refresh doesn't cause any affect because the data isn't in url -->
        <label for="empid">Employee ID</label>
        <input type="text" name="empid" id="empid" required />

        <label for="ename">Employee Name</label>
        <input type="text" name="ename" id="ename" required />

        <label for="salary">Employee Salary</label>
        <input type="text" name="salary" id="salary" required />
        <br><br>
        
        <input type="submit" name="sbt" value="Submit">
        <button type="reset">Reset</button>
    </form>

    <br><br>

    <?php
    // Initialize variables
    $empid = $ename = $salary = "";

    // Check if the submit button is pressed
    if(isset($_GET['sbt'])) {
        // Get data from the form
        $empid = $_GET['empid'];
        $ename  = $_GET['ename'];
        $salary = $_GET['salary'];


        // SQL query to insert the data into the temp table
        $query = "INSERT INTO temp (empid, ename, salary) VALUES ('$empid', '$ename', '$salary')";

        // Execute the query and check for errors
        if(mysqli_query($conn, $query)) {
            echo "New record created successfully.";
        } else {
            echo "Error: " . mysqli_error($conn);
        }
    }

    // Query the employee data from the temp table
    $result = mysqli_query($conn, "SELECT empid, ename, salary FROM temp");

    ?>

    <!-- Display Employee Data in a Table -->
    <table border="1" width="600px">
        <tr>
            <th>Employee ID</th>
            <th>Name</th>
            <th>Salary</th>
        </tr>

        <?php
        // Check if there are records to display
        if(mysqli_num_rows($result) > 0) {
            // Loop through each record and display
            while($row = mysqli_fetch_assoc($result)) {
                echo "<tr>
                        <td>" . $row["empid"] . "</td>
                        <td>" . $row["ename"] . "</td>
                        <td>" . $row["salary"] . "</td>
                    </tr>";
            }
        } 
        ?>
    </table>

    <?php
    // Close the database connection
    mysqli_close($conn);
    ?>

</body>
</html>
