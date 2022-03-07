#!/usr/bin/env python3
import sys
import time
import random
import string
letters = string.ascii_letters
print ('stdout: Print random characters')
print ('stdout: '+''.join(random.choice(letters) for i in range(1000)) )
print("stderror: with print", file=sys.stderr)
print("stdout: Wait 3 seconds")
time.sleep(3)
print("stdout: Finished waiting 3 seconds. Print random characters")
print ( ''.join(random.choice(letters) for i in range(1000)) )
print("stderror: with print", file=sys.stderr)
print("stdout: Wait 4 seconds")
time.sleep(4)
sys.exit("stderr: Exiting")
