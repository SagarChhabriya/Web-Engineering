## Problem Statement

The population of a certain country has grown at a rate proportional to the number of people in the country. At present, the country has 80 million inhabitants. Ten years ago, it had 70 million. Assuming that this trend continues, find:

(a) An expression for the approximate number of people living in the country at time $ t $.

(b) The approximate number of people at the end of the next 10-year period.

---

## Solution

### (a) Expression for the Number of People Living in the Country at Time $ t $

The population follows an exponential growth model where the rate of growth is proportional to the current population. The formula for exponential growth is:

$$
P(t) = P_0 e^{kt}
$$

where:
- $ P_0 $ is the initial population at $ t = 0 $,
- $ k $ is the growth rate constant,
- $ t $ is the time in years,
- $ e $ is the base of the natural logarithm.

Given data:
- 10 years ago $ t = -10 $, the population was 70 million.
- At present $ t = 0 $, the population is 80 million.

1. **Find $ k $:**

   At $ t = -10 $:
   $$
   P(-10) = P_0 e^{-10k}
   $$
   Substituting $ P(-10) = 70 $ million:
   $$
   70 = 80 e^{-10k}
   $$

   Solve for $ e^{-10k} $:
   $$
   \frac{70}{80} = e^{-10k}
   $$
   $$
   \frac{7}{8} = e^{-10k}
   $$

   Take the natural logarithm of both sides:
   $$
   \ln\left(\frac{7}{8}\right) = -10k
   $$
   $$
   k = -\frac{\ln\left(\frac{7}{8}\right)}{10}
   $$

2. **Expression for $ P(t) $:**

   Substitute $ P_0 = 80 $ and $ k $:
   $$
   P(t) = 80 e^{kt}
   $$
   $$
   k = -\frac{\ln\left(\frac{7}{8}\right)}{10}
   $$

   Therefore:
   $$
   P(t) = 80 e^{-\frac{\ln\left(\frac{7}{8}\right)}{10} t}
   $$

### (b) Approximate Number of People at the End of the Next 10-Year Period

To find the population at $ t = 10 $ years from now, substitute $ t = 10 $ into the expression:

$$
P(10) = 80 e^{-\frac{\ln\left(\frac{7}{8}\right)}{10} \cdot 10}
$$

Simplify the exponent:
$$
P(10) = 80 e^{-\ln\left(\frac{7}{8}\right)}
$$
$$
e^{-\ln\left(\frac{7}{8}\right)} = \frac{1}{e^{\ln\left(\frac{7}{8}\right)}} = \frac{1}{\frac{7}{8}} = \frac{8}{7}
$$

Thus:
$$
P(10) = 80 \cdot \frac{8}{7}
$$
$$
P(10) = \frac{640}{7}
$$
$$
P(10) \approx 91.43 \text{ million}
$$

---

**Summary:**

(a) The expression for the population at time $ t $ is:
$$
P(t) = 80 e^{-\frac{\ln\left(\frac{7}{8}\right)}{10} t}
$$

(b) The approximate number of people at the end of the next 10-year period is:
$$
\approx 91.43 \text{ million}
$$



## Problem Statement

The rate of growth of the population in a small town is proportional to the present population. The population of the town was 1000 a year ago, and the present population is 2000. Assuming the rate of increase in population is proportional to the present population, find:

1. The differential equation describing the population growth.
2. The population after the end of the 4th year.

---

## Solution

### 1. Differential Equation

The rate of growth of the population $ P(t) $ is proportional to the current population:

$$
\frac{dP(t)}{dt} = kP(t)
$$

where:
- $ \frac{dP(t)}{dt} $ is the rate of change of the population,
- $ k $ is the proportionality constant (growth rate).

### 2. Solve the Differential Equation

The general solution to this differential equation is:

$$
P(t) = P_0 e^{kt}
$$

where:
- $ P_0 $ is the initial population at $ t = 0 $,
- $ k $ is the growth rate constant,
- $ t $ is the time in years.

#### Applying Initial Conditions

Given:
- The population 1 year ago $ t = -1 $ was 1000.
- The present population $ t = 0 $ is 2000.

Use these conditions to find $ k $:

1. **Find $ k $**:

   At  $ t = -1  $ 

   $$
   P(-1) = P_0 e^{-k}
   $$

   Given $$ P(-1) = 1000 $$ and $$ P_0 = 2000 $$

   $$
   1000 = 2000 e^{-k}
   $$

   Solve for $ e^{-k} $:

   $$
   \frac{1000}{2000} = e^{-k}
   $$

   $$
   \frac{1}{2} = e^{-k}
   $$

   Take the natural logarithm:

   $$
   -k = \ln\left(\frac{1}{2}\right) = -\ln(2)
   $$

   $$
   k = \ln(2)
   $$

2. **Write the Population Function**:

   Substitute $$ k = \ln(2) $$ and $$ P_0 = 2000 $$

   $$
   P(t) = 2000 e^{(\ln(2))t}
   $$

   Simplify using the property $$ e^{\ln(a)} = a $$

   $$
   P(t) = 2000 \cdot 2^t
   $$

#### Population After 4 Years

To find the population at $ t = 4 $ years:

$$
P(4) = 2000 \cdot 2^4
$$

$$
P(4) = 2000 \cdot 16
$$

$$
P(4) = 32,000
$$

---

**Summary:**

1. The differential equation describing the population growth is:

   $$
   \frac{dP(t)}{dt} = kP(t)
   $$

2. The population after the end of the 4th year is:

   $$
   P(4) = 32,000
   $$
---




<!-- ## Problem Statement

A family deposits money into a bank account continuously at a rate of $10,000 per year. The account earns interest at an annual rate of 4%. The family starts with an initial deposit of $23,000. Assuming they do not make any withdrawals, how much money will be in the account after 4 years?

---

## Solution

### General Solution

To solve this problem, we use the formula for continuous deposits with continuous compounding interest. The differential equation governing this situation is:

$$
\frac{dA(t)}{dt} = rA(t) + D
$$

where:
- $ A(t) $ is the amount in the account at time $ t $,
- $ r $ is the annual interest rate (4% or 0.04),
- $ D $ is the continuous deposit rate ($10,000 per year).

The general solution to this differential equation is:

$$
A(t) = A_0 e^{rt} + \frac{D}{r} \left( e^{rt} - 1 \right)
$$

where:
- $ A_0 $ is the initial deposit ($23,000),
- $ t $ is the time in years.

### Applying the Initial Conditions

1. **Initial Deposit $ A_0 $**:

   Substitute $ A_0 = 23,000 $, $ r = 0.04 $, and $ D = 10,000 $ into the formula:

   $$
   A(t) = 23{,}000 e^{0.04t} + \frac{10{,}000}{0.04} \left( e^{0.04t} - 1 \right)
   $$

2. **Calculate Amount After 4 Years**:

   Substitute $ t = 4 $ into the formula:

   $$
   A(4) = 23{,}000 e^{0.04 \cdot 4} + \frac{10{,}000}{0.04} \left( e^{0.04 \cdot 4} - 1 \right)
   $$

   Simplify:

   $$
   e^{0.16} \approx 1.174
   $$
   $$
   A(4) = 23{,}000 \cdot 1.174 + \frac{10{,}000}{0.04} \left( 1.174 - 1 \right)
   $$
   $$
   A(4) = 26{,}982 + 250{,}000 \cdot 0.174
   $$
   $$
   A(4) = 26{,}982 + 43{,}500
   $$
   $$
   A(4) = 70{,}482
   $$

Thus, the amount of money in the account after 4 years will be approximately:

$$
A(4) \approx 70{,}482
$$

---

**Summary:**

After 4 years, the amount in the account will be approximately $70,482. -->



## Problem Statement

A family deposits money into a bank account continuously at a rate of \$10,000 per year. The account earns interest at an annual rate of 4%. The family starts with an initial deposit of \$23,000. Assuming they do not make any withdrawals, how much money will be in the account after 4 years?

---

## Solution

### Differential Equation

Let $ A(t) $ represent the amount of money in the account at time $ t $. The rate of change of the account balance is given by:

$$
\frac{dA(t)}{dt} = rA(t) + D
$$

where:
- $ \frac{dA(t)}{dt} $ is the rate of change of the account balance,
- $ r $ is the annual interest rate (0.04),
- $ D $ is the continuous deposit rate (\$10,000 per year).

### General Solution to the Differential Equation

To solve the differential equation, we use the integrating factor method:

1. **Rewrite the Differential Equation:**

   $$ 
   \frac{dA(t)}{dt} - rA(t) = D 
   $$

2. **Find the Integrating Factor:**

   The integrating factor $ \mu(t) $ is:

   $$
   \mu(t) = e^{\int -r \, dt} = e^{-rt}
   $$

3. **Multiply Through by the Integrating Factor:**

   Multiply both sides by $ e^{-rt} $:

   $$
   e^{-rt} \frac{dA(t)}{dt} - r e^{-rt} A(t) = D e^{-rt}
   $$

   This simplifies to:

   $$
   \frac{d}{dt} \left( A(t) e^{-rt} \right) = D e^{-rt}
   $$

4. **Integrate Both Sides:**

   Integrate both sides with respect to $ t $:

   $$
   \int \frac{d}{dt} \left( A(t) e^{-rt} \right) \, dt = \int D e^{-rt} \, dt
   $$

   The left side integrates to:

   $$
   A(t) e^{-rt}
   $$

   The right side integrates to:  

   $$
   \int D e^{-rt} \, dt = -\frac{D}{r} e^{-rt}
   $$

   Thus:

   $$
   A(t) e^{-rt} = -\frac{D}{r} e^{-rt} + C
   $$

   where $ C $ is the constant of integration.

5. **Solve for $ A(t) $:**

   Multiply through by $ e^{rt} $:

   $$
   A(t) = -\frac{D}{r} + C e^{rt}
   $$

   The general solution is:

   $$
   A(t) = C e^{rt} - \frac{D}{r}
   $$

### Apply Initial Conditions

Given:
- Initial deposit $ A_0 = 23{,}000 $ at $ t = 0 $,
- Continuous deposit $ D = 10{,}000 $,
- Annual interest rate $ r = 0.04 $.

At $ t = 0 $:

$$
A(0) = C - \frac{D}{r}
$$

Substitute $ A_0 = 23{,}000 $:

$$
23{,}000 = C - \frac{10{,}000}{0.04}
$$

$$
23{,}000 = C - 250{,}000
$$

$$
C = 273{,}000
$$

### Specific Solution

Substitute $ C $ into the general solution:

$$
A(t) = 273{,}000 e^{0.04t} - 250{,}000
$$

### Amount After 4 Years

To find the amount after 4 years ($ t = 4 $):

$$
A(4) = 273{,}000 e^{0.16} - 250{,}000
$$

Using $ e^{0.16} \approx 1.174 $:

$$
A(4) = 273{,}000 \cdot 1.174 - 250{,}000
$$

$$
A(4) = 320{,}482 - 250{,}000
$$

$$
A(4) \approx 70{,}482
$$

---

**Summary:**

The amount in the account after 4 years is approximately:

$$
A(4) \approx 70{,}482
$$
