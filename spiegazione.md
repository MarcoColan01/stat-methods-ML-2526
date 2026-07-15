# Steps to follow
1. Review carefully all the assignments and pick one.
2. Implement the required algorithms using Python and evaluate them as detailed in the assignment.
3. Write a thorough report (PDF document, up to 5-10 pages) explaining the methodologies and comparing the results against the expected output.
4. Publish the code and the report on a public GitHub (or GitLab) repository.
5. Submit the repository using this form.

# Evaluation: criteria and timeline
The evaluation of the project will mostly focus on the **correctness** and **completeness** of the **methodology** employed, rather than on the accuracy of the trained model(s) or training time. The **reproducibility** of the results and the **quality of the report** also play a substantial role in the final evaluation.
Within approximately 3 to 4 weeks after each deadline, the submissions will be reviewed and the students will be contacted to set the date of an oral examination, usually held online but possibly in person upon request, where the project will be thoroughly discussed with the TAs; students are required to prepare a brief presentation (~5/10 mins) of their work (without slides), they will be asked to motivate the choices made in the assignment and discuss the results.

**IMPORTANT**: You must read carefully the following declaration and include it in your report:
I declare that this material, which I now submit for assessment, is entirely my own work and has not been taken from the work of others, save and to the extent that such work has been cited and acknowledged within the text of my work. I understand that plagiarism, collusion, and copying are grave and serious offences in the university and accept the penalties that would be imposed should I engage in plagiarism, collusion or copying. This assignment, or any part of it, has not been previously submitted by me or any other person for assessment on this or any other course of study.

# Coding and report specifications
The preferred language is Python, any other choice must be agreed upon with the TAs. Jupyter notebooks are allowed. 

***VERY IMPORTANT: All the required algorithms, unless specified otherwise, must be implemented from scratch, external libraries like ```numpy``` and ```matplotlib``` may be used to only ease computation and plotting results.*** 

The submitted code should be reproducible and run in reasonable time (see the datasets section). The report must be written in LaTeX and the submitted repository must contain the final PDF. The report should describe the work done to complete the assignment, discussing in particular the choices made regarding the datasets, the implementation, and the visualizations. Furthermore, the report should provide a thorough analysis of the results, highlighting both the positive and the negative aspects. The report should be 5-10 pages long.

# Datasets
The assignments do not specify the exact dataset for the task, instead you are required to pick or generate datasets and motivate the associated choices in the report. **All the listed types of dataset must be included in the project, the report must include a comparison of the results across the datasets.**

For **real-world datasets**, standard sources such as the ```UCI Machine Learning Repository``` or ```sklearn.datasets``` are recommended. When selecting a dataset, make sure it is consistent with the task at hand, using classification datasets for classification problems and regression datasets for regression problems.

For **synthetic datasets**, you are free to design the data-generating process. A typical approach is to sample inputs from a chosen distribution (e.g., Gaussian or uniform distribution), possibly in multiple dimensions, and then define the labels as a deterministic function of the inputs. For instance, a linear function can be used to generate linearly separable data. Noise can be added to make the problem more realistic and to study robustness.

When applicable, datasets should be split into training and test sets and special care must be taken to ensure that no data leakage occurs. In these cases, the model must be trained exclusively on the training set and performance should be evaluated on the test set. If a different evaluation protocol is more appropriate for a specific assignment, it should be clearly justified.

The running time of the algorithms is not a primary concern for this project, avoid excessively large datasets and **prefer small- to medium-scale problems** that allow you to run multiple experiments efficiently.

# La mia scelta: Assignment 8 - Boosting and Additive Models
Nel corso avete studiato il concetto di Empirical Risk Minimization (ERM) e i predittori basici come i modelli lineari e gli alberi decisionali. Questi metodi si basano sulla scelta di un singolo modello da una classe di ipotesi, eventualmente con regolarizzazione. Tuttavia, un approccio diverso consiste nel combinare molti modelli semplici in uno più robusto.

Il boosting è un metodo che costruisce un classificatore robusto combinando iterativamente classificatori deboli, in genere modelli semplici che offrono prestazioni solo leggermente migliori rispetto ad una scelta casuale. Ad ogni passaggio, l'algoritmo si concentra sugli esempi più difficili da classificare, migliorando gradualmente le prestazioni. Questo processo può essere interpretato sia come una procedura di ottimizzazione e sia come un modo per costruire modelli additivi. 

Questo lavoro esplora il boosting da entrambe le prospettive. Implementerete e analizzerete AdaBoost e studierete come la combinazione di classificatori deboli influisce sultraining error, sul test error e sulla robustezza. Questo si collega al materiale del corso sulla minimizzazione della loss e lo estende alla costruzione iterativa e adattiva di modelli.

## Objective
- Understand how boosting combines weak learners
- Study the relationship between training error and generalization
## Required datasets
- Real-world classification dataset
- Synthetic classification dataset
## Tasks
- Implement or use AdaBoost with:
    - Decision stumps as weak learners
- Track over iterations:
    - Training error
    - Test error
- Analyze:
  - Evolution of sample weights
  - Contribution of weak learners
- Compare with:
    - Single decision tree
    - Logistic regression
- Expected Output
    - Training error decreasing over iterations
    - Non-trivial behavior of test error
    - Insight into how boosting focuses on hard examples





