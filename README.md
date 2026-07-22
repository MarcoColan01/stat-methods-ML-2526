# Boosting and Additive Models

Project for the *Statistical Methods for Machine Learning* course
(Università degli Studi di Milano) — Assignment 8: Boosting and Additive Methods. The author of this project is Marco Colangelo (ID  67045A).

AdaBoost with decision stumps, implemented from scratch and compared against a single decision tree and logistic regression, on one real-world and one synthetic binary classification dataset.

## Repository layout

```
src/          algorithm and utility modules 
notebooks/    notebooks that run the experiments using src/
datasets/     cached copies of the real and synthetic datasets
results/      raw metrics produced by the experiments
report/       LaTeX sources and the final PDF; report/figures/ holds the plots
```

## Setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Reproducibility

All seeds, split proportions and experiment constants are defined in `src/config.py`. 


