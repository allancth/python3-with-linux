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

import random

min_number = 1
max_number = 3
answer = random.randint(min_number, max_number)

guess = input("Guess the number - " + str(min_number) + " to " + str(max_number) + ": ")
guess = int(guess)

if guess < min_number or guess > max_number:
    print("Only number from {0} to {1}, inclusive.".format(min_number, max_number))
elif guess == answer:
    print("You're right!")
elif guess < answer:
    print("Nope! The answer is bigger than your guess.")
else:
    print("Nope! The answer is smaller than your guess.")

