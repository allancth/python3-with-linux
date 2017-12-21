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

from enum import Enum

class Operation(Enum):
    ADD = 1
    SUB = 2
    MUL = 4
    DIV = 8
    MOD = 16

class OperationNotSupportedException(BaseException):

    def __init__(self, op):
        BaseException.__init__(self, "{0} not supported".format(op))

def execute(a, b, op: Operation):
    if op == Operation.ADD:
        return a + b
    elif op == Operation.SUB:
        return a - b
    elif op == Operation.MUL:
        return a * b
    elif op == Operation.DIV:
        return a / b
    elif op == Operation.MOD:
        return a % b
    else:
        raise OperationNotSupportedException(op)

for e in Operation:
    print(e)

e = Operation.ADD
print("{0} = {1}".format(e.name, e.value))

r = execute(1, 2, Operation.ADD)
print(r)

# r = execute(1, 2, "pow")
# print(r)

