# A common interface shared by every model implemented in this project

from abc import ABC, abstractmethod
import numpy as np 

def check_X(X):
    X = np.asarray(X, dtype=float)
    if X.ndim != 2:
        raise ValueError(f"X must be 2D, got shape {X.shape}")
    return X 

def check_Xy(X, y):
    X = check_X(X)
    y = np.asarray(y).ravel()

    if y.shape[0] != X.shape[0]:
        raise ValueError(f"X has {X.shape[0]} rows but y has {y.shape[0]} entries")
    
    labels = set(np.unique(y).tolist())
    if not labels <= {-1,1}:
        raise ValueError(f"labels must be in {{-1, +1}}, found {sorted(labels)}")
    if len(labels) < 2:
        raise ValueError("y contains a single class; nothing to learn")
    
    return X, y.astype(int)

def check_sample_weight(sample_weight, n_samples):
    #Return a normalized weight vector, defaulting to the uniform one.
    if sample_weight is None:
        return np.full(n_samples, 1.0 / n_samples)
 
    w = np.asarray(sample_weight, dtype=float).ravel()
    if w.shape[0] != n_samples:
        raise ValueError(
            f"sample_weight has {w.shape[0]} entries, expected {n_samples}"
        )
    if np.any(w < 0):
        raise ValueError("sample_weight must be non-negative")
 
    total = w.sum()
    if total <= 0:
        raise ValueError("sample_weight sums to zero")
    return w / total


class Classifier(ABC):
 
    @abstractmethod
    def fit(self, X, y, sample_weight=None):
        """Fit the model and return self."""
 
    @abstractmethod
    def predict(self, X):
        """Return an array of predicted labels in {-1, +1}."""
 
    def error(self, X, y, sample_weight=None):
        """Zero-one error, weighted by sample_weight when provided.
 
        With uniform weights this is the plain misclassification rate; with the
        boosting distribution it is the weighted error epsilon_t.
        """
        X, y = check_Xy(X, y)
        mistakes = self.predict(X) != y
        if sample_weight is None:
            return float(np.mean(mistakes))
        w = check_sample_weight(sample_weight, y.shape[0])
        return float(np.sum(w[mistakes]))
 
    def accuracy(self, X, y):
        return 1.0 - self.error(X, y)

class IterativeClassifier(Classifier):
 
    @abstractmethod
    def staged_predict(self, X):
        """Yield predictions of the ensemble truncated at t = 1, 2, ..., T."""
 
    def staged_error(self, X, y):
        """Zero-one error of every prefix ensemble, as a 1-D array."""
        X, y = check_Xy(X, y)
        return np.array(
            [float(np.mean(pred != y)) for pred in self.staged_predict(X)]
        )