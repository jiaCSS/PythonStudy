import tkinter
from tkinter import *

def add(*args):
    total = 0
    for n in args:
        total += n
    return total

print(add(2, 3, 4))

def calculate ( n,  **kwargs):
    print(kwargs)
    print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add =3, multiply = 5)
# kwargs return a dict while *args retuns tuples


