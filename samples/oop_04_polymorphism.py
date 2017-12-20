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

from oop_02_square import Square
from oop_02_rectangle import Rectangle
from oop_02_triangle import Triangle
from oop_02_circle import Circle
import random

class ShapePainter(object):

    def paint_red(self, shape):
        shape.apply_color("red")

    def paint_green(self, shape):
        shape.apply_color("green")

    def paint_blue(self, shape):
        shape.apply_color("blue")

s = [ Square("Alice", 10), 
    Rectangle("Bob", 10, 20), 
    Triangle("Catherine", 10, 10), 
    Circle("David", 5), 
    Square("Erica", 25), 
    Rectangle("Frank", 12, 24), 
    Triangle("Gloria", 7, 21), 
    Circle("Harvey", 13), 
    Square("Ivy", 16), 
    Rectangle("James", 7, 22), 
    Triangle("Kerry", 10, 10), 
    Circle("Liam", 1)
    ]

sp = ShapePainter()
for e in s:
    r = random.randint(1, 3)
    if r == 1: sp.paint_red(e)
    elif r == 2: sp.paint_green(e)
    else: sp.paint_blue(e)

#     if isinstance(e, Square):
#         sp.paint_red(e)

for e in s:
    print("{0} and the area is {1:.4f}.".format(e, e.sq_area()))

