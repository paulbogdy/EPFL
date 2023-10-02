# Mathematics of Data (EE-556)

This file contains the notes I took during the 2023 Mathematics of Data [(EE-556)](https://edu.epfl.ch/coursebook/en/mathematics-of-data-from-theory-to-computation-EE-556). The notes are ordered by topics, rather then by courses, and they contain the most relevant informations in my opinion (Not detailed).

**NOTE:** The notes are meant to contain all the information presented during the courses.

### Class Structure:
* **Lecture** Monday 9:15 - 12:00 [(MA B1 11)]
* **Exercises** Friday 16:15 - 19:00 TBD 
* Number of Credits: **6**
* First 3 weeks we'll do 2 hours lectures instead of the exercises (check outlook)
* Contains suplimentary material (You're expected to know this)

## Content

Extract information from data while understanding trade-offs.

### ML Paradigms:
* Supervised Learning - predict having examples
    * Generator (The data in nature)
    * Supervisor (Gives a interpretable value to the data)
    * Learning Machine (Learns to do what the supervisor does)
* Unsupervised Learning - predict without examples
* Reinforcement Learning - agent interacting with an environment

### Loss Function

* Checks how different the current function is from the ideal function (from a statistical standpoint).  
* Measures data fidelity.
* (a, b) Error should be positive and 0 only if the inputs are equal 
* (c) Symetric $`d(b_{1}, b_{2}) = d(b_{2}, b_{1})`$
* (d) Should satisfy the triangle inequality $`d(b_{1}, b_{2}) \le d(b_{1}, b_{3}) + d(b_{3}, b_{2})`$ 
    * metric -> a, b, c, d
    * pseudo-metric -> a, b, c
    * divergence -> a, b

* Logistic Loss (For Classification)
    * $`b_{1} \in R`$ and $`b_{2} \in \pm 1`$
    * $`L(b_{1}, b_{2}) = \log_{2} (1 + exp(-b_{1} \times b_{2}))`$ 
* $`l_{q}`$ loss
    * Basically distance with a certain power
    * $`L_{q}(b_{1}, b_{2}) = \lVert b_{1} - b_{2} \rVert _{q} ^q = \displaystyle\sum _{i=1} ^n | b_{1i} - b_{2i} | ^q`$ 
    * $`b_{2}`$ can be 0 => $` \lVert b \rVert _{q} ^q = \displaystyle\sum _{i=1} ^n | b_{i} | ^q`$
* Wasserstein Distance (First Lecture)
    * How hard it is to transform one distribution into another (Area between CDFs)
    * Sensitive to outliers

### Statistical Learning Model

* Consists of 3 parts:
    * Sample of random variables $`(a_{i}, b_{i}) \in A \times B`$ 
    * A class of functions $`h^\circ \in H^\circ`$ (The model)
    * The Loss function $`L: B \times B \rightarrow R`$
* Risk of $`h^\circ`$ => Expected value of $`(a, b)`$ random variables
* Minimize Risk Empirically:
    * We estimate the function class $H$ and we take the function with the smallest risk
* Parametric model -> can be represented by parameters

### Law of Large Numbers

* Basically the more samples you have the closer you are to the actual expected value
* $X$ random variable, The mean of samples converges to the expected value

### Central limit theorem

* The distribution of normalized sample tends to the normal distribution

### Estimator

* Gives a parameter (From a Parameter Space $X$) based on samples
* Least Squares:
    * $`L_{2}`$
* Maximum Likelihood:
    * $`-\log p_{x}(b)$ where $p_{x}`$ is the probability distribution function for the x (parameters of the function)
    * We try to maximize the probability of observing most of the samples
    * **IMPORTANT:** The ML Estimator converges to the optimal parameter from the Parameter Space
    * However it is not always the best 
* M-Estimator: $`x_{M}^\star \in \arg \min{F(x)}`$
    * Minimization type estimator (As minimization problems)
* Exam question: With a distribution and a linear function define the estimator

### Probability (Supplementary)

* Sample space $`\Omega`$
* Event -> subset of sample space $`E \subset \Omega`$
* Principle of inclusion-exclusion: $`P(A \cup B) = P(A) + P(B) - P(A \cap B)`$
* Marginal probability -> The probability of an event $`A`$ to occur $`P(A)`$
* Joint probability -> $`P(A, B)`$ both events occuring
* Conditional Probability ->  $`P(A|B)`$ probability of A happening if B happened
* Bayes rule -> $`P(A|B) = \frac {P(B|A)P(A)} {P(B)}`$
* Random variable -> function from value to outcome of the experiment
* Probability mass function (Pmf) -> $`P(X = x)`$ probability that the random variable has that value
* Probability density function (Pdf):
    * The integral over $`[a, b]`$ is the probability of x being in that interval
    * Basically Pmf for non-discrete functions
* $`p(x, y) = p(x|y)p(y)`$
* Expectation (Expected Value) $`\mathbb{E}[X]`$:
    * Discrete -> average of all probabilities multiplied by the value
    * Continous -> Integral of $`xp(x)`$
* Variance: $`\mathbb{V} = \sum {(x - \mathbb{E}[X])^2}P(X = x)`$
    * Integral if continous
* Covariance: $`\text{cov}[x, y] = \mathbb{E}[(x - \mathbb{E}[x])(y - \mathbb{E}[y])]`$
* Precision Matrix -> Inverse of Covariance matrix

### Complexity (Supplementary)

* $`\Omicron`$ -> Bigger than the actual function
* $`\Omega`$ -> Smaller than the actual function
* $`\Theta`$ -> Around that function

### Kernels (Supplementary)

* $`\phi: A \rightarrow H`$ text embedding
* $`K(a, b) = \langle \phi (a), \phi (b) \rangle`$ (Kernel), inner product of the embeddings
* Basically comperes the similarity between embeddings
* Hilbert Space
    * Linear Vector Space
    * Has an inner product operation
    * Has the distance $`|x - y| = \sqrt {\langle x - y, y - x\rangle}`$

### Regression

* Gaussian linear regression model: $b_{i} = `\langle a_{i}, x \rangle + w_{i}`$
* Logistic regression model
    * Come with a score -> assign a probability: $`\frac 1 {1 + \text{exp} (-s_{x}(a))}`$ where $`s_{x}`$ is the score
    * When the score function is linear, we have a linear classifier

### Linear Algebra

* Vector Norms:
* Quasy-Norms -> Does not satisfy triangle inequality
* Pseudo-Norms -> Does not satisfy definitiveness
* $`l_{0}`$ Norm -> Counts the number of non-zero elems
* Dual Norm:
    * $`\Vert x \Vert ^ \star = \text{sup}_{\Vert y \Vert \le 1} x^\top y`$
    * $`\Vert x \Vert ^ {\star \star} = \Vert x \Vert`$
* Matrix Norms (Same restrictions as Vector Norms)
* Matrix inner product: $`\langle A, B \rangle = \text{trace} (AB^\top) = \langle \text{vec}(A), \text{vec}(B) \rangle`$
* Schatten q-norms $`\Vert A \Vert _{q} = (\displaystyle \sum _{i=1} ^p (\sigma (A)_{i})^q)^{\frac 1 q}`$
* Every $`l_{q}`$ norms are convex
* Think of matrices in terms of eigenvalues
* Question on convergence rates in exam
* Reading convergence plots is in the exam

### Iterative Descent

* Solving optimization problems is impossible -> We need approximations
    * $`\epsilon`$ optimal if: $`f(x_{\epsilon} ^ \star) - f^\star \le \epsilon`$
    * $`\epsilon`$ optimal in sequence if: $`\Vert x_{\epsilon} ^ \star - x^\star \Vert \le \epsilon`$
* Finding Solutions:
    * Guess a solution -> refine it based on observation -> repeat
* Finding initial solution in the domain of the problem can be a problem in itself
* No tricks in exams !!!
* Gradient locally is the best direction, but is not the globally best direction
* Proximal point method -> Use the gradient of $`x^{k+1}`$
* The gradient has sort of a fog of war (Can only see slightly around)
* How to pick step size

## Usefull Links
* [Zoom for lectures and exercises](https://go.epfl.ch/mod-zoom) (Passcode: 994779)
* [Recorded Videos](https://mediaspace.epfl.ch/channel/EE-556%2BMathematics%2Bof%2Bdata%253A%2Bfrom%2Btheory%2Bto%2Bcomputation/30469)
* [Matrix Cookbook](https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf)
