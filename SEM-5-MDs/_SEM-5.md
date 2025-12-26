# Semester 5 Study Guide

## Table of Contents

1. [Statistics](#statistics)
    - [Statistics 3 Chapter](#statistics-3-chapter)
    - [Probability](#probability)
    - [Descriptive VS Inferential](#descriptive-vs-inferential)
    - [Nature of Variables and Data](#nature-of-variables-and-data)
    - [Central Values, Partition Values, Dispersion](#central-values-partition-values-dispersion)
    - [Coefficient of Variation and Skewness](#coefficient-of-variation-and-skewness)
    - [Kurtosis and Moments](#kurtosis-and-moments)
2. [Differential Equations](#differential-equations)
    - [Introduction to Differential Equations](#introduction-to-differential-equations)
    - [Types of Differential Equations](#types-of-differential-equations)
    - [Applications](#applications)
3. [Networking](#networking)
    - [Network Core](#network-core)
    - [Data Communication](#data-communication)
    - [Network Protocols](#network-protocols)
    - [Packet Tracer](#packet-tracer)
    - [Network Classifications and Topologies](#network-classifications-and-topologies)
    - [Router Configuration and Transmission Media](#router-configuration-and-transmission-media)
4. [Visual Programming](#visual-programming)
    - [Console Programming and .NET Framework](#console-programming-and-net-framework)
    - [OOP and Control Structures](#oop-and-control-structures)
    - [GUI Elements and Exercises](#gui-elements-and-exercises)
5. [Web](#web)
    - [Software vs Website and Web Applications](#software-vs-website-and-web-applications)
    - [Architecture](#architecture)
    - [Scripting Languages](#scripting-languages)
    - [XAMPP Setup and DOM Tasks](#xampp-setup-and-dom-tasks)
6. [Tech Entrepreneurship](#tech-entrepreneurship)
    - [Chapter 1 Completed](#chapter-1-completed)
    - [Elevator Pitching](#elevator-pitching)

---

## Statistics

### Statistics 3 Chapter
1. Introduction
2. Drawing the Data
3. Central Tendency

### Probability

1. Introduction
2. Sampling & Sampling Distribution
3. Discrete Random Variable
   - Bernoulli R.V
   - Binomial R.V
   - Poisson R.V
   - Hypergeometric R.V
4. Continuous Random Variable
   - Uniform C.R.V
   - Exponential C.R.V
   - Normal C.R.V
5. Time Series Analysis
6. ANOVA Testing (Analysis of Variance)

### Descriptive VS Inferential
1. Nature of Variable, Collection, Variable, Nature of Observations
2. Scaling of Data: Nominal, Ordinal, Interval, Ratio
3. Variables: Quantitative, Qualitative


### Central Values, Partition Values, Dispersion
1. Central Values
   - Average Values
     - Arithmetic Mean (Ungrouped, Discrete, Grouped)
     - Geometric Mean, Properties of Geometric Mean
     - Harmonic Mean, Properties of Harmonic Mean
       - Relationship Among Arithmetic Mean, Harmonic Mean, & Geometric Mean
   - Position Values
     - Median
     - Mode (Individual, Discrete, Continuous)
   - Miscellaneous
     - Relation Between Mean and Median
     - Properties of Mean
     - Combined Mean
     - Changes in Origin (+, -) & Scale (*, /)

## 2. Partition Values
   - Quartiles
     - 4-Parts, Q1, Q2, Q3, k=1,2,3
   - Deciles
     - 10-Parts, D1, D2, ..., D9, D=1,2,...,9
   - Percentiles
     - 99-Parts, P1, P2, ..., P99, P=1,2,...,99

## 3. Dispersion
   - Range
   - Variance
   - Standard Deviation
   - IQR
   - Coefficient of Variation

## 4. Coefficient of Variation and Skewness
   - Distribution Curves: Symmetric, Asymmetric, Skewness (Skew > 0: Mode < Median < Mean, vice versa)
   - Coefficient of Skewness: -1 to 1
     - Karl Pearson's Coefficient of Skewness (Based on averages)
     - Bowley's Coefficient of Skewness (Based on Quartiles)

## 5. Kurtosis
   - Peakness and Flatness of Data
     - Platy-Kurtic, Meso-Kurtic, Lepto-Kurtic

## 6. Moments About Mean
   - M1, M2, M3, M4

## 7. Coefficient of Kurtosis

### After MID

## 8. Sample and Sampling Distribution
- ✅ **Population vs. Sample** 
- ✅ **Parameter vs. Statistics** 
- ✅ **Types of Sampling:** 
  - ✅ Probability Sampling: `SSCS`
  - ✅ Non-Probability Sampling: `SQJC`
- ✅ **Sampling Distribution:** 
  - ✅ With replacement 
  - ✅ Without replacement
- **Key Theorems and Tests:** 
  - Central Limit Theorem
  - Z-score test
  - ✅ Standard Error


## 9. Population Proportion

- ✅ **Probability Distribution for Population Proportion** 
- ✅ **Sample Distribution of Sample Proportion** 

## 10. Random Variable

### 10.1 Discrete Random Variables

- ✅ **Probability Mass Function (PMF)** - Piecewise Example 
- ✅ **Mean and Variance** 

### 10.2 Continuous Random Variables

- ✅ **Probability Density Function (PDF)** - Integration Example 
- ✅ **Mean and Variance** 

## 11. Distributions

## Sampling
1. ✅ Probability Sampling
2. ✅ Non Probability Sampling


### 11.1 Discrete Distributions

- ✅ **Bernoulli Distribution** 
- ✅ **Binomial Distribution** 
  - Expectation and Variance
- **Hypergeometric Distribution**
- ✅ **Poisson Distribution** 
  - ⚠️ Relationship between Poisson and Binomial: 
    - P is small ⬇️ and sample size is very large ⬆️ then binomial approximation for poisson


### 11.2 Continuous Random Variables (C.R.V)

- ✅ **Uniform Continuous Random Variable (C.R.V)**
- ✅ **Normal Continuous Random Variable (C.R.V)**
  - Standardized Normal Distribution
  - When sample size (n) isn’t given vs. when n is given
- ✅ **Exponential Continuous Random Variable (C.R.V)**

- `Mean and Variance of Distribtions: CRV + DRV`

## 12. Correlation and Linear Regression

- **Calculation of Correlation**
- **Covariance**
- **Simple Linear Regression**
- **Multiple Linear Regression**




## 13. T-test (Student's T-test)

- **Parameters**: t, z
- **Single Mean**
- **Two Means**: `Independent`, `Dependent`
- **More than Two Means**: `ANOVA` i.e., `One Way Anova`


- **Population Mean**: T-test
  - **One Population**: One Tailed + Two Tailed
  - **Two Independent Populations**: One Tailed + Two Tailed

- **Constructing Hypotheses**
- **Defining Significance Level**
- **Calculating Statistics: t-calculated, f-calculated, etc**
- **Critical Value of t**:
  - One Sample: Degrees of freedom (d.f) = n - 1
  - Two Sample: Degrees of freedom (d.f) = $n_1 + n_2 - 2$
- **Comparison**: calculated vs. critical



## 14. F-Test

- **Population Variance**:
  - F-test: Two Sample Variance Based Test
    - One Tailed
    - Two Tailed
    - ANOVA: One Way Anova





## 15. Non-Parameter Tests

- **Kruskal-Wallis Signed Rank Test**


## 16. Coefficient of Determination (R-squared)

- Formula: `1 - (SSE / SST)`

---


## Differential Equations

### Introduction to Differential Equations
1. ✅ DE, ODE, PDE, Order, Degree 
  - Note: Order and degree (if defined) of a differential equation are always positive integers.
2. ✅ Solution of DE: General, Particular, Singular
3. ✅ Assignment: Partial Fraction
    - Linear, Repeated Linear, Quadratic, Quadratic Repeated (Reducible | irreducible)
    - $\frac{7}{(x+1)(x^{2}+2)^{2}}$
4. ✅ Reducible to variable seperable
5. ✅ Reducible to Homogeneous 
6. ✅ Linear + its DPT properties
7. ✅ Bernoulli
8. ✅ Exact + Non Exact(4 Cases)
9. Higher Order
  - ✅ Traditional Method (4 Types of C.F | 6 Types of P.I)
  - ✅ Cauchy Euler
    - Linear differential equation with variable coefficient. Substitution: $let\space x = e^{z}, then \space logx=z$ 
  - ✅ Undertermined Coefficient method for $P.I$
    - This method is used for finding P.I of Linear D.E with constant coefficient. This method is not applicable for equations of form $ln(x), \space \space \frac{1}{x}, \space\space tan(x), \space\space sin^{-1}x$
    - This method is applicable for the non-homogeneous terms of polynomial, sin/cos, exponential, or their combination only.
  - ❌ Variation of Parameters
10. Applications: 
  - ✅ Growth and Decay
  - ✅ Linear(interest)
  - ✅ Newton's Two Laws
11. Laplace + Properties
  - ✅ Shifting Property
  - ✅ Multiplication by $e^{t}$
  - ✅ Multiplication by $t$
  - ✅ Division by $t$
  - ✅ Derivative Property
  - ✅ Integral Property
12. ✅ Inverse Laplace
  - ✅ Gamma Function
  - ✅ Convolution Theorem ✨
13. ✅ System of Linear D.Es ✨
14. Numerical Methods: 
  - ✅ Picard's
  - ✅ Taylor Series
  - ✅ Euler method + (graph ⚠️)
  - ✅ Euler Modified
  - ✅ Range Kutta ✨
    - ⚠️ Error Calculation ✨ 
15. Higher Order Applications
  - ✅ Circuit
  - ✅ Robotic Arm ✨



REVISION:
  - Partial Fraction
  - Convolution Theorem
  - System of D.E
  - Undetermined Coefficient method

SIR EXAM:
  - 1st Order: Linear Application, and 2-Questions 
  - 2nd Order: Higher Order: Traditional, Laplace(Basic, System) | 2 Applications
  - Numerical: RK




### Types of Differential Equations
1. Variable Separable
2. Reducible to Variable Separable (Implicit)
3. Homogeneous Differential Equations (All terms having same degree)
4. Reducible to Homogeneous
5. Linear Differential Equation
6. Reducible to Linear DE
7. Bernoulli's DE, Conditions of Identification, Quick Sort Analysis
8. Exact DE and its 4 Rules
9. Higher Order DE(4 Cases of C.F, 6 Cases of P.I)
10. Cauchy Euler(D.E with Variable Coefficient)
11. Undetermined Coefficient Method
12. Variation of Parameters

### Applications
1. Growth
2. Investment
3. Radioactive Material
4. Circuit Analysis

---

## Networking

### Network Core
1. Networking Devices, Transmission Media(Guided, Unguided)
2. IP Version(IPV4, IPV6) + Classes(A,B,C,D,E)
3. Domains, Addresses(Physical, Logical)
4. Network Engineer, Network Definition

### Data Communication
1. Transmission Mode: Simplex, Half/Full Duplex, Half Duplex: HUB
2. Sync vs Async
3. Collision Port in Hub
4. Electromagnetic Waves (Analog, Digital)
5. Signal Spectrum: Radio Waves, Micro Waves, Infrared, Gamma, Beta, X-Rays

### Network Protocols
1. Definition
2. OSI Model
3. Examples: TCP/IP, HTTP, FTP, ICMP, POP3
4. Layer 1 (Physical, HUB, Wires, Ports)
5. Layer 2 (Switch), ARP, RARP
6. Layer 3 (Router)
7. Network Connectivity Device



### Network Classifications and Topologies
1. Functionality, Area
2. CSMA/CD, CSMA/CA
3. IP Addresses (Works on Layer 3)
4. Classes, Broadband vs Baseband, Subnet Mask

### Router Configuration and Transmission Media
1. Router Configuration Commands
2. DCE vs DTE
3. Router RIP
4. Transmission Media: Guided, Unguided
5. Cables, Connectors (BNC, RJ45)

### Transmission Media
1. Guided VS Unguided | Ground Line vs Satelite Link
2. Cables: Coaxial, Twisted Pair (cat5, cat6, cat7), Untwisted, Fiber optic, 

### Packet Tracer || Final Exam Tasks
1. Two Ways to Assign IP: Static (Customized) + Dynamic (DHCP)
2. Switches(1,2,3), InterNetwork Connectivity: Router(1,2,3), 
3. VLAN (Single Switch)
4. InterVLAN (Multiple Switches + Router)
5. InterVLAN VTP

Modulation + DeModulation 
Multiplexer
ip exercises















### MISC
1. Broadband: Many signals at a time
2. Baseband: only one signal at a time 
3. Router on Stick Methodology
4. Error checking algorithms, (Transport Layer, checksum, end-to-end), and point-to-point
5. Impairment causes in network: Attention, distortion, Noise
6. Types of Noise: Thermal, Induce, Cross Talk, Impulse
7. Switch Port Mode: Access, Trunk; It is router on stick methodology.
8. Routing: Dynamic, Distance Vector, Link State(Short Distance, less traffic, open shortest path first(OSPF), dijsktra algorithm)
9. Border Gateway Protocol()
10. STP: Spanning Tree Protocol: Root, Bridge, Block
11. VTP: VLAN Trunking Protocol

---




  
  




---
## Visual Programming

### Console Programming and .NET Framework
1. .NET Framework
2. CLR (Common Language Runtime)
3. C# + .NET Architecture

### OOP and Control Structures
1. Namespace, Partial Class
2. Variables, Arrays, Objects, Methods, Functions, Event Listeners
3. Bubble Sort, Selection Sort
4. .NET Architecture Diagram
5. Control Structures: Repetition + Selection
6. Creation + Execution of Project

### GUI Elements and Exercises
1. Previous + Next, Timer (Time Watch, Increment, Auto Pic Changer)
2. Text Box vs Rich Text Box
3. Bio Data, Calculator, Sorting
4. List Box, Check Box, Radio Button


## October 02, 2024 VP
1. Datagridview
2. Dataset can have multiple tables


## VP MISC
1. BackColor = Color.Red;
2. WindowState = FormWindowState.Maximized;
3. lable1.Font = new Font("Arial", 12, FontStyle.Bold);
4.  private void button1_Click(object sender, EventArgs e)
  `{
      button1.Text = "Submit";
      Close();
  }`
5. 


## Final Exam Tasks
1. Namespace, Partial Class
2. Variables, Arrays, Objects, Methods, Functions, Event Listeners
3. Bubble Sort, Selection Sort
4. .NET Architecture Diagram
5. Control Structures: Repetition + Selection
6. Creation + Execution of Project

1. Previous + Next, Timer (Time Watch, Increment, Auto Pic Changer)
2. Text Box vs Rich Text Box
3. Bio Data, Calculator, Sorting(selection, bubble)
4. GroupBox(List Box, Check Box, Radio Button)
5. ❌ Background Worker, DateTime Picker,  ColorDialog,FontDialog, FileDialog(Manual Object Creation, filter),
6. Color Changer, StripMenu, 


1. Datagridview
2. Dataset can have multiple tables
3. Data Base: Insert, Update, Delete


---
- dateTimePicker1.Text, fontDialog.Font, colorDialog1.Color;
- fileDialog.filter = "ChooseImage(*.png;*.jpg;*.GIF)|*.png;*.jpg;*.GIF";
- DoWork: Loop, Thread.Sleep, backgroundWorker1.ReportProgress(0)
- ProgressChanged: progressBar.value +=1
- RunWorkerCompleted: MessageBox.Show('Task Completed');
- LoadFileButton_Click: backgroundWorker1.WorkerReportProgress = true; backgroundWorker1.RunWorkerAsync();
- OQC-ECL: Open, query, cmd, ExecuteNonQuery(), close, lgv
- lgv: open, objects, fill & display, close



## Web

### Software vs Website and Web Applications
1. Types of Web Applications
2. What is Engineering 
3. Regression Testing
4. Web Centric, Client (Browser)

### Architecture
1. 1-Tier, 2-Tier, 3-Tier
2. Explain Web Architecture (3-Tier)

### Scripting Languages
1. Client-Side, Server-Side

### XAMPP Setup and DOM Tasks
1. XAMPP Setup
2. Syncing VS Code
3. Hypertext, Hyperlinks
4. DOM, JS Tasks


### Web-Practical
1. Document Object Model (DOM)

- The Document Object Model (DOM) is a way for scripts or programming languages to interact with web pages. It shows how a document, like an HTML page, is structured in memory.

- The DOM represents this structure as a tree. Each part of the tree is called a **node**, and nodes can hold objects. Using DOM methods, you can change the document's layout, style, or content.

- Nodes can also have **event handlers**, which are functions that run when certain actions (events) happen on the page.

`DOM --> Nodes --> Events`

## Web JS Programs
1. Image tag, Anchor ta
2. CSS: inline, internal, external
3. Div and Span
4. Table of Mid using Div and table
5. Timer: Image changer, Stop Watch
6. AJAX: Php load file  ✨
7. Lambda function
8. Lists HTML
9. DB connection, INSERT, UPDATE, DELETE ✨
10. CMS, Dom Theory
11. Differences: XMLHTTPRequest vs. onreadystatechange








## Tech Entrepreneurship

### Chapter 1 Completed
1. Summary of Key Points

### Elevator Pitching
1. Techniques and Best Practices



