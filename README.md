# grader
tools for grading coding assignments

## autograde.py

This will blindly run whatever scripts are in `studentDirectory`.  This is probably a bad idea, don't do this.

```
usage: autograde.py [-h] studentDirectory expectedDirectory

Automagically run python scripts and diff their outputs.

positional arguments:
  studentDirectory   directory with student scripts
  expectedDirectory  directory with expected outputs
```
