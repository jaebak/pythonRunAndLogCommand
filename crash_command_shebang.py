#!/bin/sh
''''exec python3 -u -- "$0" ${1+"$@"} # '''
import sys
import time
import random
import string
#letters = string.ascii_letters
print ('stdout: '+''.join(random.choice(letters) for i in range(1000)) )
print("stderror: with print", file=sys.stderr)
print("stdout: Wait 3 seconds")
time.sleep(3)
print("for stdout.")
print ( ''.join(random.choice(letters) for i in range(1000)) )
print("for stderror with print", file=sys.stderr)
print("stdout: Wait 4 seconds")
time.sleep(4)
sys.exit("for stderr")
