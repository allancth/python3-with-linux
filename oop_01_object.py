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

class Book(object):

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return self.title + ", by " + self.author + " (" + str(self.year) + ")"

    def __repr__(self):
        return "Book(\"{0}\", \"{1}\", {2})".format(self.title, self.author, self.year)

    def __call__(self):
        return ( self.title, self.author, self.year )

    def __del__(self):
        pass

    def __hash__(self):
        return hash(self.title + self.author + str(self.year))
 
    def __eq__(self, other):
        if self.title != other.title:
            return False
        if self.author != other.author:
            return False
        if self.year != other.year:
            return False
        return True

    def __lt__(self, other):
        return self.year < other.year

    def __le__(self, other):
        return self.year <= other.year

    def __gt__(self, other):
        return self.year > other.year

    def __ge__(self, other):
        return self.year >= other.year

b = Book("Alice in Wonderland", "Lewis Carroll", 1865)
print(b)
print(b.__class__)
print(__name__)
print(b.title)
print(b.author)
print(b.year)
print(b())
print(repr(b))
print(eval(repr(b)).title)

b1 = Book("Alice in Wonderland", "Lewis Carroll", 1865)
b2 = Book("The Wonderful Wizard of Oz", "L. Frank Baum", 1900)
print(b == b1)
print(b1 == b2)
print(b1 < b2)

