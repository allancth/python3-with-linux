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

d = set({ 3, 2, 1 })
print(d)

try:
    d = { 3, 2, 1 }
    print(d)
    print(d.__class__)

    d["name"] = "Alice"
except TypeError as e:
    print(e)

d = {}
print(d)
print(d.__class__)

d["name"] = "Alice"
d["age"] = 30
d["occupation"] = [ "Doctor" ]
print(d)

for k, v in d.items():
    print("{0}={1}".format(k, v))

l = [ {
    "name" : "Bob",
    "age" : 31, 
    "occupation" : [ "Lawyer", "Father" ]
    }, d ]

for i in l:
    print(i)

d["name"] = "Charlie"
for i in l:
    print(i)

