'''

#입력 암호화

import getpass

#pw=getpass.getpass("Pass : ")
pw = input("Pass :")
print(pw)

#해시함수

import hashlib

hl = hashlib.sha256()
#target = "hello"
#target = "hi"
#target = "world"
#target = "python"
#target = "media"
#target = "media program"
#target = "1234567890"
target = "to be or not to be, That is a question!"

hl.update(target.encode("utf-8"))
print(hl.hexdigest())



#keccak256

import Crypto.Hash.keccak as kek

#target = "hello"
#target = "hi"
#target = "world"
#target = "python"
#target = "media"
#target = "media program"
#target = "1234567890"

target = "to be or not to be, That is a question!"

kksh = kek.new(digest_bits=256)
kksh.update(target.encode("utf-8"))

print(kksh.hexdigest())

#입력키 변환

import getpass
import hashlib

pw = getpass.getpass("Pass : ")
print(pw)

hl = hashlib.sha256()

hl.update(pw.encode("utf-8"))
print(hl.digest())
print(hl.hexdigest())


import hashlib
import os

def pwInsert():
    if os.path.exists('pw.txt'):
        pw = input('insert pass :')
        hs = hashlib.sha256()
        hs.update(pw.encod("utf-8"))
        with open('pw.txt', 'r') as fp:
            return hs.hexdigest() == fp.read()
    else:
        return True
    
    
if pwInsert():
    pw=input('new pass :')
    with open('pw.txt', 'w') as fp:
        hs = hashlib.sha256()
        hs.update(pw.encode("utf-8"))
        fp.write(hs.hexdigest())
    
else:
    print("not allow password")


#시스템 정보
import platform as pf

pn = pf.uname()
print(pn)

pm = pf.machine()
print(pm)

pp = pf.processor()
print(pp)

ps = pf.system()
print(ps)




#웹정보 읽기1

import urllib.request as ur

url = 'https://www.google.com'
#url = "https://www.daum.net"

#res = urllib.request.urlopen(url)
res = ur.urlopen(url,verify=False)

web = res.read()

with open("ul.html", "wb") as fp:
    fp.write(web)

print(web)
    


#웹정보 읽기2

import http.client as hc

#url = 'https://www.google.com'
#url = "https://daum.net"
url = 'www.google.com'

conn = hc.HTTPSConnection(url)
conn.request("GET", "/")

r = conn.getresponse()

with open("ulcl.html", "wb")as fp:
    fp.write(r.read())
    
conn.close()

print(r)



import time
#싱글스레드

start = time.time()

def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")

for i in range(3) :
    counter(f"num{i}")
    
end = time.time()

print("single end", end - start)



import threading as td

def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")

thread1 = td.Thread(target=counter, args=("1num",))
thread2 = td.Thread(target=counter, args=("2num", ))
thread3 = td.Thread(target=counter, args=("3num", ))

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

print("multi end", end - start)


#병렬처리

import multiprocessing

def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")
        
process1 = multiprocessing.Process(target=counter, args=("1num",))
process2 = multiprocessing.Process(target=counter, args=("2num",))
process3 = multiprocessing.Process(target=counter, args=("3num",))

start = time.time()

process1.start()
process2.start()
process3.start()
end = time.time()

print("proc-end", end-start)
'''

#main

def main() :
    print("hello world")
    
def run() :
    print("hello world")
    
if __name__ == "__main__":
    #run()
    main()