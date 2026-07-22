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
    """Return a normalized weight vector, defaulting to the uniform one."""
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