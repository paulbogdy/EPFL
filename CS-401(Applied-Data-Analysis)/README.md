# Applied Data Analysis (CS-401)

This file contains the notes I took during the 2023 ADA [(CS-401)](https://dlab.epfl.ch/teaching/fall2023/cs401/) course. The notes are ordered by topics, rather then by courses, and they contain the most relevant informations in my opinion (Not detailed).

**NOTE:** The notes are meant to contain all the information presented during the courses.

### Class Structure:
* **Lecture** Wednesday 8:15 - 10:00 [(RLC E1 240)](http://plan.epfl.ch/?lang=fr&room=RLC%20E1%20240)
* **Exercises** Friday 13:15 - 15:00 [(CE1106)](https://plan.epfl.ch/?room==CE%201%20106) 
* Number of Credits: **8**

### Evaluation:
* Homeworks (2) | 30% | Group of 5
* Final Exam | 30% | Mini project done on campus
* Project | 25% | Group of 5
* Quizzes | 15% | Lowest 2 will be drop | 13:15-13:30 each Friday
* The grades will be normalized based on all the results

## Content

### Handling data

* It's important how you think about the world -> In order to be able to model it
* Imperative language -> Specify how to do it
* Declarative language -> Specify what you want to do (The framework figures out how)
* Flat model
    * One type of entity
    * Example: log files, csv files
* Relational model
    * Many entityes
    * Connected by relationships (Basically databases)
* Document model
    * Hirarchy
    * Example: XML, JSON
* Network model
* Most websites don't let you scrape data -> Preferably use API
* Data wrangling
    * Extract and standardize raw data
    * Clean anomalies
* Captcha was used as a solution to translate New York time

### Data Visualization

* There is a shift from static visualization to interactive
* PCA can be used to should multidimensional data
* Choose axes wisely (Linear vs Logarithmic)
* Power Law: Heavy-tailed data
    * Very large values are rare, but not very rare
    * Doesn't really make sense to work with means -> Use medians
* Complementary cumulative distribution function -> The probability of a poin being at least x
* Show data uncertainty
* Use colors wisely:
    * Sequential -> color from low to high
    * Diverging -> 2 seq colors
    * Categorical -> Different colors
* Use colorblind-safe palettes
* Don't zoom in on bar charts (People assume bottom is 0)


## Useful Links
* [Discussion Forum](https://edstem.org/eu/courses/808/discussion/)
* [Communication Guidelines](https://dlab.epfl.ch/teaching/fall2023/cs401/communication-guidelines/)
* [Github](https://github.com/epfl-ada/2023)
* [Recordings](https://mediaspace.epfl.ch/playlist/dedicated/29362/0_aw4n91mr/)