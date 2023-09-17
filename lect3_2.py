x = 10
# x = -1

if x > 0:
    print("x is positive")

elif x < 0:
    print("x is negative")

else:
    print("x is zero")
    
a = 10
# a = 1

if (a % 2 == 0):
    print("짝수")
else:
    print("홀수")
    
if (x == a):
    print("같음")
else:
    print("다름")

b = 'b'
if (b == 'a'):
    print("참")
elif (b == 'b'):
    print("참")
else:
    print("거짓")
    
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in my_list:
    for num in row:
        print(num)
        
for i in range(10):
    print(i)
    
for c in "String":
    print(c)
    
for fruit in reversed(fruits):
    print(fruit)
    
for fruit in sorted(fruits, reverse=True):
    print(fruit)
    
for i in range(2, 10):
    for j in range(1, 10):
        print(i * j)
        
rang = [5, 8, 3, 1, 6]

for i in rang:
	print("element : ", i)
else :
	print("end process")
 
for i in range(10):
    if i == 7:
        print("break ", i)
        break
    elif i == 1:
        print("continue ", i)
        continue
    else:
        print("pass ", i)
        pass

    print(i)

i = 1

while i <= 5:
    print(i)
    i += 1

j = 0

while j <= 9:
    print(j)
    j += 1

s = "String"
idx = 0
while idx < len(s):
    print(s[idx])
    idx += 1

sum_ = 0
i = 1
while i <= 10:
    sum_ += i
    i += 1

print(sum_)

i = 1
while i <= 100:
    if i % 2 == 0:
        print(i)
    i += 1

i = 1
while i <= 100:
    if i % 2 == 1:
        print(i)
    i += 1

i = 1
while i <= 100:
    if i % 7 == 0:
        print(i)
    i += 1