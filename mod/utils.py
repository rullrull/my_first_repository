import math
import random
from datetime import datetime as dt
import os

def mt_sqrt(x) :
    return math.sqrt(x)

def mt_sinpi() :
    return math.sin(math.pi /2)

def mt_elog() :
    return math.log(math.e)

def mt_exp(x) :
    return math.exp(x)

def mt_pi() :
    return math.pi

def rd_int(x, y) :
    return random.radint(x, y)

def rd_list(this) :
    return random.radint(this)

def rd_rd() :
    return random.random()

def rd_nmvar() :
    return random.normalvariate(0, 1)

def get_dtnow() :
    return dt.now()

def cvt_time2str(objtime) :
    return dt.strptime(objtime, "%Y-%m-%d")

def cvt_str2time(strtime) :
    return dt.strftime("%Y-%m-%d")

def get_curdir() :
    return os.getcwd()

def get_mkdir(pname) :
    return os.mkdir(pname)


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
'''
#=================================
