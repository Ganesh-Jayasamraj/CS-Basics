# Data type conversion

a = int(18.99)
b = float(6)
c = str(78)

print(a)
print(type(a))
print(b)
print(type(b))
print(c + "78")
print(type(c))

# converting string to int
d = int(c)
d = d + 52
print(d)

e = int("g")        # Expected Error "invalid literal for int() with base 10: 'g'"
print(e)