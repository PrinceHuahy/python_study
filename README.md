This is a study note. Based on [W3schools](https://www.w3schools.com/python)

# Python Syntax

- In python, double quotes or single quotes both are ok.

```python
a = "abc"
b = 'abc'
print(a == b)
```

## Comments

- Write # after code at same line with double space or start with a new line to create a comments.
- In Pycharm, you can easily use `ctrl + /` to comments or uncomment.

```python
a = 5
# use # before string will get a comments
print(a)  # print 5 at screen.
```

- Multi Line Comments

```python
x = 1
# comments line 1
# comments line 2
# comments line 3
print(x)
```

- You can use multiline string instead multi line comments because Python will ignore strings that are not assigned to a
  variable.

```python
"""
You can write comments
between double triple-quotes.
"""
```

## Python Variables

> variable = value

```python
a1 = 3
a2 = 3.14
a3 = 'pi'
a4 = True
a5 = None
 ```

### Variable type

- Use `type(variable)` in python can easily get variable type. Python is a case-sensitive language.

```python
x = 3.14
print(type(x))
y = 'pi'
print(type(y))
```

### Casting type

- If you want to change the variable type, you need casting them.

```python
x = 3.14
print(type(x))
y = int(3.14)
print(type(y))
print(type(str(3.14)))
z = '3.14'
print(float(z))
```

- Attention: you can not cast 'a' to int type.But you can change '3.14' to 3.14.

### Variable name

- Variable name must start with a letter or underscore character.
- Variable name can only use `A-z,0-9 and _`
- `abCd` and `abcd` are two variable.
- Personally `not recommend` use key-word to name a variable.

```python
# These variable name is ok
a = 5
_aA = 6.5
Twfsa_vczxv = True
myFuncValue = 'test'
my_func_value2 = '4'
# These variable name is unusable.
# 4a = 'hello python'
# sse$c = 2
# ffc-fasd = 65
# These are key-word variable.
# list = [1, 2, 3]
# str = 'hello'
# int = 5
# float = 3.14
# dict = {a: 1}
```

### Assign Multiple Values

- If you want to create multiple values at one time. Just use ',' to separate them.

> variable1, variable2, variable3 = value1, value2, value3

```python
a, b, c = 1, 'beta', True
print(a, b, c)
```

- Create multiple variable with same value.

> variable1 = variable2 = variable3 = value

```python
a = b = c = 5
print(a, b, c)
```

### Output Variables

- Use `print()` function to output variables.

```python
x = 1
print(x)
print(5)
print('this is a string.')
```

- You can add string and variable in print.

```python
x = 'Tom'
y = 10
print('My name is ' + x + ', and I am ' + str(y) + ' years old.')
print('My name is', x, ', and I am', y, 'years old.')
print(2 + 3)
print(3 + 2 / 5 * 7)
```

- `print` can only add same type value with `+`, so use `str(y)` to change y to string.
- You can also use `,` to "add" string in python. but with `,` it will auto add a space between two strings.
- When you use `,` in python, it's not `add` two same value. Instead, it just shows two different value with a space to
  separate them.
- You can do the calculation in print function.
- Just try to run `print(3 * 'hello')`, see what it looks like?

### Global Variables

In python, we specify that `function` can only read variable's value which not declared in `function`.

```python
x = 5


def my_func():
    print('2 + 3 = ', x)


my_func()

# def wrong_use():
#     x = x + 1
#     print(x)
# wrong_use()
```

- when you run second function, it will return a error like this

> UnboundLocalError: local variable 'x' referenced before assignment

- To avoid this error, we can use `global` to declared them.

```python
x = 5


def my_func():
    global x
    x = x + 1
    print(x)


my_func()
```

- `global` is like a label, to tell python this variable you can use everywhere.

## Python Data Types

Every language have multiple data type.

- Common data types

> str, int, float, list, tuple, range, dict, set, bool, NoneType.

- Here is all Python build-in data types.

```
Text Type:	  str
Numeric Types:	  int, float, complex
Sequence Types:	  list, tuple, range
Mapping Type:	  dict
Set Types:	  set, frozenset
Boolean Type:	  bool
Binary Types:	  bytes, bytearray, memoryview
None Type:	  NoneType
```

## Python Numbers

- In python, there are three type of number.

```python
x = 5  # int
y = 35e3  # float
z = 1 + 4j  # complex
```

### Number type casting

```python
x = 5
print(float(x))
y = 3.6
print(int(y))
z = 41
print(complex(z))
```

- when you change the type from `float` to `int`, it will lost decimal part.
- when you change the type to `complex` , it will auto add `0j`.
- `complex` type can not cast to `int` or `float`.

### Random Number

- Python can not directly use random number, it must use random lib.

```python
import random

print(random.randrange(1, 10, 2))
```

### String and Number Casting

- If string variable looks like a number, you can cast it to a number type.
- Every Number type variable can cast to a string.

```python
x = '3.14'
print(float(x))
y = 3.1415
print(str(3.1415))

```

## Python String

### Strings

- Everything in double quotation marks or single quotation marks is string.

### Multiline String

- Use three quotes to create a multiline string.

```python
a = '''This is
a multiline string
It can have multiple lines.'''
print(a)
```

### Strings are Arrays

- In Python, We can think of a string as a list of characters.
- We can use array's function to deal with string.The more info can be find in Arrays statement.

```python
a = 'Hello python'
print(len(a))
print(a[2])
for i in a:
    print(i)
print('llo' in a)
```

### Slicing Strings

- Just like array, string also have an index.

```
strign:  H  e  l  l  o  !  
index :  0  1  2  3  4  5
index : -6 -5 -4 -3 -2 -1 
```

```python
a = 'Hello Python!'
print(a[2:7])
print(a[-8:-2])
print(a[1:])
print(a[:-2])
```

### Modify Strings

- We can use `upper()` to upper case, use `lower()` to lower case.

```python
a = 'Hello, python!'
print(a.upper())
print(a.lower())
```

- Use `strip()` to remove whitespace before and after in a string.

```python
a = '     This is before whitespace'
b = 'This is after whitespace'
c = '    Both side have whitespace   '
print(a.strip())
print(b.strip())
print(c.strip())
```

- Use `replace()` to replace element in string.
```python
str_value = 'aabcdesafdasc'
print(str_value.replace('a','A'))  # change 'a' to 'A' in str_value.
```

- Use `split()` to separate string to list.
```python
a = 'Hello, This is a mistake, Thank you.'
print(a.split(','))
```
### Format Strings
-
