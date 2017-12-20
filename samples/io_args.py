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

import sys, getopt

opts, args = getopt.getopt(sys.argv[1:], "")
print("opts={0}, args={1}".format(opts, args))

args = "-a -b1 -b2".split()
opts, args = getopt.getopt(args, "ab:")
print("opts={0}, args={1}".format(opts, args))

args = "--a --b".split()
opts, args = getopt.getopt(args, "", [ "a", "b" ])
print("opts={0}, args={1}".format(opts, args))

args = "-a -b1 -b2 --c --d e f".split()
opts, args = getopt.getopt(args, "ab:", [ "c", "d" ])
print("opts={0}, args={1}".format(opts, args))

