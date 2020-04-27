# Import packages
import pandas           # Regular import
import pandas as pd     # Import with an alias
from math import  sqrt  # Import submodule of a module

# Operators:
print('Arithmetic: +, -, *, /, **, //, %')
print('Assignment: =, +=, *=')

# Variables & Assignment Operators

# Regular Assignment
x = 1
y = 's'
z = .25

# Group Assignment
x, y, z = 1, 's', .25

# Variable:
print('Numeric: int, float, and Complex number')
print("Boolean: 'True' or 'False'")
print('Sequence: String, List, Tuple')
print('Dictionary')

### Working with Strings

# Initialize
print("some string")
print('some string')
print('This\'s a string')
print("This's a string")
print('"This is a string"')

# Concatenation
print('This' + ' ' + "a string")
print('Hello' * 2)                  # output: HelloHello

# Access Characters
str = 'Hello there!'
print(str[0])   # output: H

# String's length
print(len('abc'))   # output: 3

# Format Strings (f-strings)
str = 'a'
print(f'This is {str} string.')  # output: 'This is a string.'

### Type and Type Conversion
int, str, flt = 5, '13', .25
print(type(int))
print(type(str))
print(type(flt))
print(str(a))
print(int(str))
print(int(flt))
