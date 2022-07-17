# Python

## Scalar Objects

- int : 5
- float : 3.27
- bool : True False
- NoneType : None
- String : 'a'
- can use `type()` to see the type of an object

```
>>> type(3.1)
<class 'float'>
>>> type(5)
<class 'int'>
>>> type(None)
<class 'NoneType'>
>>> type(True)
<class 'bool'>
>>> type('a')
<class 'str'>
>>>
```

- change object type

```
>>> float(5)
5.0
>>> int(3.9)
3
>>>
```

## Printing to console

use `print` function to print object to screen.

## Operators on ints and floats

```
>>> 3+2
5
>>> 3-2
1
>>> 3*2
6
>>> 4/2
2.0
>>> 6//5
1
>>> 6%4
2
>>> 3**2
9
>>>
```

### operator precedence without parentheses

`**` >`*` > `/` > `+` or `-`

## Binding Variables and Values

`variable` = `value`

```
>>> pi = 3.1415
>>> pi
3.1415
>>>
```

```
pi = 3.14
radius = 2.2
area = pi * (radius ** 2)
```

## Comparison Operators on int and float

- i and j are any variable names
- use `==` equal, `!=` not equal

```
>>> i = 3
>>> j = 5
>>> i > j
False
>>> i >= j
False
>>> i < j
True
>>> i <= j
True
>>> i == j
False
>>> i != j
True
>>>
```

## Logic operators on bools

- a and b are any variable names

  `a`  and `b`  == True if `a` is True and `b` is True

  `a` or `b` == True if `a` is True or `b` is True

  not `a` == True if `a` is False

## Branching Programs

```python
x = int(input('Enter an integer:'))
if x % 2 == 0:
    print('')
    print('Even')
else:
    print('')
    print('Odd')
print('Done with conditional')
```

```python
x, y, z = map(int, input('enter x,y,z and split with ",":\n').split(','))
if x < y and x < z:
    print('x is least')
elif y < z:
    print('y is least')
else:
    print('z is least')
```

```python
x, y = map(float, input('input x and y use space to separate them.\n').split(' '))
if x == y:
    print('x = y')
    if y != 0:
        print('x / y = ', x / y)
elif x < y:
    print('x is smaller')
else:
    print('y is smaller')
print('thanks!')
```

## Strings,Branching,Iteration

### Variables

- <span style="color:red">name</span>
    - descriptive
    - meaningful
    - helps re-read code
    - cannot be <strong>keywords</strong>
- <span style='color:red'>value</span>
    - store information
    - can be update

### exchange the variables value

```python
x = 1
y = 2
x, y = y, x
```

## Types

- String

