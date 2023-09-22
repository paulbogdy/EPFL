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
* (c) Symetric $d(b_{1}, b_{2}) = d(b_{2}, b_{1})$
* (d) Should satisfy the triangle inequality $d(b_{1}, b_{2}) \le d(b_{1}, b_{3}) + d(b_{3}, b_{2})$ 
    * metric -> a, b, c, d
    * pseudo-metric -> a, b, c
    * divergence -> a, b

* Logistic Loss (For Classification)
    * $b_{1} \in \R$ and $b_{2} \in \pm 1$
    * $L(b_{1}, b_{2}) = \log_{2} (1 + exp(-b_{1} \times b_{2}))$ 
* $l_{q}$ loss
    * Basically distance with a certain power
    * $L_{q}(b_{1}, b_{2}) = \lVert b_{1} - b_{2} \rVert _{q} ^q = \sum _{i=1} ^n | b_{1i} - b_{2i} | ^q$ 
    * $b_{2}$ can be 0 => $ \lVert b \rVert _{q} ^q = \sum _{i=1} ^n | b_{i} | ^q$
* Wasserstein Distance (First Lecture)
    * How hard it is to transform one distribution into another (Area between CDFs)
    * Sensitive to outliers

### Statistical Learning Model

* Consists of 3 parts:
    * Sample of random variables $(a_{i}, b_{i}) \in A \times B$ 
    * A class of functions $h^\circ \in H^\circ$ (The model)
    * The Loss function $L: B \times B \rightarrow \R$
* Risk of $h^\circ$ => Expected value of $(a, b)$ random variables
* Minimize Risk Empirically:
    * We estimate the function class $H$ and we take the function with the smallest risk

### Law of Large Numbers

* Basically the more samples you have the closer you are to the actual expected value
* $X$ random variable, The mean of samples converges to the expected value

### Estimator

* Gives a parameter (From a Parameter Space $X$) based on samples
* Least Squares:
    * $L_{2}$
* Maximum Likelihood:
    * $-\log p_{x}(b)$ where $p_{x}$ is the probability distribution function for the x (parameters of the function)
    * We try to maximize the probability of observing most of the samples
    * **IMPORTANT:** The ML Estimator converges to the optimal parameter from the Parameter Space
    * However it is not always the best 
* M-Estimator: $x_{M}^\star \in \arg \min{F(x)}$

TODO: Complete at Lecture 2

## Usefull Links
* [Zoom for lectures and exercises](https://go.epfl.ch/mod-zoom) (Passcode: 994779)
* [Recorded Videos](https://mediaspace.epfl.ch/channel/EE-556%2BMathematics%2Bof%2Bdata%253A%2Bfrom%2Btheory%2Bto%2Bcomputation/30469)