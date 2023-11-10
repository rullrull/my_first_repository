'''
import multiprocessing as mp
import time

def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")
        
if __name__== "__main__":
    process1 = mp.Process(target=counter, args=("1um"))
    process2 = mp.Process(target=counter, args=("2um"))
    process3 = mp.Process(target=counter, args=("3um"))
    
    start=time.time()
    
    process1.start()
    process2.start()
    process3.start()
    
    process1.join()
    process2.join()
    process3.join()
    end =time.time()
    
    print("proc-end", end-start)

import asyncio
import random as rd

async def tester(name):
    snum = rd.randint(10,20)
    print(f"{name}-{snum}")
    for i in range(snum):
        await asyncio.sleep(1)
        print(f"{name}-{snum}-{i}")
        
    print(f"end of {name}")
    
async def main():
    task1 = asyncio.create_task(tester("1test"))
    task2 = asyncio.create_task(tester("2test"))
    task3 = asyncio.create_task(tester("3test"))
    
    print("start")
    start = time.time()
    await task1
    await task2
    await task3
    end = time.time()
    print("end", end-start)
    
    if __name__ == '__main__':
        asyncio.run(main())


import asyncio
import time

async def worker1():
    for i in range(1,6):
        print(f"Task 1:Step{i}")
        await asyncio.sleep(1)
        
async def worker2():
    for i in range(1,4):
        print(f"Task 2:Step{i}")
        await asyncio.sleep(2)
        
async def main():
    
    task_1=asyncio.create_task(worker1())
    task_2=asyncio.create_task(worker2())
    
    print("start task")
    start = time.time()
    await task_1
    await task_2
    end=time.time()
    print("end-", end-start)
    print("end task")
    
if  __name__ == '__main__':
    asyncio.run(main())
    


#스케쥴

import time
import sched

start = time.time()

def tester(name):
    print(f"start-time {time.time()-start}")
    for i in range(3):
        print(f"{name}-{i}")
        
    print(f"end of {name}")

def run():
    s = sched.scheduler()
    s.enter(5,1, tester, ('1num',))
    s.enter(3,1, tester, ('2num',))
    s.enter(7,1, tester, ('3num',))
    s.run()

if __name__ == "__main__":
    run()
    #main()
    print("end")




#문자열 비교

import diff_match_patch.diff_match_patch as dm

origin = "To be or not to be, That is a question!"
copyed = "To be or not to be, That is a question!"

dmp = dm()
diff = dmp.diff_main(origin, copyed)
dmp.diff_cleanupSemantic(diff)

for d in diff:
    print(d)
    


#faker임의 데이터

from faker import Faker as fk

#temp = fk()
temp = fk("ko-KR")
print(temp.name())

#with open("fktemp.csv", "w", newline='') as f:
with open("fktemp.", "w", newline='') as f:
    for i in range(30) :
        f.write(temp.name() + "," +
	    temp.address() + "," + 
	    temp.postcode() + "," + 
	    temp.company() + "," + 
	    temp.job() + "," + 
	    temp.phone_number() + "," + 
	    temp.email() + "," + 
	    temp.user_name() + "," + 
	    temp.ipv4_private() + "," + 
	    temp.ipv4_public() + "," + 
	    temp.catch_phrase() + "," + 
    	temp.color_name() + "\n" )



#시스템명령어 사용

import subprocess as sp

#res = sp.run(["cmd", "/c", "dir"], capture_output=True)
#res = sp.run(["cmd", "/c", "dir"], capture_output=False)
#res = sp.run(["cmd", "/c", "C:\Program Files\DAUM\PotPlayer"], capture_output=False)
#res = sp.run(["cmd", "/c", "ipconfig", "/all"], capture_output=True)
#print(res)



#에러처리

import traceback as tb

def tester():
    return 1/0

def caller():
    tester()
    
    
def main():
    try :
        caller()
        
    #except ZeroDivisionError:
    #    print("zde error")
        
    except ValueError :
        print("ve error")
        
    except Exception as ex:
        print("ex error", ex)
        
    else :
        print("ok")
        
    finally :
        print("end")
        
    #except :
        print(tb.format_exc())
        
#def main():
 #   caller()
    
if __name__ == "__main__":
    main()
    


#태그 찾기

from bs4 import BeautifulSoup as bs
import requests as rq

url = "https://www.daum.net/"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, 'html.parser')

#pres = res_html.find("h1")
pres = res_html.find("h2")
print(pres)
print("\n1--------------------------\n")
print(pres.get_text().strip())
print("\n2--------------------------\n")
print(pres.next_element.get_text().strip())
print(pres.get_text())
print("\n6--------------------------\n")



pres = res_html.find("title")
print(tres)
print("\n3--------------------------\n")
print(tres.next_element) 
print(tres.get_text().strip())
print("\n4--------------------------\n")



fares = res_html.findAll("a")
for i in fares :
    print(i.get_text())
#print(fares)
print("\n5--------------------------\n")


clres = res_html.findAll(class_="doc-title")
print(clres)

print("\n6--------------------------\n")
clrs=res_html.find(class_="head_top")
print(clrs)
print(clrs.get_text())
     

      
# 찾기

from bs4 import BeautifulSoup as bs
import requests as rq

url = "https://www.daum.net/"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, 'html.parser')

item = res_html.select_one("body > div.cotainer-table")

#print(item)
print(item.get_text())

wt=res_html.select_one("#content_table > div.table")
print(wt.get_text())

goods = res_html.select_one("#content_table > div.table")
#print(goods)
print(goods.get_text())
'''

#select
from bs4 import BeautifulSoup as bs
import requests as rq

url = "https://www.daum.net/"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, 'html.parser')

iss = res_html.select("a.wrap_thumb")
#print(iss)
print("\n------------------------\n")

for i in iss:
    issue = i.get_text()
    print(issue)
    
print("\n----------------------------\n")
ct = res_html.select("a.wrap_thumb")
for j in ct :
    c = j.attrs["data-tiara-custom"]
    print(c + "\n")