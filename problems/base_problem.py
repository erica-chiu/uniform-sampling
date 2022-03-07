import numpy as np
import torch
from abc import ABC


class BaseProblem(ABC):

    @abstractmethod
    def fn(x):
        pass

    def u_fn(x):
        pass

