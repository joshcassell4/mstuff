import numpy as np
from flask import Flask

def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))
 
def f1(x,y):
    return np.add(x,y)

def f2(x,y):
    return np.subtract(x,y)

def f3(x,y):
