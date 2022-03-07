from abc import ABC
import numpy as np
import torch


class BaseSolver(ABC):

    @abstract_method
    def sample(problem, num_samples):
        pass
