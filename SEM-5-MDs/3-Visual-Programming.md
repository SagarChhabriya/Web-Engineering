https://www.tutorialspoint.com/csharp/csharp_overview.htm

https://www.tutorialspoint.com/csharp/csharp_overview.htm

https://www.tutorialspoint.com/dotnet_core/index.htm



https://cuitutorial.com/visual-programming-past-paper/

https://www.studocu.com/row/document/abdul-wali-khan-university-mardan/skill-development/mcqs-visual-programming-c/15414382

https://www.w3resource.com/csharp-exercises/

https://www.studocu.com/row/document/assiut-university/visual-programming-c/c-visual-programming-practice-and-answers/20521560

 

# Introduction to Visual Programming Languages (VPL)

## Definition
Visual Programming Languages (VPL) use graphics or blocks to create programs, allowing users to build applications without writing traditional code. Instead of focusing on syntax and code structure, users can connect visual components to perform tasks.
 
## How It Works
For example, if you want to print a multiplication table in a text-based language like C, you’d write loops and syntax. In a VPL like Scratch, you simply drag and drop blocks that represent those functions, making it easier to think logically.

## Examples of Visual Programming Languages
- **Scratch:** Create stories, games, and animations using blocks.
- **Blockly:** A tool for building block-based programming languages that can generate code in JavaScript, Python, etc.
- **mBlock:** Used for programming robots.
- **Bubble:** For creating web applications.
- **Minibloq:** A graphical environment for Arduino.

## Applications of VPL
1. **Multimedia:** Users can create multimedia projects without needing to know complex coding.
2. **Education:** Tools like Scratch help students learn coding concepts through projects.
3. **Video Games:** VPLs allow for game development without traditional coding.

## Advantages of VPL
- **User-Friendly:** Great for beginners who want to learn coding basics.
- **Visual Logic:** Easier to understand and implement ideas.
- **Built-In Objects:** Access to pre-defined blocks simplifies development.
- **Custom Code:** Users can add their own code if needed.

## Disadvantages of VPL
- **Memory Usage:** VPLs require more memory due to graphics, which can slow down execution.
- **Limited Functions:** Users may encounter restrictions without custom coding.
- **Learning Curve:** Adding custom code still requires some coding knowledge.
- **Not Ideal for Professionals:** Most tech companies prefer traditional programming languages.

## Comparison: Regular Programming Languages vs. Visual Programming Languages

| Regular Languages                     | Visual Programming Languages          |
|---------------------------------------|--------------------------------------|
| Text-based programming                | Block/graphics-based programming      |
| Not beginner-friendly                 | Beginner-friendly                     |
| More customizable                     | Limited customization                 |
| Faster and more efficient             | Slower due to graphics                |
| Complex syntax                        | Simple visual interface               |
| Requires more learning time           | Easy for beginners                    |
| Requires less memory                  | Uses more memory                     |

In summary, both regular and visual programming languages have their places. VPLs simplify programming for beginners, while regular languages offer more depth and efficiency for advanced users.


## .NET Framework Components
The .NET Framework is composed of four main components:
- Common Language Runtime (CLR)
- Framework Class Library (FCL),
- Core Languages (WinForms, ASP.NET, and ADO.NET), and
- Other Modules (WCF, WPF, WF, Card Space, LINQ, Entity Framework, Parallel LINQ, Task Parallel Library, etc.)


## CLR (Common Language Runtime)
It is a program execution engine that loads and executes the program. It converts the program into native code. It acts as an interface between the framework and operating system. It does exception handling, memory management, and garbage collection. Moreover, it provides security, type-safety, interoperability, and portablility. A list of CLR components are given below:

![](assets/VP-1-net-common-language-runtime.png)

## FCL (Framework Class Library)
It is a standard library that is a collection of thousands of classes and used to build an application. The BCL (Base Class Library) is the core of the FCL and provides basic functionalities.

![](assets/VP-2-net-framework-base-class-library.png)

## WinForms
Windows Forms is a smart client technology for the .NET Framework, a set of managed libraries that simplify common application tasks such as reading and writing to the file system.

## LINQ (Language Integrated Query)
It is a query language, introduced in .NET 3.5 framework. It is used to make the query for data sources with C# or Visual Basics programming languages.

# .NET Common Language Runtime (CLR)

The .NET CLR is a runtime environment that manages and executes code written in any .NET programming language. It is the virtual machine component of the .NET framework.

## Key Features
- **Compilation**: Code from .NET-compliant languages is compiled into CLR's intermediate language, known as MSIL (Microsoft Intermediate Language), which is platform-independent and similar to Java bytecode.
- **Metadata**: During compilation, metadata is generated and stored in a Manifest file, providing information about members and types required by CLR to execute MSIL code.
- **Just-In-Time Compilation**: The CLR includes a Just-In-Time (JIT) compiler that converts MSIL code into native machine code, which is platform-dependent.
- **Management**: CLR oversees memory management, thread management, exception handling, code execution, code safety, verification, and compilation.


## The main components of CLR are:
- Common type system
- Common language speciation
- Garbage Collector
- Just in Time Compiler
- Metadata and Assemblies


## 1. Managed code:
Any language that is written in the .NET framework is managed code. Managed code use CLR, which looks after your applications by managing memory, handling security, allowing cross-language debugging, etc. The process of managed code is shown in the figure:

![](assets/VP-3-net-common-language-runtime4.png)

## 2. Unmanaged code:
The code developed outside the .NET framework is known as unmanaged code. Applications that do not run under the control of the CLR are said to be unmanaged. Certain languages such as C++ can be used to write such applications, such as low-level access functions of the operating system. Background compatibility with VB, ASP, and COM are examples of unmanaged code. This code is executed with the help of wrapper classes. The unmanaged code process is shown below:

![](assets/VP-4-net-common-language-runtime5.png)




# BackgroundWorker in C#

## Overview
The `BackgroundWorker` class allows you to run tasks in the background while keeping your user interface (UI) responsive. It is useful for long-running tasks in Windows Forms applications.

## Usage
- **Run Background Tasks:** Perform tasks like file I/O or web requests without blocking the main UI.
- **Report Progress:** Update the UI with progress, such as in a progress bar.
- **Cancel Tasks:** Easily cancel ongoing tasks if needed.

## Key Components
1. **DoWork Event:** Where the background task runs.
2. **ProgressChanged Event:** Reports progress to the UI.
3. **RunWorkerCompleted Event:** Called when the task finishes.

## Pros and Cons

### Pros
- **Easy to Use:** Simple setup for background tasks.
- **Responsive UI:** Keeps the application responsive during long tasks.
- **Built-in Features:** Supports progress reporting and cancellation.

### Cons
- **UI-Focused:** Mainly for Windows Forms; not suitable for all scenarios.
- **Not Best for CPU-Intensive Tasks:** Better for I/O-bound tasks.
- **Limited Control Over Threads:** Less control compared to using `Thread` or `Task`.

## When to Use BackgroundWorker
- In Windows Forms applications to keep the UI responsive.
- For simple tasks that require progress updates and cancellation.

## Synchronous vs. Asynchronous Programming

### Synchronous Programming
- **Definition:** Tasks run one after another.
- **Pros:** Easy to understand and debug.
- **Cons:** Can freeze the UI during long tasks.

### Asynchronous Programming
- **Definition:** Tasks can run at the same time.
- **Pros:** Keeps the application responsive and uses resources efficiently.
- **Cons:** More complex to manage.

## Conclusion
`BackgroundWorker` is great for running background tasks in Windows Forms. For complex tasks, consider using `Task` and async/await. Understanding when to use synchronous versus asynchronous programming is important for building responsive applications.


# Shera
<pre>

                           +-----------------------+
                           |     .NET Framework    |
                           +-----------------------+
                                      |
            +-------------------------+-------------------------+
            |                                                   |
    +------------------+                                +-------------------+
    |      CLR         |                                |        BCL        |
    +------------------+                                +-------------------+
            |
+-----------+-----------+
|           |           |          +-----------------+
|           |           |          | Application      |
|           |           +----------| Domains          |
|           |                      +-----------------+
|           |                      | Assemblies       |
|           |                      +-----------------+
|           |                      | Managed Code     |
|           |                      +-----------------+
|           |                      | Common Type      |
|           |                      | System (CTS)     |
|           |                      +-----------------+
|           |                      | Common Language   |
|           |                      | Specification (CLS)|
|           |                      +-----------------+
|           |    
|           +-------------------------------------------+
|                                                       |
|  +-----------------+ +------------------+ +-----------------+
|  | Execution       | | Memory           | | Security        |
|  | Management      | | Management       | |                 |
|  +-----------------+ +------------------+ +-----------------+
|  | Exception       | | Interoperability  | | Debugging and   |
|  | Handling        | +------------------+ | Profiling       |
|  +-----------------+                      +-----------------+

</pre>

# .NET Framework Architecture Theory

The .NET Framework is a comprehensive software development platform designed by Microsoft to facilitate building and running applications across various environments. Its architecture is structured to provide a consistent and efficient programming model, ensuring seamless interoperability among different languages and technologies.

## Key Components of .NET Framework Architecture

### 1. Common Language Runtime (CLR)
- **Execution Management**: The CLR compiles Intermediate Language (IL) code into native machine code at runtime, allowing applications to run efficiently on different hardware platforms.
- **Memory Management**: Automatic garbage collection helps reclaim memory allocated to objects that are no longer in use, preventing memory leaks and optimizing resource usage.
- **Security**: The CLR enforces Code Access Security (CAS) to ensure that applications have the appropriate permissions, safeguarding system resources from unauthorized access.
- **Exception Handling**: It provides a structured approach to handling runtime errors, ensuring that applications can recover gracefully from unexpected issues.
- **Interoperability**: The CLR allows .NET applications to interact with components from other platforms, including COM objects and native Windows APIs.
- **Debugging and Profiling**: Integrated tools help developers identify and resolve issues in their applications, enhancing performance and reliability.

### 2. Base Class Library (BCL)
- The BCL is a rich collection of pre-built classes, interfaces, and data types that provide foundational functionalities for application development. It includes libraries for file I/O, data access, string manipulation, networking, and more.
- The BCL promotes code reuse and accelerates development by offering standardized components that developers can leverage across different applications.

### 3. Application Domains
- Application domains are isolated environments within the CLR that allow multiple applications to run concurrently while maintaining security and reliability. Each application domain can load and execute assemblies independently, which helps prevent crashes from affecting other applications.

### 4. Assemblies
- Assemblies are the building blocks of .NET applications, typically packaged as DLLs or EXEs. They contain the compiled code, metadata, and manifest information necessary for the CLR to manage the execution of the code.
- Assemblies ensure versioning, security, and deployment of applications, allowing for modular development.

### 5. Managed Code
- Managed code is any code that runs under the control of the CLR, benefiting from services such as garbage collection, type safety, and security checks. This allows developers to focus on business logic rather than low-level programming details.

### 6. Common Type System (CTS)
- The CTS defines a standard set of data types and rules for declaring and managing them in the .NET environment. This ensures that types created in different .NET languages (like C#, VB.NET, etc.) can interact seamlessly, promoting language interoperability.

### 7. Common Language Specification (CLS)
- The CLS is a subset of the CTS that defines a standard for language interoperability within the .NET Framework. It ensures that any language that conforms to the CLS can interact with code written in other languages, facilitating the use of multiple programming languages in a single application.

## Summary
The architecture of the .NET Framework is designed to provide a robust, scalable, and secure environment for application development. By leveraging the CLR and BCL, along with key concepts like application domains and assemblies, the .NET Framework simplifies many aspects of programming, allowing developers to create high-quality applications efficiently. Its emphasis on managed code and interoperability among languages fosters a diverse ecosystem that can cater to a wide range of development needs.






























## Table of contents
1. Bubble Sort
2. Selection Sort
3. Color Changer
4. Stripmenu
5. Group Box (Radio Button, Check Box, List Box)
6. Timer
7. Picture
8. Background
9. DateTimePicker
10. FileDialog
11. BackgroundWorker
12. Tooltip
13. DataGridView


## Sorting

```js
using System;

public class Class2
{
    public Class2()
    {

    }
    static void Main(string[] args){
        //Console.WriteLine("RADHE RADHE FROM PROGRAM.CS");
        Class2 obj = new Class2();
        int[] arr = { 7, 2, 3, 5, 4, 6, 1, 8, 9 };
        //Console.WriteLine(obj.contains(arr, 5));

        //obj.reverseArray();

        int[] result = bubblesort(arr);
        Console.WriteLine(string.Join(" ",result));
        Console.WriteLine(string.Join(" ", selectionsort(arr)));
        Console.ReadKey();
    }

     public static int[] selectionsort(int[] arr){
     for (int i = 0; i < arr.Length - 1; i++)
     {
         int start = i;
         for (int j = i + 1; j < arr.Length; j++)
         {
             if (arr[j] < arr[start])
             {
                 start = j;
             }
         }
         int temp = arr[i];
         arr[i] = arr[start];
         arr[start] = temp;
     }
     return arr;
 }

 public static int[] ForLoopSelectionSort(int[] arr)
{
    int end = arr.Length; // Get the length of the array

    // Step 2: Repeat While i < end - 1
    for (int i = 0; i < end - 1; i++)
    {
        // Step 3: Set j := i + 1
        for (int j = i + 1; j < end; j++)
        {
            // Step 5: If arr[i] > arr[j] then interchange
            if (arr[i] > arr[j])
            {
                // Interchange
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        // Step 7 is implicit; for loop automatically increments i
    }

    // Step 8: Exit
    return arr;
}



 public static int[] bubblesort(int[] arr)
 {
     int end = arr.Length;
     for (int i = 0; i < end - 1; i++)
     {
         for (int j = 0; j < end - i - 1; j++)
         {
             if (arr[j] > arr[j + 1])
             {
                 // Swap arr[j] and arr[j+1]
                 int temp = arr[j];
                 arr[j] = arr[j + 1];
                 arr[j + 1] = temp;
             }
         }
     }
     return arr;
 }


}

```






## Color Changer
```js
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp5
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {

            //BackColor = Color.Turquoise;

            int r, g, b;
            Random random = new Random();
            r = random.Next(0,255);
            g = random.Next(0,255); 
            b = random.Next(0,255); 
            
            
            BackColor = Color.FromArgb(r, g, b);    
            WindowState = FormWindowState.Maximized;
        }
    }
}
```


## Strip Menu
```python
#  Inside Partial Class
 
 private void pictureHandlerToolStripMenuItem_Click(object sender, EventArgs e)
 {
     this.Hide();
     new Form2().Show();
 }

 private void backgroundToolStripMenuItem_Click(object sender, EventArgs e)
 {
     this.Hide();
     new Form3().Show(); 
 }

```


## Group Box (Radio Button, Check Box, List Box)
## Timer

```js
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Sept_06
{
    public partial class Form1 : Form
    {
        int k = 1;
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            WindowState = FormWindowState.Minimized;
            BackColor = Color.Beige;
            label1.Text = Convert.ToString(k);
            timer1.Interval = 1000;
            timer1.Start();
        // Timer tick event will fire

        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            k = k + 1;
            if (k > 10)
            {
                k = 1;
            }
            label1.Text = k.ToString();
        }
    }
}

```


## Picture Changer
```js
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Sept_06
{
    public partial class Form2 : Form
    {   
        static int index = 1;
        string path = "D:\\Ao\\Code\\WebCode\\Web-Engineering\\100-Days-of-Code\\Week-2\\responsive-blog\\css\\assets\\dog" + index.ToString() + ".jpg";
        public Form2()
        {
            InitializeComponent();
        }

        private void Form2_Load(object sender, EventArgs e)
        {
            WindowState = FormWindowState.Minimized;
            BackColor = Color.Khaki;
            timer1.Interval = 1000;
            timer1.Start(); 
            try
            {
                pictureBox1.Image = Image.FromFile(path);   
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }

        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            index = index + 1;
            string path = "D:\\Ao\\Code\\WebCode\\Web-Engineering\\100-Days-of-Code\\Week-2\\responsive-blog\\css\\assets\\dog" + index.ToString() + ".jpg";
            if (index > 10)
            {
                index = 1; 
            }
            try
            {
                pictureBox1.Image = Image.FromFile(path);
            }
            catch(Exception ex)
            {

            }


        }
    }
}

```


## Background Changer
```js
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Sept_06
{
    public partial class Form3 : Form
    {
        public Form3()
        {
            InitializeComponent();
        }

        private void Form3_Load(object sender, EventArgs e)
        {
            WindowState = FormWindowState.Minimized;
            BackColor = Color.Aqua;
            //timer1.Interval = 1000;
            //timer1.Start();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            //Random rnd= new Random();
            //int r = rnd.Next(0, 255);
            //int g = rnd.Next(0, 255);
            //int b = rnd.Next(0, 255);

            //BackColor = Color.FromArgb(r, g, b);

        }
    }
}

```


## DateTimePicker
```js
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Sept_10_Date_Time_Picker
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void dateTimePicker1_ValueChanged(object sender, EventArgs e)
        {
            label1.Text = dateTimePicker1.Text;
        }

        private void fontDialog1_Apply(object sender, EventArgs e)
        {

            // apply font to the label
            label1.Font = fontDialog1.Font;
            //fontDialog1_Apply.Apply += new EventHandler(fontDialog1_Apply);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            fontDialog1.ShowDialog();
            label1.Font = fontDialog1.Font;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            colorDialog1.ShowDialog();
            label1.ForeColor = colorDialog1.Color;  
        }

        private void button2_Click(object sender, EventArgs e)
        {
            FontDialog fontObject = new FontDialog();
            if(fontDialog1.ShowDialog() == DialogResult.OK)
            {
                fontObject.ShowDialog();
                label1.Font = fontObject.Font;
            }

           
        }

        private void diceGameToolStripMenuItem_Click(object sender, EventArgs e)
        {


            // open the dice game form
            new Form2().Show();
            this.Hide();
        }
    }
}

```


## FileDialog
```js
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Sept_20_File_Dialog
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void SelectFile_Click(object sender, EventArgs e)
        {
            OpenFileDialog fileDialog = new OpenFileDialog();
            // choose image
            fileDialog.Filter = "ChooseImage(*.png;*.jgp;*.GIF)|*.png;*.jgp;*.GIF";
            fileDialog.ShowDialog();
            pictureBox1.Image = Image.FromFile(fileDialog.FileName);
            
            for(int i = 0; i<100; i++)
            {
                progressBar1.Value = i;
            }
            
        }
    }
}

```


## Background Worker
```js
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Sept_24_Back___
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //backgroundWorker has 3 workress
            // 1. Do worker 2. Progress changed 3. Work completed
            // Do work       progress changed       completedtask
            
            //backgroundWorker1.WorkerReportsProgress = true;
            //backgroundWorker1.WorkerSupportsCancellation = true;


        }

        private void backgroundWorker1_DoWork(object sender, DoWorkEventArgs e)
        {
            for (int i=1; i<= 100; i++){
                Thread.Sleep(90);
                //backgroundWorker1.ProgressChanged += backgroundWorker1_ProgressChanged; 
                backgroundWorker1.ReportProgress(0);
                // report progress will call the progress changed

            }
        }

        private void backgroundWorker1_ProgressChanged(object sender, ProgressChangedEventArgs e)
        {
            progressBar1.Value += 1;
            // after progress changed RunWorkerComplete will be called
        }

        private void backgroundWorker1_RunWorkerCompleted(object sender, RunWorkerCompletedEventArgs e)
        {
            MessageBox.Show("Task Completed");
        }

        private void button1_Click(object sender, EventArgs e)
        {
            backgroundWorker1.WorkerReportsProgress = true;
            backgroundWorker1.RunWorkerAsync();

            // by default the RunWorkerAsync will call the DoWorker
            // 

        }
    }
}

```


## Tooltip

```js
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Sept_27_tooltip
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // Add a media player

            
        }

        private void axWindowsMediaPlayer2_Enter(object sender, EventArgs e)
        {
            axWindowsMediaPlayer2.URL = "D:\\  \\Aditya Rikhari\\Aditya Rikhari - AANA NAHI (original).mp4";
            axWindowsMediaPlayer2.URL = "D:\\  \\Aditya Rikhari\\Aditya Rikhari - Tinka (Official Music Video) ft. Mugdha Agarwal.mp4";



        }
    }
}

```


## Datagridview

```js
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace DataGridView
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            DataTable table_person = new DataTable();

            //table.Columns.Add(
            //    new DataColumn( CompanyName, typeof(string ) ) );

            table_person.Columns.Add("Rno");
            table_person.Columns.Add("Name");
            table_person.Columns.Add("Address");

            table_person.Rows.Add(101, "Sagar", "KK");
            table_person.Rows.Add(101, "Qadeer", "KK");
            table_person.Rows.Add(101, "Deepak", "KK");

            DataTable  table_color = new DataTable();
            
            table_color.Columns.Add("Color");
            table_color.Columns.Add("des");
            table_color.Rows.Add("Red", "good");
            table_color.Rows.Add("Green", "Exe");






            // dataGridView1.DataSource = table_person;
            DataSet set = new DataSet();
            set.Tables.Add(table_color);
            set.Tables.Add(table_person);


            //dataGridView1.DataSource = set.Tables[0];
            dataGridView1.DataSource = table_person;





        }
    }
}

```



```js
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace PageDynamicLocation
{
    public partial class Form1 : Form
    {
        private int x = 50;
        private int y = 50;


        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

            WindowState = FormWindowState.Maximized;
            timer1.Interval = 10;
            timer1.Start();

            
            
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            


            x++;
            while(x < 500)
            {
                x++;
                pictureBox1.Location = new Point(x, y);
            }

            //BackColor = Color.Red;
            while (y < 500)
            {
                y++;
                pictureBox1.Location = new Point(x, y);
            }
            //BackColor = Color.AliceBlue;
            while (x > 0)
            {
                x--;
                pictureBox1.Location = new Point(x, y);
            }
            //BackColor = Color.Yellow;

            while (y > 0)
            {
                y--;
                pictureBox1.Location = new Point(x, y);
            }
            //BackColor = Color.Green;


            // after visiting all four sides, now place it to the center
            Thread.Sleep(1000);
            pictureBox1.Location = new Point(250, 250);
            Thread.Sleep(1000);

        }
    }
}

```





```js
using System;
using System.Data;
using System.Windows.Forms;
using MySql.Data.MySqlClient;

namespace DBConnection
{
    public partial class Form1 : Form
    {
        MySqlConnection conn = new MySqlConnection("server=localhost; user=root; password=; database=test");
        string query = "Select * from temp";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            lgv();
        }

        // Loader Method: Open, objects, fill & display, close
        public void lgv()
        {
            conn.Open();

            MySqlCommand cmd = new MySqlCommand(query, conn);
            MySqlDataAdapter adp = new MySqlDataAdapter(cmd);
            
            DataTable dt = new DataTable();
            adp.Fill(dt);
            
            dataGridView1.DataSource = dt;
            conn.Close();
        }


        // Insert Button Event Listener
        private void button1_Click(object sender, EventArgs e)
        {
            
            // OQC-ECL
            // 1. open
            conn.Open();
            
            // 2. query
            string insertQuery = "INSERT INTO temp (empid, ename, salary) VALUES (@empid, @ename, @salary)";
            
            // 3. cmd
            MySqlCommand cmd = new MySqlCommand(insertQuery, conn);
            cmd.Parameters.AddWithValue("@empid", Convert.ToInt32(empidTextBox.Text));
            cmd.Parameters.AddWithValue("@ename", enameTextBox.Text);
            cmd.Parameters.AddWithValue("@salary", Convert.ToDecimal(salaryTextBox.Text));
             
            // 4. ExecuteNonQuery
            int rowsAffected = cmd.ExecuteNonQuery();
            // Check if the insert was successful
            if (rowsAffected > 0)
                MessageBox.Show("Record inserted successfully.");
            else
                MessageBox.Show("Insert failed.");
                        
            // 5. close                        
            conn.Close();
            // 6. lgv
            lgv();
        }


        // Reset Button
        private void button4_Click(object sender, EventArgs e)
        {
            empidTextBox.Text = "";
            enameTextBox.Text = "";
            salaryTextBox.Text = "";
        }


        // Delete Button
        private void button3_Click(object sender, EventArgs e)
        {
            if (string.IsNullOrEmpty(empidTextBox.Text)) {
                MessageBox.Show("Please enter a valid empid.");
                    return;
            }
            
            // 1. open
            conn.Open();
            // 2. query
            string deleteQuery = "DELETE FROM temp WHERE empid = @empid";
            
            // 3. cmd
            MySqlCommand cmd = new MySqlCommand(deleteQuery, conn);
            cmd.Parameters.AddWithValue("@empid", Convert.ToInt32(empidTextBox.Text));
            
            // 4. NonExecuteQuery
            if (cmd.ExecuteNonQuery() > 0)
                MessageBox.Show("Record deleted successfully.");
            else
                MessageBox.Show("No record found with the given empid.");
            
            // 5. close
            conn.Close();

            // 6. lgv
            lgv();
        }

        // Update Button
        private void button2_Click(object sender, EventArgs e)
        {
            if (string.IsNullOrEmpty(empidTextBox.Text)) {
                 MessageBox.Show("Please enter a valid empid.");
                    return;
            }
            // 1. open
            conn.Open();
            // 2. query
            string updateQuery = "UPDATE temp SET ename = @ename, salary = @salary WHERE empid = @empid";

            // 3. cmd
            MySqlCommand cmd = new MySqlCommand(updateQuery, conn);
            cmd.Parameters.AddWithValue("@empid", Convert.ToInt32(empidTextBox.Text));
            cmd.Parameters.AddWithValue("@ename", enameTextBox.Text);
            cmd.Parameters.AddWithValue("@salary", Convert.ToDecimal(salaryTextBox.Text));
            
            // 4. NonExecuteQuery
            int rowsAffected = cmd.ExecuteNonQuery();

            if (rowsAffected > 0)
                MessageBox.Show("Record updated successfully.");
            else
                MessageBox.Show("No record found with the given empid.");
            
            // 5. Close
            conn.Close();
            // 6. lgv
            lgv();
        }
    }
}

```












# VB Book

Text Property: &OK, E&xit

Although .NET originally targetted and still targets only the windows platform, you are seeing development communities using open-source projects to convert .NET to run on other platforms such as Linux and Unix. This means that a program written by a .NET developer on windows could run unchanged on Linux. In fact, the Mono Project (www.mono-project.com) has already released several version of its product. This project has developed an open-source version of a C# and VB.NET compiler, a runtime for the Common Language Infrastrucutre(CLI, also known as the Commong Intermediate Language, CIL), a subset of the .NET classes, and other .NET goodies independent of Microsoft's involvment. 


DAO:  Data Active Object
COM: Component Object Model
ADO: ActiveX Data Objects


# Visual Programming Language

## Theory
- **Desktop Application + Console Programming**
- **Event Driven Programming**
- **Use of Visual Programming (VP)**

## History
- **Structured Programming**
- **Use of .NET Framework**
  - CLR (Common Language Runtime)
  - CIL (Common Intermediate Language)
- **Architecture of .NET**
- **Regular vs Visual Programming Language**
- **Java vs C#**
- **Object-Oriented Programming Language**
  - **Four Principles**:
    - Encapsulation
    - Abstraction
    - Inheritance
    - Polymorphism

## Practical
- **Sorting Programs**:
  - Bubble Sort
  - Selection Sort
- **Control Statements**:
  - Loops: `for`, `while`, `do while`
  - Conditional Statements: `if`, `if else`, `else`
  - `Switch`
- **Random Color Changing**
- **Picture Handling**:
  - Set a picture using `PictureBox`
  - `Hide()`
  - `Show()`
  - `Timer`
  - Picture changes on click
  - Picture change with timer
- **User Interface Elements**:
  - Use of Radio Button, Checkbox, ListBox
  - FontDialog
  - OpenFileDialog
    - Filter
  - ProgressBar
  - BackgroundWorker:
    - `DoWork`
    - `ProgressChanged`
    - `RunWorkerCompleted`
  - DataTable, DataSet
  - Windows Media Player
  - Panel
  - ToolTip
  - GridView



## Mid
1. Control Structure, OOP, Selection sort in console (7 Marks)
2. .NET Architecture, previous and Next button code on label (7 Marks)
3. Timer importance, its applications, automated picture code (8 Marks)
4. Definitions (8 Marks)
    - Radio and Checkbox
    - List and RichTextBox
    - Sync and Async
    - Label and TextBox