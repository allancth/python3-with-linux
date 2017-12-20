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

from threading import Thread
from datetime import datetime
import time

class Clock(Thread):

    def __init__(self):
        Thread.__init__(self)
        self._running = True

    def __enter__(self):
        return self

    def __exit__(self, t, v, tb):
        self.stop()

    def run(self):
        while self._running:
            time.sleep(1)
            if self._running:
                print(datetime.now())

    def stop(self):
        self._running = False

    def is_running(self):
        return self._running

c = Clock()
c.start()
while c.is_running():
    if input("Type 'x' and press [Enter] to stop\n") == "x":
        c.stop()

# with Clock() as c:
#     c.start()
#  
#     while True:
#         if input("Type 'x' and press [Enter] to stop\n") == "x":
#             break

