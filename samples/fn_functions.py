#!/usr/bin/env python3
# The MIT License (MIT)
#
# Copyright (c) 2017 allancth
#
# Permission is hereby granted, free of charge, to any person obtaining a copy 
# of this software and associated documentation files (the "Software"), to deal 
# in the Software without restriction, including without limitation the rights 
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
# copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
# SOFTWARE.

from datetime import datetime

def add(a: int, b: int) -> int:
    return a + b

def multiply(a, b):
    return a * b

def subtract(a, b):
    return b - a

def divide(a, b):
    return a / b

def greet(name: str="World") -> str:
    print("Hello {0}!".format(name))

def fib(n: int=0) -> int:
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)

result = add(1, 2)
print(result)

greet("Alice")
greet()

for i in range(10):
    print(fib(i))

def get_date():
    return datetime.now().day, datetime.now().month, datetime.now().year

t = get_date()
print(t)
print("{0}-{1}-{2}".format(t[2], t[1], t[0]))

d, m, y = get_date()
print("{0}-{1}-{2}".format(y, m, d))

