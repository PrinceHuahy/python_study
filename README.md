This is a study note. Based on [W3schools](https://www.w3schools.com/python)

# Python Syntax

- In python, double quotes or single quotes both are ok.

```python
a = "abc"
b = 'abc'
print(a == b)
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

- <span style="color:red">Attention:</span> you can not casting 'a' to int type.But you can change '3.14' to 3.14.

### Variable name

- Variable name must start with a letter or underscore character.
- Variable name can only use `A-z,0-9 and _`
- `abCd` and `abcd` are two variable.
- Personally <span style="color:red">not recommend</span> use key-word to name a variable.

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
list = [1, 2, 3]
str = 'hello'
int = 5
float = 3.14
dict = {a: 1}
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

## Comments

- Write # after code at same line with double space or start with a new line to create a comments.

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
