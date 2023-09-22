# Machine Learning (CS-433)

This file contains the notes I took during the 2023 ML [(CS-433)](https://www.epfl.ch/labs/mlo/machine-learning-cs-433/) course. The notes are ordered by topics, rather then by courses, and they contain the most relevant informations in my opinion (Not detailed).

**NOTE:** The notes are meant to contain all the information presented during the courses.

### Class Structure:
* **Lecture** Tuesday 16:15 - 18:00 [(RLC E1 240)](http://plan.epfl.ch/?lang=fr&room=RLC%20E1%20240) 
* **Lecture** Wednesday 10:15 - 12:00 [(RLC E1 240)](http://plan.epfl.ch/?lang=fr&room=RLC%20E1%20240)
* **Exercises** Thursday 14:15 - 16:00 [(INJ218)](http://plan.epfl.ch/?lang=en&room=INJ218) 
* Number of Credits: **8**

### Evaluation:
* Project 1 | 10% | Groups of 3 | Due **30.08.2023**
* Project 2 | 30% | Groups of 3 | Due **21.12.2023**
    * [Projects with labs](https://www.epfl.ch/labs/mlo/ml4science/)
* Final Exam | 60% | Theoretical | **TBD**

## Content

### Regression

Input -> Output (**Predict** Output | **Interpret** effects of input over the output)  
$(x_{n}, y_{n})$ -> input, output pair  
$N$ -> **Data Size** (Number of samples)  
$D$ -> **Dimensionality** (Dimension of a sample)  
Correlation $\ne$ Causation

### Linear Regression

Finding the linear function that approximates the output  
$y_n \approx f(x_{n}) \coloneqq w_{0} + w_{1}x_{n1}$  
Multivariate -> A bigger polynomial  
$f(x_{n}) = \tilde{x} \_{n}^\top \tilde{W}$ , where $\tilde{x} \_{n}$ means adding the bias term as a 1 to the $x_{n}$ array (It now has $D+1$ dimension).  
The goal is to learn the $\tilde{W}$ array.

### Overparametrization - D > N

The tasks becomes **undetermined** -> Multiple possible solutions.  
Quite common in deep learning.  
Regularization is a solution.  

### Loss Functions

* Used to learn parameters 
* Evaluates the model on given samples
* Desired Properties:
    * Symetric around 0
    * Large and Very Large mistakes should be penalized the same
* Robust Statistics -> Statistics good for a wide range of distributions
* Mean Square Error (MSE)
    * $\frac 1 N \displaystyle\sum_{n=1}^{N} [y_{n} - f_{w}(x_{n})]^2$
    * Sensible to outliers
* Mean Absolute Error (MAE)
    * $\frac 1 N \displaystyle\sum_{n=1}^{N} |y_{n} - f_{w}(x_{n})|$
    * Better with outliers
* Huber Loss
    * $`\text{Huber}(e) = \begin{cases} \frac 1 2 e^2 &\text{, if } \|e\| \le \delta \\ \delta \|e\| - \frac 1 2 \delta ^2 &\text{, if } \|e\| > \delta\end{cases}`$
    * convex, differentiable, robust to outliers
* Tukey's bisquare Loss
    * $`\frac {\delta L} {\delta e} = \begin{cases} e \lbrace 1 - \frac {e^2} {\delta ^ 2} \rbrace \text{, if } |e| \le \delta \\ 0 \text{, if } |e| > \delta \end{cases}`$
    * Non convex, but robust

### Convexity

* Shape of U
* $`h(\lambda u + (1 - \lambda)v) \le \lambda h(u) + (1 - \lambda)h(v); \forall u, v \in R^D; 0 \le \lambda \le 1`$ 
* Strictly Convex -> Strict inequality
* Any local minimum is global minimum

## Usefull Links
* [Discussion Forum](https://edstem.org/eu/courses/797/discussion/)
* [Videos of the Lectures](https://mediaspace.epfl.ch/channel/CS-433+Machine+learning/55647)
* [Course github](https://github.com/epfml/ML_course)
