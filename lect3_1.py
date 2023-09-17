x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is y)  
print(x is z)  
print(x is not y)  

a = 5
b = 5

print(a is b)
print(a is not b)

print(3 == 3.0)
print(3 is 5.0)

a = [3, 5, 1]
b = a

print(a)
print(b)

a[0] = 2
print(a)

x = 2 ** 3 ** 2
print(x)    

print(2 + 3 * 4)
print(10 / 5 / 2)
print(2 ** (3 ** 2))
print(10 % 3 % 2)
print(1 + 2 > 3 and 4 - 1 < 2)
print(not False and True)
print(not True or False and True)
print(1 & 2 | 3 ^ 4)
print(5 in [3, 4, 5] or 2 not in [1, 2, 3])
print(2 * -3 // 2)
print(1 == 2 != 3)