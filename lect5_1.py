# datetime 모듈의 datetime 함수를 dt라는 별명으로 사용
from datetime import datetime as dt

# 현재 시간 출력 dt.now()
print(dt.now())

#특정 시간대의 현재 시간 출력
#from pytz import timezone
#tz = timezone('Asia/Seoul')
#tz = timezone('UTC')
# 문자열을 날짜로 변환 dt.strptime()
date_string = '2021-07-08'
date_object = dt.strptime(date_string, '%Y-%m-%d')
print(date_object)

# 날짜를 문자열로 변환 obj.strftime()
date_object = dt.now()
date_string = date_object.strftime('%Y-%m-%d')
print(date_string)


import mod.utils as mu

dtnow = mu.get_dtnow()
print(dtnow)

'''

import os

# 현재 디렉토리 출력 
print(os.getcwd())

# 상위 디렉토리로 변경, 상대경로, 절대경로 
os.chdir("../")

#변경된 디렉토리 출력
print(os.getcwd())

# 파일목록 출력 
print(os.listdir())

# 폴더 삭제 
os.rmdir("new_directory")
print(os.listdir())

# 폴더 생성 
os.mkdir("new_directory")
print(os.listdir())
'''


import mod.utils as mu
import os

print(mu.get_curdir())

pname="python"
mu.os_mkdir(pname)
print(os.listdir())

os.rmdir(pname)
print(os.listdir())

import sys
print(sys.version)
print(sys.argv)

#stack

st =[]

#스펙에 값 넣기
st.append(1)
st.append(2)
st.append(3)
st.append(4)
st.append(5)

#스펙의 상태 확인
print(st) #[1,2,3]

#스펙에서 값 빼기
top = st.pop()
print(top) #
print(st) #
print(len(st)) #

# append, pop 이용한 queue

#빈 큐 생성
queue = []

#큐에 값 넣기
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)

#큐의 상태 확인
print(queue) #[1,2,3]

#큐에서 값 빼기
front = queue.pop(0)
print(front) #1
print(queue) #[2,3]
print(len(queue))


'''
print(dt.now())

# 문자열을 날짜로 변환
date_string = '2021-07-08'
date_object = dt.strptime(date_string, ''
'''