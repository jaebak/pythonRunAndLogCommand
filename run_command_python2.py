#!/usr/bin/env python
from __future__ import print_function
import subprocess
import threading
import time

def output_reader_logger(process, log_file, commandOutput):
  for line in iter(process.stdout.readline, b''):
    output = line.decode('utf-8')
    print(output, end='')
    log_file.write(output)
    commandOutput[0] += output

# https://eli.thegreenplace.net/2017/interacting-with-a-long-running-child-process-in-python/
def runCommandAndLog(command, log_file):
  print("\n[Info] Running command: "+command)
  log_file.write("\n[Info] Running command: "+command+'\n')
  process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)

  commandOutput = ['']
  thread = threading.Thread(target=output_reader_logger, args=(process,log_file, commandOutput))
  thread.start()
  thread.join()
  # Try to get poll
  for iTime in range(10):
    if (process.poll() == None): time.sleep(1)
    else: break
  return process.poll(), commandOutput[0]

####

def output_reader(process, commandOutput):
  for line in iter(process.stdout.readline, b''):
    output = line.decode('utf-8')
    print(output, end='')
    commandOutput[0] += output

def runCommand(command):
  print("\n[Info] Running command: "+command)
  process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)

  commandOutput = ['']
  thread = threading.Thread(target=output_reader, args=(process,commandOutput))
  thread.start()
  thread.join()
  # Try to get poll
  for iTime in range(10):
    if (process.poll() == None): time.sleep(1)
    else: break
  return process.poll(), commandOutput[0]

if __name__ == "__main__":
  print("[Info] Script will execute: "+'./test_command.py')
  with open('test_command.log', 'w') as log_file :
    returnCode, output = runCommandAndLog('./test_command.py', log_file)
  print("[Info] Output and error logged to test_command.log\n")
  print("[Info] Printing returnCode: "+str(returnCode))
  print("[Info] Printing output to script")
  print(output)
  print()

  print("Script will execute: "+'./crash_command.py')
  with open('crash_command.log', 'w') as log_file :
    returnCode, output = runCommandAndLog('./crash_command.py', log_file)
  print("Output and error logged to crash_command.log")
  print("[Info] Printing returnCode: "+str(returnCode))
  print("[Info] Printing output to script")
  print(output)

  print("[Info] Script will execute: "+'./test_command.py')
  returnCode, output = runCommand('./test_command.py')
  print("[Info] Output and error logged to test_command.log\n")
  print("[Info] Printing returnCode: "+str(returnCode))
  print("[Info] Printing output to script")
  print(output)
  print()
