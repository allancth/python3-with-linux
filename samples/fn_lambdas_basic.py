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

def get_fn(a, b, op):
    if op == "+":
        return lambda: a + b
    elif op == "-":
        return lambda: a - b
    elif op == "*":
        return lambda: a * b
    elif op == "/":
        return lambda: a / b
    else:
        return None

r = get_fn(1, 2, "+")
print(r)
print(r())

def apply_fn(f):
    return f() + get_fn(5, 5, "+")()

r = apply_fn(r)
print(r)

r = apply_fn(lambda: 3 + 4)
print(r)

fn_factorial = lambda fn, n: n * fn(fn, n - 1) if n > 0 else 1
r = fn_factorial(fn_factorial, 5)
print(r)

# def fn_factorial(a):
#     if a <= 1:
#         return 1
#     else:
#         return a * fn_factorial(a - 1)
# 
# print(fn_factorial(3))

