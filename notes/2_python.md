>[Back to Index](README.md)

### Table of contents
- [Getting Started with Python](#getting-started-with-python)
  - [Running Python](#running-python)
  - [Common Data Types](#common-data-types)
  - [Control Flow](#control-flow)
- [Basic and Intermediate Scripting](#basic-and-intermediate-scripting)
- [Libraries: PIP, Virtual/Env](#libraries:-pip,-Virtual/Env)
- [Building a Web Application with Python and Flask](#building-a-web-application-with-python-and-flask)

# Getting Started with Python

## Running Python
### REPL 
Python is an interpreted language, and the code is evaluated line-by-line. Since each line can be evaluated by itself, the time between evaluating each line doesn’t matter, and this allows us to have a **REPL**.

**REPL** stands for: Read, Evaluate, Print, Loop 

Each line is read, evaluated, the return value is then printed to the screen, and then the process repeats. 

```python
ailin@Ailin:/mnt/c/Users/Khoo Ai Lin/Desktop/Cloud suport and devops/practice/python$ python3
Python 3.8.2 (default, Mar 13 2020, 10:14:16)
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 1 + 1
2
>>> None
>>> exit()
```

- Access REPL by running `python3` from terminal 
- The `>>>` indicates that you can type on that line. 
- To exit the REPL, `type exit()` or `CTRL+d`

### Creating and running Python scripts

1. Create a python script `vim hello.py`
2. Enter the line in vim `print("Hello World")`
3. Pass the file to python CLI to run it `python3 hello.py`
4. Check where is the executable file `which python3`
4. Add shebang at the top line of script `#!/usr/bin/python3`
5. Make the python file executable `chmod u+x hello.py`
6. Run the script ` ./hello.py` The command takes into consideration that you are in the same directory as the file is in.
7. Change name of file `mv hello.py hello`
7. Run the script without specifying the absolute path by adding directory to `$PATH`  

```bash
$ mkdir ~/bin
$ mv hello ~/bin/
$ export PATH=$HOME/bin:$PATH
$ hello
Hello, World!
```

### Comments

```python
# This is a single line comment 
"""
This is not a block comment, it is a string, but it will still work when you really need for some lines of code to not execute.
"""
```

## Common Data Types

### Strings

Create strings using either single quotes ('), double quotes ("), or triple single or double quotes for a multi-line string.

```python
>>> 'single quoted string'
'single quoted string'
>>> "double quoted string"
'double quoted string'
>>> '''
... this is a triple
... quoted string
... '''
'\nthis is a triple \nquoted string \n'
>>> print ('''
... this is a triple
... quoted string
... ''')
this is a triple
quoted string
```
Combine strings using the + operator and multiply a string by a number using the * operator: 

```python
>>> "pass" + "word"
'password'
>>> "Ha" * 4
'HaHaHaHa'
```

### Numbers int and float)


### Booleans and None

### Working with Variables

### Lists

### Tuples

### Dictionaries

## Control Flow

### Conditionals and Comparisons 

### while loop

### for loop

### Logic Operations

# Basic and Intermediate Scripting



_[Back to the top](#table-of-contents)_
