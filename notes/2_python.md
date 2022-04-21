>[Back to Index](README.md)

### Table of contents
- [Getting Started with Python](#getting-started-with-python)
  - [Running Python](#running-python)
  - [Common Data Types](#common-data-types)
  - [Control Flow](#control-flow)
- [Basic and Intermediate Scripting](#basic-and-intermediate-scripting)
  - [Basic Scripting](#basic-scripting)
  - [Intermediate Scripting](#intermediate-scripting)
- [Libraries: PIP, Virtual/Env](#libraries-pip-virtualenv)
  - [Useful Standard Library Packages](#useful-standard-library-packages)
  - [Using Pip and Virtualenv](#using-pip-and-virtualenv)
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
6. Run the script ` ./hello.py` The command takes into consideration that you are in the same directory as the file is in. There is no need to append python3 in front to run the file. 
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
Strings are immutable which means you can’t change an existing string.

### Numbers (int and float)

```python
>>> 2 + 2 # Addition
4
>>> 10 - 4 # Subtraction
6
>>> 3 * 9 # Multiplication
27
>>> 5 / 3 # Division with floating point result
1.6666666666666667
>>> 5 // 3 # Floor division; quotient
1
>>> 8 % 3 # Remainder
2
>>> 2 ** 3 # Exponential
8
```
Convert using `int`, `float`, `str` function

```python
>>> str(1.1) #string
'1.1'
>>> int("10") #integer
10
>>> int(5.999) #integer
5
>>> float("5.6") #float
5.6
>>> float(5) #float
5.0
```
### Booleans and None

Python has two boolean constants:  `True` and `False`. The constant used to represent lack of value is `None`.

### Working with Variables

We can assign a value to a variable by using a single `=`.

```
>>> my_str = "This a string"
>>> print(my_str)
This a string
```
Check the type of variable by using `type`.

```
>>> message = 'And now for something completely different'
>>> n = 17
>>> pi = 3.1415
>>> type(message)
<class 'str'>
>>> type(n)
<class 'int'>
>>> type(pi)
<class 'float'>
```

`76trombones` is illegal because it begins with a number. `more@` is illegal because it contains an illegal character, `@`. But what’s wrong with `class`? It turns out that class is one of Python’s keywords and they cannot be used as variable names.
Python reserves 35 keywords:
```
and       del       from      None      True
as        elif      global    nonlocal  try
assert    else      if        not       while
break     except    import    or        with
class     False     in        pass      yield
continue  finally   is        raise     async
def       for       lambda    return    await
```

### Lists

A list is a sequence of values. In a string, the values are characters; in a list, they can be any type. A list is created in Python by using the square brackets (`[` and `]`). The syntax for accessing the elements of a list is the same as for accessing the characters of a string: the bracket operator. The expression inside the brackets specifies the index.

```python
>>> my_list = [1, 2, 3, 4, 5]
>>> my_list[0]
1
>>> my_list[1]
2
>>> print(mixed_list)
['dog', 2.0, 5, [10, 20]]
```
The above list contains a string, a float, an integer, and another list. A list within another list is *nested*.

Lists are mutable because you can change the order of items in a list or reassign an item in a list. When the bracket operator appears on the left side of an assignment, it identifies the element of the list that will be assigned.

```python
>>> numbers = [17, 123]
>>> numbers[1] = 5
>>> print(numbers)
[17, 5]
```


### Tuples

Tuples are a fixed width, immutable sequence type. We create tuples using parenthesis `(` and `)` and at least one comma `,`.

We can use tuples in some operations like concatenation, but we can’t change the original tuple that we created. One interesting characterist of tuples is that we can unpack them into multiple variables at the same time. Since tuples are immutable, we don’t have access to the same methods that we do on a list. We can use tuples in some operations like concatenation, but we can’t change the original tuple that we created. 

```python
>>> point = (2.0, 3.0)
>>> point_3d = point + (4.0,)
>>> point_3d
(2.0, 3.0, 4.0)
>>> type(point_3d)
<class 'tuple'>
>>> x, y, z = point_3d
>>> x
2.0
>>> y
3.0
>>> z
4.0
```

### Dictionaries

Dictionary is a mapping between a set of indices (which are called keys) and a set of values. Each key maps to a value. The association of a key and a value is called a key-value pair or sometimes an item. We create dictionary literals by using curly braces `{` and `}`, separating keys from values using colons `:`, and separating key/value pairs using commas `,`. Here’s an example dictionary: 

```python
>>> ages = { 'kevin': 59, 'alex': 29, 'bob': 40 }
>>> ages
{'kevin': 59, 'alex': 29, 'bob': 40}
```
Elements of a dictionary are not indexed with integer indices. Instead, you use the keys to look up the corresponding values:
```python
>>> ages['kevin']
59
```
To add items to the dictionary, you can use square brackets:

```python
>>> ages['kayla'] = 21
>>> ages
{'kevin': 59, 'alex': 29, 'bob': 40, 'kayla': 21}
```

Items can be removed from a dictionary using the `del` statement or by using the `pop` method: 

```python
>>> del ages['kevin']
>>> ages
{'alex': 29, 'bob': 40, 'kayla': 21}
>>> ages.pop('alex')
29
>>> ages
{'bob': 40, 'kayla': 21}
```

We use the `values` and `keys` method to return the keys of the dictionary as a list. 

```python
>>> ages = {'kevin': 59, 'bob': 40}
>>> ages.keys()
dict_keys(['kevin', 'bob'])
>>> ages.values()
dict_values([59, 40])
>>> list(ages.values())
[59, 40]
```

Alternate way to create dictionary using the `dict` constructor

```python
>>> weights = dict(kevin=160, bob=240, kayla=135)
>>> weights
{'kevin': 160, 'bob': 240, 'kayla': 135}
```

## Control Flow

### Conditionals and Comparisons 

```
>>> 1 < 2
True
>>> 0 > 2
False
>>> 2 == 1
False
>>> 2 != 1
True
>>> 3.0 >= 3.0
True
>>> 3.1 <= 3.0
False
>>> 1.1 == "1.1"
False
>>> 1.1 == float("1.1")
True
>>> "this" == "this"
True
>>> "this" == "This"
False
>>> "b" > "a"
True
>>> "abc" < "b"
True
```
Notice that the string 'b' is considered greater than the strings 'a' and 'abc'. The characters are compared one at a time alphabetically to determine which is greater. This concept is used to sort strings alphabetically.

`in` is a boolean operator that takes two strings and returns `True` if the first appears as a substring in the second:

```
>>> 2 in [1, 2, 3]
True
>>> 4 in [1, 2, 3]
False
>>> 2 not in [1, 2, 3]
False
>>> 4 not in [1, 2, 3]
True
```
In order to write useful programs, we almost always need the ability to check conditions and change the behavior of the program accordingly. Conditional statements give us this ability. The simplest form is the `if` statement:

```python
if x > 0 :
    print('x is positive')
```

The boolean expression after the `if` statement is called the condition. We end the `if` statement with a colon character `:` and the line(s) after the `if` statement are indented.

If you enter an `if` statement in the Python interpreter, the prompt will change from three chevrons to three dots to indicate you are in the middle of a block of statements, as shown below:

```python
>>> x = 3
>>> if x < 10:
...     print('Small')
...
Small
>>>
```
To add an alternative code path, we’ll use the `else` keyword, followed by a colon `:`, and indenting the code underneath:

```python
>>> if False:
...     print("Was True")
... else:
...     print("Was False")
...
Was False
```
In the event that we want to check multiple potential conditions we can use the `elif CONDITION:` statement. 

```python
>>> name = "Kevin"
>>> if len(name) >= 6:
...     print("name is long")
... elif len(name) ==5:
...     print("name is 5 characters")
... elif len(name) >=4:
...     print("name is 4 or more")
... else:
...     print("name is short")
...
name is 5 characters
```
Notice that we fell into the first `elif` statement’s block and then the second `elif` block was never executed even though it was true. We can only exercise one branch in an `if` statement.

### while loop

`while` loop repeats itself based on a condition that we pass to it. Here’s the general structure of a `while` loop:

```python
while CONDITION:
    pass
```

```
>>> n = 5
>>> while n > 0:
...     print(n)
...     n = n -1
...
5
4
3
2
1
```
The flow of execution for a `while` statement:

- Evaluate the condition, yielding `True` or `False`.

- If the condition is false, exit the `while` statement and continue execution at the next statement.

- If the condition is true, execute the body and then go back to step 1.

We call each time we execute the body of the loop an iteration. For the above loop, we would say, “It had five iterations”, which means that the body of the loop was executed five times.

```
>>> while True:
...     line = input('>')
...     if line[0] == '#':
...             continue
...     if line == 'done':
...             break
...     print(line)
...
>hello there
hello there
># don't print this
>print this
print this
>done
```

All the lines are printed except the one that starts with the hash sign because when the `continue` is executed, it ends the current iteration and jumps back to the `while` statement to start the next iteration, thus skipping the `print` statement. The loop condition is `True`, which is always true, so the loop runs repeatedly until it hits the `break` statement.

### for loop

Sometimes we want to loop through a set of things such as a list of words, the lines in a file, or a list of numbers. When we have a list of things to loop through, we can construct a definite loop using a `for` statement. We call the `while` statement an indefinite loop because it simply loops until some condition becomes `False`, whereas the `for` loop is looping through a known set of items so it runs through as many iterations as there are items in the set.

```
>>> colours = ['blue', 'green', 'red', 'purple']
>>> for colour in colours:
...     print(colour)
...
blue
green
red
purple
>>> colour
'purple'
```

```
>>> colours = ['blue', 'green', 'red', 'purple']
>>> for colour in colours:
...     if colour == 'blue':
...             continue
...     elif colour == 'red':
...             break
...     print(colour)
...
green
```
1. blue will populate the variable colour, it will hit `continue` and go back to the body of `for` loop.
2. green will populate the variable colour, it will go the `print(colour)` statement and go back to the body of `for` loop.  
3. red will populate the variable colour, `break` statement will be executed and it will break out of `for` loop without going to the `print` statement.

`Dictionary` is an unordered collection of data values, used to store data values like a map, which unlike other Data Types that hold only single value as an element, Dictionary holds key : value pair. `items()` method is used to return the list with all dictionary keys with values.

```
>>> ages = {'kevin': 59, 'bob': 40, 'kayla': 21}
>>> for name, age in ages.items():
...     print(f"Person Named: {name}")
...     print(f"Age of: {age}")
...
Person Named: kevin
Age of: 59
Person Named: bob
Age of: 40
Person Named: kayla
Age of: 21
>>>

```

### Logic Operations

A boolean expression is an expression that is either true or false. The following examples use the operator `==`, which compares two operands and produces `True` if they are equal and `False` otherwise:
```
>>> 5 == 5
True
>>> 5 == 6
False
>>>
```
Other comparison operators:

```
x != y               # x is not equal to y
x > y                # x is greater than y
x < y                # x is less than y
x >= y               # x is greater than or equal to y
x <= y               # x is less than or equal to y
x is y               # x is the same as y
x is not y           # x is not the same as y
```
True and False are special values that belong to the class bool; they are not strings:

```
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
```

There are three logical operators: `and`, `or`, and `not`. The semantics (meaning) of these operators is similar to their meaning in English. 

For example, `x > 0 and x < 10` is true only if x is greater than 0 and less than 10.

`n%2 == 0 or n%3 == 0` is true if either of the conditions is true, that is, if the number is divisible by 2 or 3.

Finally, the `not` operator negates a boolean expression, so `not (x > y)` is true if x > y is false; that is, if x is less than or equal to y.

Strictly speaking, the operands of the logical operators should be boolean expressions, but Python is not very strict. Any nonzero number is interpreted as “true.”

```
>>> 17 and True
True
```
```
>>> name = ""
>>> not name
True
>>> if not name:
...     print("no name given")
...
no name given
```
# Basic and Intermediate Scripting

## Basic Scripting

### Reading User Input

Python provides a built-in function called `input` that gets input from the keyboard. When this function is called, the program stops and waits for the user to type something. When the user presses `Enter`, the program resumes and `input` returns what the user typed as a *string*.

Before getting input from the user, it is a good idea to print a prompt telling the user what to input. You can pass a string to `input` to be displayed to the user before pausing for input:

```
#!/usr/bin/python3
name = input("What is your name? ")
birthdate = input("What is your birthdate? ")
age = int(input("How old are you? "))
print(f"{name} was born on {birthdate}")
print(f"Half of your age is {age / 2}")
```

```bash
ailin@Ailin:~/bin$ age
What is your name? Ai Lin
What is your birthdate? 11/11/2011
How old are you? 11
Ai Lin was born on 11/11/2011
Half your age is 5.5
```
### Function Basics

A function is a named sequence of statements that performs a computation. You can “call” the function by name. One example of a function call:

```
>>> type(32)
<class 'int'>
```
The name of the function is `type`. The expression in parentheses is called the *argument* of the function. The argument is a value or variable that we are passing into the function as input to the function.

When you define a function, you specify the *name* and the *sequence of statements*. `def` is a keyword that indicates that this is a function definition. The name of the function is `hello_world`. The empty parentheses after the name indicate that this function doesn’t take any arguments.

```
>>> def hello_world():
...     print("Hello, World")
...
>>> hello_world()
Hello, World
>>>
```
To define an arguement, we will place *parameter* in the parentheses. Inside the function, the arguments are assigned to variables called *parameters*. This function assigns the argument to a parameter `name`. When the function is called, it prints the value of the parameter.

```
>>> def print_name(name):
...     print(f"Name: {name}")
...
>>> print_name("Charmander")
Name: Charmander
>>> output = print_name("Keith")
Name: Keith
>>> output
>>>
```
If we don’t explicitly declare a return value, then the result will be `None`. To return a result from a function, we use the `return` statement in our function.

```
>>> def add_two(num):
...     return num + 2
...
>>> result = add_two(2)
>>> print(result)
4
>>>
```
When this script executes, the `print` statement will print out “4” because the `add_two` function was called with 2 as argument. Within the function, the parameter `num` is 2. The function computed the sum of 2 + 2 and used the `return` statement to send the computed value back to the calling code as the function result, which was assigned to the variable `result` and printed out.

### Using Functions in Scripts

Write a script that prompts the user for some information and calculates the user’s Body Mass Index (BMI). We want to prompt the user for their information, gather the results, and make the calculations if we can. If we can’t understand the measurement system, then we need to prompt the user again after explaining the error.

**Gathering Information**

```python
def gather_info():
    height = float(input("What is your height? (inches or meters) "))
    weight = float(input("What is your weight? (pounds or kilograms) "))
    system = input("Are your mearsurements in metric or imperial systems? ").lower().strip() 
    return (height, weight, system)
```
**Calculate and print BMI**

```python
def calculate_bmi(weight, height, system='metric'): # set the default of the function
    if system == 'metric':
        bmi = (weight / (height ** 2)) 
    else:
        bmi = 703 * (weight / (height ** 2)) 
    return bmi
```
**Set up the script's flow**

```python
while True:
    height, weight, system = gather_info() 
    if system.startswith('i'):
        bmi = calculate_bmi(weight, height, system)
        print(system)
        print(f"Your BMI is {bmi}") 
        break
 
    elif system.startswith('m'):
        bmi = calculate_bmi(weight, height) 
        print(f"Your BMI is {bmi}")
        break
    else:
        print("Error: Unknown measurement system. Please use imperial or metric.")
```
1. We want to be able to re-prompt the user, so we want to utilize an intentional infinite loop (`while True`) that we can break out of. 
2. The `gather_info` function is called and the `return` values are assigned to the variables `height, weight, system`.
3. Use conditionals loop `if elif else` to check the system type.
4. The function `calculate_bmi` takes the arguments `weight, height, system` as inputs. They are placed in the order of when the function`calculate_bmi` is created. A [positional argument](https://www.codingem.com/what-is-a-positional-argument-in-python/) in Python is an argument whose position matters in a function call. The argument must be provided in a correct position in a function call. We can pass the arguments as `keyword argument` so that the argument order does not matter. The interpreter knows which one of the arguments is height. 

    `bmi = calculate_bmi(height=height, system=system, weight=weight)`


### Using Standard Library packages

There are a lot of functions that we can use if we import them from the standard library.  Here’s how we can import the time module for use:

```
>>> import time
>>> print(time)
<module 'time' (built-in)>
```
This statement creates a *module object* named `time`. The module object contains the functions and classes defined in the module. To access one of the functions, you have to specify the name of the module and the name of the function, separated by a period. This format is called *dot notation*. Let’s call the `localtime` function provided by the time package:

```
>>> now = time.localtime()
>>> now
time.struct_time(tm_year=2022, tm_mon=4, tm_mday=19, tm_hour=18, tm_min=4, tm_sec=36, tm_wday=1, tm_yday=109, tm_isdst=0)
>>> now.tm_hour
18
```
Calling this function returns a time.struct_time to use that has some attributes that we can interact with using a period (.). Here is our first time interaction with an attribute on an object that isn’t a function. Sometimes we need to access the data from an object, and for that,
we don’t need to use parentheses.

```python
import time

start_time = time.localtime()
print(f"Timer started at {time.strftime('%X', start_time)}")

#Wait for user to stop timer
input("Press 'Enter' to stop timer ")

stop_time = time.localtime()
difference = time.mktime(stop_time) - time.mktime(start_time)

print(f"Timer stopped at {time.strftime('%X', stop_time)}")
print(f"Total time: {difference} seconds")
print(time.mktime(stop_time))
print(time.mktime(start_time))
```
```
Timer started at 18:46:35
Press 'Enter' to stop timer 
Timer stopped at 18:46:55
Total time: 20.0 seconds
1650365215.0
1650365195.0
```

1. Call the function `time.localtime()` and assign to variable `start_time`.
2. `time.strftime()` converts `struct_time` representing a time as returned by `localtime()` to a string as specified by the format argument. `%X` is the locale’s appropriate time representation.
3. Call the `input` function, the program stops and waits for the user to type something. When the user presses `Enter`, the program resumes.
4. `time.localtime()` is called again to get the stop_time. 
5. `time.mktime()` converts a time_struct into a numeric value so we can calculate the time difference. It returns a floating point number.

We’re only using a subset of the functions from the time package, and it’s a good practice to only import what we need. We can import a subset of a module using the `from` statement combined with `import`.

```python
from time import localtime, mktime, strftime

start_time = localtime()
print(f"Timer started at {strftime('%X', start_time)}")

#Wait for user to stop timer
input("Press 'Enter' to stop timer ")

stop_time = localtime()
difference = mktime(stop_time) - mktime(start_time)

print(f"Timer stopped at {strftime('%X', stop_time)}")
print(f"Total time: {difference} seconds")
print(mktime(stop_time))
print(mktime(start_time))
```

### Working with Environment Variables

We can access environment variables from inside of our Python scripts and use environment variables to configure a script or CLI. 

The `os` module allows us to access functionality of the underlying operating system. So we can perform tasks such as: navigate the file system, obtain file information, rename files, search directory trees, fetch environment variables, and many other operations. By **importing** the `os` package, we’re able to access a lot of miscellaneous operating system level attributes and functions, not the least of which is the `environ` object. This object behaves like a dictionary, so we can use the subscript operation to read from it. It is mapping object where keys and values are strings that represent the process environment. For example, environ['HOME'] is the pathname of your home directory. 

```
import os
>>> print(os.environ['HOME'])
/home/ailin
```
Printing all the environment variables (key-value pairs) will show theenvironment variables name and values will get printed.
```
>>> for k, v in os.environ.items():
...     print(f'{k}={v}')
...
SHELL=/bin/bash
WSL_DISTRO_NAME=Ubuntu
```
Read a `'STAGE'` environment variable and print out what stage we’re currently running in:
```python
import os

stage = os.environ["STAGE"].upper()

output = f"We're running in {stage}"

if stage.startswith("PROD"):
    output = "DANGER!!! - " + output
print(output)
```
```
Traceback (most recent call last):
  File "c:\Users\Khoo Ai Lin\Desktop\Cloud suport and devops\CloudDevOps\2_python\osmodule.py", line 5, in <module>
    stage = os.environ["STAGE"].upper()
  File "C:\Users\Khoo Ai Lin\AppData\Local\Programs\Python\Python310\lib\os.py", line 679, in __getitem__
    raise KeyError(key) from None
KeyError: 'STAGE'
```
```
>>> print(os.environ.get('STAGE'))
None
```
Using `get` will return `None` if a key is not present rather than raise a `KeyError`.

```python
import os
stage = os.getenv("STAGE", "dev").upper()
output = f"We're running in {stage}"
if stage.startswith("PROD"):
    output = "DANGER!!! - " + output
print(output)
```

```
We're running in DEV
```

If the `STAGE` environment variable isn’t set, then we want to change the default to `DEV`and we can do that by using the `os.getenv` function. 
`getenv(key, default=None)` If the key does not exist, `None` will be returned if we did not change the default. 

### Interacting with Files

When we want to read or write a file (say on your hard drive), we first must open the file. Opening the file communicates with your operating system, which knows where the data for each file is stored. When you open a file, you are asking the operating system to find the file by name and make sure the file exists. 

```
>>> file_handle = open('xmen_base.txt')
>>> print(file_handle)
<_io.TextIOWrapper name='xmen_base.txt' mode='r' encoding='UTF-8'>
```
If the `open` is successful, the operating system returns us a file handle. The file handle is not the actual data contained in the file, but instead it is a “handle” that we can use to read the data.

There are four different methods (modes) for opening a file:

- `r` - Read - Default value. Opens a file for reading, error if the file does not exist

- `a` - Append - Opens a file for appending, creates the file if it does not exist

- `w` - Write - Opens a file for writing, creates the file if it does not exist
 
- `x` - Create - Creates the specified file, returns an error if the file exists

- `a` open for writing, appending to the end of file if it exists

- `b` binary mode

- `t` text mode (default)

- `+` open for updating (reading and writing)


```
>>> import io
>>> dir(io.TextIOWrapper)
['_CHUNK_SIZE', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_checkClosed', '_checkReadable', '_checkSeekable', '_checkWritable', '_finalizing', 'buffer', 'close', 'closed', 'detach', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 'line_buffering', 'name', 'newlines', 'read', 'readable', 'readline', 'readlines', 'reconfigure', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'write_through', 'writelines']
```
We can use `dir()` to check the available methods for `io.TextIOWrapper`.

`read` gives us all of the contents as a single string but notice that it gave us an empty string when we called the function as second time. That happens because the file maintains a cursor position and when we first called `read` the cursor was moved to the very end of the file’s contents. 

```
>>> file_handle.read()
'Storm\nWolverine\nCyclops\nBishop\nNightcrawler\n'
>>> file_handle.read()
''
```
If we want to reread the file we’ll need to move the beginning of the file using the `seek` function. Seek to `0` and it will go to the beginning of file. By seeking to a specific point of the file, we are able to get a string that only contains what is after our cursor’s location. We can seek to `6` which is the position of the `W` character.

```
>>> file_handle.seek(0)
0
>>> file_handle.read()
'Storm\nWolverine\nCyclops\nBishop\nNightcrawler\n'
>>> file_handle.seek(6)
6
>>> file_handle.read()
'Wolverine\nCyclops\nBishop\nNightcrawler\n'
```
We can read through content is by using a for loop:

```
>>> for line in file_handle:
...     print(line, end="")
...
Storm
Wolverine
Cyclops
Bishop
Nightcrawler
```
Once we’re finished working with a file, it is important that we close our
connection to the file using the `close` function:

```
>>> file_handle.close()
>>> file_handle.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.
```
If the file already exists, opening it in write mode clears out the old data and starts fresh, so be careful! If the file doesn’t exist, a new one is created.
Let’s create a copy of our xmen file (new_xmen.txt) that we can add additional content to:

```
>>> file_handle = open('xmen_base.txt')
>>> new_fh = open('new_xmen.txt', 'w')
>>> new_fh
<_io.TextIOWrapper name='new_xmen.txt' mode='w' encoding='UTF-8'>
```
The write method of the file handle object puts data into the file, returning the number of characters written. The default write mode is text for writing (and reading) strings. However, we could not read the file handle as we only open for writing. Therefore, we close the file and reopened the file, using the `r+` mode which will allow us to read and write content to the file.

```
>>> new_fh.write(file_handle.read())
44
>>> new_fh.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
io.UnsupportedOperation: not readable
>>> new_fh.close()
>>> new_fh = open('new_xmen.txt', 'r+')
>>> new_fh.read()
'Storm\nWolverine\nCyclops\nBishop\nNightcrawler\n'
```

```
>>> new_fh.seek(0)
0
>>> new_fh.write("Beast\n")
6
>>> new_fh.write("Phoenix\n")
8
>>> new_fh.seek(0)
0
>>> new_fh.read()
'Beast\nPhoenix\ne\nCyclops\nBishop\nNightcrawler\n'
>>> new_fh.close()
>>> file_handle.close()
```
A fairly common thing to want to do is to append to a file without reading its current contents. This can be done with the `a` mode. Let’s close the `xmen_base.txt` file and reopen it in the `a` mode to add another name without worrying about losing our original content. This time, we’re going to use the `with` statement to temporarily open the file and have it automatically closed after our code block has executed. There is no need to call `file.close()` when using `with` statement.

```
>>> with open('xmen_base.txt', 'a') as file:
...     file.write('Professor Xavier\n')
...
17
```
Another way of creating the file variable outside the `with` statement:

```
>>> file = open('xmen_base.txt', 'a')
>>> with file:
...     file.write("Something\n")
...
10
>>> exit()
```
```
$ cat xmen_base.txt
Storm
Wolverine
Cyclops
Bishop
Nightcrawler
Professor Xavier
Something
```

## Intermediate Scripting

### Parsing Command Line Parameters

The `sys` module provides valuable information about the Python interpreter. You can also use it to obtain details about the constants, functions and methods of the Python interpreter.

`argv` function is used to display the arguments used while executing the script or to store for other purposes.

Write a script:
```
#!/usr/bin/python3
import sys
print(f"First argument {sys.argv[0]}")
```
Run the script (The first argument is the script itself):
```
$ chmod u+x ~/bin/param_echo
$ param_echo testing
First argument /home/user/bin/param_echo
```
Another example to get index of `1`: 

```
#!/usr/bin/python3

import sys
print(f"Positional arguments: {sys.argv[1:]}")
print(f"First argument: {sys.argv[1]}")
```
```
$ param_echo testing testing12 'another argument'
Positional arguments: ['testing', 'testing12', 'another argument']
First argument: testing
```
Positional arguments are based on spaces unless we explicitly wrap the
argument in quotes (`'another argument'`).


### Robust CLIs with argparse

### Catching an exception

### Exit Statuses

### Execute Shell Commands

### Advanced Iteration with List Comprehension

# Libraries: PIP, Virtual/Env

## Useful Standard Library Packages

## Using Pip and Virtualenv

# Building a Web Application with Python and Flask


_[Back to the top](#table-of-contents)_
