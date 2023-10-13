#파일 생성
#f=open("new.txt", 'w')
'''
f = open("temp.txt", 'w+')
f.close()
'''
#파일 쓰기
'''
file = open("temp.txt", "w")
'''

#file.write("hello\n") :역슬레쉬로 한 라인이 생김.
'''
file.write("hello")
file.write("world")

file.close()
'''

# c:/User/Catholic/temp.txt
'''
f=open("c:/Users/ryuhyeonjeong/Desktop/대학/2023/1-2/미정프/python/my_first_repository/temp.txt", "w")
for i in range(100) :
    f.write(f"{i}\n")
    
f.close()
'''

#추가쓰기
'''
file = open("c:/Users/ryuhyeonjeong/Desktop/대학/2023/1-2/미정프/python/my_first_repository/temp.txt", "a")

file.write("hello\n")
file.write("world")

file.close()
'''

#파일읽기
'''
file = open("temp.txt", "r")
res = file.read()
print(res)

file.close()
'''

#다른 경로로 파일 읽기
'''
f = open("c:/Users/ryuhyeonjeong/Desktop/대학/2023/1-2/미정프/python/my_first_repository/temp.txt", "r")
res = f.read()
print(res)

f.close()
'''

#readline

#f = open("temp.txt", "r")
'''
f = open("temp.txt", "r")

for i in range(110):
    res = f.readline()
    print(res)
    
f.close()
'''

#readlines 읽기
'''
f = open("temp.txt", "r")
res = f.readlines()
print(res)

f.close()
'''


#readlines 읽기
'''
f = open("temp.txt", "r")
line = f.readlines()
for l in line :
    print(1)
    
f.close()
'''


#file object
'''
f = open("temp.txt", "r")
for line in f :
    print(line)
    
f.close()
'''

