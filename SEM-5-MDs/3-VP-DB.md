## Visual Programming -C# Database Connection Using XAMPP


### 1. Select Query
The database and table is created in the XAMPP and the Apache + MySQL services are up.

```csharp
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using MySql.Data;
using System.Configuration;
using MySql.Data.MySqlClient;

// installed packages: MySql.Data, Nuget Framework




namespace DBConnection
{
    public partial class Form1 : Form
    {


        // 1. Connection with XAMPP: Password value should not be enclosed in single quotes
        MySqlConnection conn = new MySqlConnection("server=localhost; user=root; password=; database=test");


        // 2. Query
        string query = "Select * from temp";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

            // 4. Call the driver method
            lgv();
        }



        // 3. Driver Method
        public void lgv()
            {

                // 1. Establish the Connection i.e., open()
                conn.Open();
                
                // 2. Create a SQL Commmand using `connection` and `query`.
                MySqlCommand cmd = new MySqlCommand(query, conn);

                // 3. Load the `cmd` data to adapter.
                MySqlDataAdapter adp = new MySqlDataAdapter(cmd);


                // 4. Fill Datable using the adapter    
                DataTable dt = new DataTable();
                adp.Fill(dt);

                // 5. Assign the filled datatable to the gridview.
                dataGridView1.DataSource = dt;

                // 6. Close the connection
                conn.Close();

            }
    }
}


      

```



## 2. Insert Query
The Insert Action will be performed on the button click.


```csharp
  private void button1_Click(object sender, EventArgs e)
        {
            // 1. Prepare the insert query
            string insertQuery = "INSERT INTO temp (empid, ename, salary) VALUES (@empid, @ename, @salary)";


            // 2. try-catch block
            try
            {
                // 1. Open connection
                conn.Open();

                // 2. Create a command with the query and the connection
                MySqlCommand cmd = new MySqlCommand(insertQuery, conn);

                // 3. Add parameters to prevent SQL injection
                cmd.Parameters.AddWithValue("@empid", Convert.ToInt32(empidTextBox.Text)); // Assuming you have a TextBox for empid
                cmd.Parameters.AddWithValue("@ename", enameTextBox.Text); // Assuming you have a TextBox for ename
                cmd.Parameters.AddWithValue("@salary", Convert.ToDecimal(salaryTextBox.Text)); // Assuming you have a TextBox for salary

                // 4. Execute the query
                int rowsAffected = cmd.ExecuteNonQuery();

                // 5. Check if the insert was successful
                if (rowsAffected > 0)
                {
                    MessageBox.Show("Record inserted successfully.");
                }
                else
                {
                    MessageBox.Show("Insert failed.");
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error: " + ex.Message);
            }
            finally
            {
                // Close the connection
                conn.Close();
            }

            // 7. Update the dataGridView to reflect changes i.e., call driver method lgv()
            lgv();
        }

       
```

`@empid`, `@ename`, and `@salary` are parameters in a SQL query, not variables or column names. They act as placeholders for values that will be inserted into the query at runtime.

For example, in this line:
```csharp
cmd.Parameters.AddWithValue("@empid", empidTextBox.Text);
```
`@empid` is a placeholder in the SQL query, and `empidTextBox.Text` is the actual value entered by the user. When the query runs, `@empid` is replaced with the value from the TextBox.

- Using parameters helps prevent SQL injection and makes the code more secure and maintainable.


### 3. Clear Button
The button will clear the data from the text fields.

```csharp
 private void button4_Click(object sender, EventArgs e){
            empidTextBox.Text = "";
            enameTextBox.Text = "";
            salaryTextBox.Text = "";
 }

```


### 4. Delete Query

```csharp
 private void button3_Click(object sender, EventArgs e)
        {
            // 1. Verify the Input Field
            if (string.IsNullOrEmpty(empidTextBox.Text))
            {
                MessageBox.Show("Please enter a valid empid.");
                return;
            }


            // 2. Object: Create SQL Command object.
            MySqlCommand cmd = null;

            // 3. try-catch block
            try
            {

                // 1. Query
                string deleteQuery = "DELETE FROM temp WHERE empid = @empid";
                
                // 2. Command with query and connection
                cmd = new MySqlCommand(deleteQuery, conn);
                
                // 3. Employee id
                cmd.Parameters.AddWithValue("@empid", Convert.ToInt32(empidTextBox.Text));

                // 4. Close the connection 
                conn.Open();


                // 5. Verification Message
                if (cmd.ExecuteNonQuery() > 0)
                    MessageBox.Show("Record deleted successfully.");
                else
                    MessageBox.Show("No record found with the given empid.");
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error: " + ex.Message);
            }
            finally
            {
                if (cmd != null)
                {
                    cmd.Dispose();  // Explicitly dispose of the command object
                }
                conn.Close();  // Ensure connection is always closed
            }

            // 4. Update the dataGridView by calling the driver method lgv()
            lgv(); // Reload data
        }

        
```


## 5. Update Query

```csharp
private void button2_Click(object sender, EventArgs e)
        {


            // Ensure that empid TextBox is not empty
            if (string.IsNullOrEmpty(empidTextBox.Text))
            {
                MessageBox.Show("Please enter a valid empid.");
                return;
            }

            try
            {
                // Prepare the update query
                string updateQuery = "UPDATE temp SET ename = @ename, salary = @salary WHERE empid = @empid";

                // Create a command with the query and the connection
                MySqlCommand cmd = new MySqlCommand(updateQuery, conn);

                // Add parameters to prevent SQL injection
                cmd.Parameters.AddWithValue("@empid", Convert.ToInt32(empidTextBox.Text));  // empid
                cmd.Parameters.AddWithValue("@ename", enameTextBox.Text);                    // ename
                cmd.Parameters.AddWithValue("@salary", Convert.ToDecimal(salaryTextBox.Text)); // salary

                // Open the connection
                conn.Open();

                // Execute the query
                int rowsAffected = cmd.ExecuteNonQuery();

                // Check if the update was successful
                if (rowsAffected > 0)
                {
                    MessageBox.Show("Record updated successfully.");
                }
                else
                {
                    MessageBox.Show("No record found with the given empid.");
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error: " + ex.Message);
            }
            finally
            {
                // Close the connection
                conn.Close();
            }

            // Optionally reload the data to reflect changes
            lgv();
        }
      
```



























# Differences between Linear Probing and Bucket Hashing

- **Collision Handling**:
  - **Linear Probing**: Finds the next available slot sequentially (with end-around).
  - **Bucket Hashing**: Stores multiple items in a list (bucket) at each index.

- **Space Utilization**:
  - **Linear Probing**: Can lead to clustering, reducing space efficiency.
  - **Bucket Hashing**: Efficient space utilization as each bucket can hold multiple elements.

- **Insertion**:
  - **Linear Probing**: Slower when many collisions occur, as it searches for the next empty spot.
  - **Bucket Hashing**: Faster, adds items directly to the corresponding bucket.

- **Search Time**:
  - **Linear Probing**: Can be slower if clustering occurs, requiring more steps.
  - **Bucket Hashing**: Generally faster, but may involve linear search within crowded buckets.

- **Load Factor**:
  - **Linear Probing**: Efficiency decreases as the table gets more full (higher load factor).
  - **Bucket Hashing**: More flexible, as each bucket can hold multiple elements without significant degradation.

- **Performance Degradation**:
  - **Linear Probing**: Can degrade significantly if the table is full or has many collisions.
  - **Bucket Hashing**: More robust, as multiple elements can be stored in each bucket, reducing degradation.

## Summary:
- **Linear Probing**: Simple, but suffers from clustering and performance degradation with high load factors.
- **Bucket Hashing**: More flexible, handles collisions by storing multiple elements in a bucket, and is generally more efficient in space utilization and search performance.



```java
public class RecursiveFindMinimum {

    public static int findMinimum(int[] arr, int left, int right) {
        // Base case: If the range has only one element, return it as the minimum
        if (left == right) {
            return arr[left];
        }

        int mid = left + (right - left) / 2;

        if (arr[mid] > arr[right]) {
            return findMinimum(arr, mid + 1, right);
        } else {
            return findMinimum(arr, left, mid);
        }
    }

    public static void main(String[] args) {

        int[] arr = {7, 2, 9, 4, 1, 5};
        
        int result = findMinimum(arr, 0, arr.length - 1);
        System.out.println("Minimum element is: " + result);
    }
}
```

Q5)

- a) If the value 18 is inserted into this tree, which node becomes its parent?
    - Answer: The parent of 18 is 19.
- b) If the value 2 is inserted into this tree, which node becomes its parent?
    - Answer: The parent of 2 is 1.
- c) If we delete node 19, which node should be its replacement node?
    - Answer: The replacement node for 19 is 24.

- d) If we delete the root node 15, which node should be selected as its replacement node so that the fewest number of changes are made to the tree?
    - Answer: The replacement for the root node 15 is 19.



```java
public class BinaryTree {

    // Method to count the number of leaf nodes in the tree
    public static int countLeaves(TreeNode root) {
        // Base case: if the tree is empty, return 0
        if (root == null) {
            return 0;
        }
        // If both left and right children are null, it is a leaf node
        if (root.left == null && root.right == null) {
            return 1;
        }
        // Recursively count leaves in both subtrees
        return countLeaves(root.left) + countLeaves(root.right);
    }
    public static void main(String[] args) {
        // Creating a sample binary tree
        TreeNode root = new TreeNode(15);
        root.left = new TreeNode(7);
        root.right = new TreeNode(19);
        root.left.left = new TreeNode(3);
        root.left.right = new TreeNode(9);
        root.right.right = new TreeNode(24);
        root.left.left.left = new TreeNode(1);
        root.left.left.right = new TreeNode(2);
        root.left.right.right = new TreeNode(10);
        root.right.right.left = new TreeNode(23);
        
        // Count the number of leaf nodes
        int leafCount = countLeaves(root);
        System.out.println("Number of leaf nodes: " + leafCount);
    }
}
```
