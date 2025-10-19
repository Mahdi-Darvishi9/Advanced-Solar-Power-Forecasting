from dataclasses import dataclass
from typing import Tuple
import numpy as np
from sklearn.base import RegressorMixin, BaseEstimator, clone
from sklearn.linear_model import LinearRegression

@dataclass
class StackedEnsemble(RegressorMixin):
    base_models: Tuple[BaseEstimator, BaseEstimator]
    meta_model: BaseEstimator = LinearRegression()

    def fit(self, X, y):
        m1, m2 = self.base_models
        self.m1_ = clone(m1).fit(X, y)
        self.m2_ = clone(m2).fit(X, y)
        meta_X = np.c_[self.m1_.predict(X), self.m2_.predict(X)]
        self.meta_model_ = clone(self.meta_model).fit(meta_X, y)
        return self

    def predict(self, X):
        meta_X = np.c_[self.m1_.predict(X), self.m2_.predict(X)]
        return self.meta_model_.predict(meta_X)
