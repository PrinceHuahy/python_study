a = 'Hello Python!'
print(a[2:7])
print(a[-8:-2])
print(a[1:])
print(a[:-2])
a = '     This is before whitespace'
b = 'This is after whitespace'
c = '    Both side have whitespace   '
print(a.strip())
print(b.strip())
print(c.strip())

a = 'Hello, This is a mistake, Thank you.'
print(a.split(','))