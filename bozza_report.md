# TRACCIA
In the course, you have studied empirical risk minimization and basic predictors such as linear models and trees. These methods rely on choosing a single model from a hypothesis class, possibly with regularization. However, a different approach is to combine many simple models into a stronger one.

Boosting is a method that builds a strong classifier by iteratively combining weak learners, typically simple models that perform only slightly better than random guessing. At each step, the algorithm focuses on the examples that are hardest to classify, gradually improving performance. This process can be interpreted both as an optimization procedure and as a way of constructing additive models.

This assignment explores boosting from both perspectives. You will implement and analyze AdaBoost, and study how combining weak learners affects training error, test error, and robustness. This connects to the course material on loss minimization and extends it to iterative, adaptive model construction.

Objective
Understand how boosting combines weak learners
Study the relationship between training error and generalization
Required datasets
Real-world classification dataset
Synthetic classification dataset
Tasks
Implement or use AdaBoost with:
Decision stumps as weak learners
Track over iterations:
Training error
Test error
Analyze:
Evolution of sample weights
Contribution of weak learners
Compare with:
Single decision tree
Logistic regression
Expected Output
Training error decreasing over iterations
Non-trivial behavior of test error
Insight into how boosting focuses on hard examples
Extension



Study overfitting as number of rounds increases


# TITOLO

### Abstract


## Introduction

### From basic predictors to boosting

### Goals of this work
Recall that the objectives are:
- Understand how boosting combines weak learners
- Study the relationship between training error and generalization


## Theoretical Background

### ERM, linear predictors and trees

### Boosting and ensemble methods

### AdaBoost

## Methodology



## Implementation and Experimental Setup


## Analysis of the results
This expected output have to be putted somewhere inside these subchapters:
- Training error decreasing over iterations
- Non-trivial behavior of test error
- Insight into how boosting focuses on hard examples


### Training and test error over iterations

### Evolution of sample weights


### Contribution of weak learners


### AdaBoost vs single decision tree and logistic regression


### Optional: analysis of overfitting over rounds



