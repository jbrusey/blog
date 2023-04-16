import numpy as np
import pandas as pd

import timeit


def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

def binet(n):
    phi = (1+np.sqrt(5))/2
    psi = 1 - phi

    return (phi**n - psi**n) / (phi - psi)


