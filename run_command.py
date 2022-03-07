#!/usr/bin/env python3
import subprocess
import threading

def output_reader(process, log_file):
  for line in iter(process.stdout.readline, b''):
    output = line.decode('utf-8')
    print(output, end='')
    log_file.write(output)

# https://eli.thegreenplace.net/2017/interacting-with-a-long-running-child-process-in-python/
def runAndLogCommand(command, log_file):
  print("\nRunning command2: "+command)
  log_file.write("\nRunning command: "+command+'\n')
  process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)

  thread = threading.Thread(target=output_reader, args=(process,log_file))
  thread.start()
  thread.join()

if __name__ == "__main__":
  # Use 'python3 -u', which is unbuffer mode, to print things quicker
  # To do so, use below shebang
  # #!/bin/sh
  # ''''exec python3 -u -- "$0" ${1+"$@"} # '''
  # OR set environment with below settings
  # export PYTHONUNBUFFERED=1

  print("Script will execute: "+'python3 -u test_command.py')
  with open('test_command.log', 'w') as log_file :
    runAndLogCommand('./test_command.py', log_file)
  print("Output and error logged to test_command.log\n")

  print("Script will execute: "+'python3 -u crash_command.py')
  with open('crash_command.log', 'w') as log_file :
    runAndLogCommand('./crash_command.py', log_file)
  print("Output and error logged to crash_command.log")
