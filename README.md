Enviornment setup
To setup python in unbuffer mode to print things quicker, use the below command.
`export PYTHONUNBUFFERED=1`
Or in the python scripts to run,  use the below shebang
```
#!/bin/sh
''''exec python3 -u -- "$0" ${1+"$@"} # '''
```

Python script that runs commands
- `run_command.py`

Example commands
- `test_command.py`: Command that has sleep
- `crash_command.py`: Command will crash.
- `crash_command_shebang.py`: Command with special shebang for unbuffered python
- `test_command_shebang.py`: Command with special shebang for unbuffered python
