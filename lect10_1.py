
'''
#dataframe

import pandas as pd

df = pd.DataFrame([["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]])
print(df)
print("\n------------------\n")

print(df[1])
print("\n------------------\n")

print(df[1][1])
print("\n------------------\n")



#dataframe 

import pandas as pd

data = {
    "x" : [10, 15, 20],
    "y" : [50, 55, 60],
    "z" : [100, 110, 120]
}

idx = ["x축", "y축", "z축"]

fr = pd.DataFrame(data, index=idx)

print(fr)

#print(fr["x"])

#print(fr.x)
#print("\n------------------\n")

#print(fr.iloc[2])

#print("\n------------------\n")
#print(fr.loc["y축"])

#print("\n------------------\n")

#열추가
#frs =pd.DataFrame(fr,columns=["x","y","z","t"])
#print(frs)

#frs["t"] = [60,120,180]
#print(frs)

#행수정
#print("\n------------------\n")
#frs.loc["t축"]=[500,600,700,800]
#print(frs)

#print("\n------------------\n")
#frs.drop("x" axis=1, inplace=True)
#print(frs)

#print("\n------------------\n")
#frs.dropp("x축", inplace=True)
#print(frs)



#칼럼추가

import pandas as pd

dt = [[1,10,100],[2,20,200],[3,30,300]]
col = ["x","y","z"]
idx = ["x축","y축","z축"]

#col=["col1","col2","col3"]
#idx=["row1","row2","row3"]
df = pd.DataFrame(data=dt,index=idx,columns=col)

print(df)
#print(df["col1"])
#print(df["y"])

print("\n------------------\n")
#print(df["현대"])
#print(df["y축"])

#print(df["col1"])

print("\n------------------\n")
#print(df+1)

# 같은 인덱스끼리 연산
dt2  = [[0],[2],[3]]
df2 = pd.DataFrame(data=dt2,index=["삼성","현대","LG"],columns=["y"])

df.div(df2)

print("\n------------------\n")
#print(df.div(df2))
print(df.mul(df2))

print("\n------------------\n")
print(df.div(df2, fil1_value=100))

print(df.div(100))
#print(df / 100)
#print("\n------------------\n")

#print(df.mul(100))
#print(df*100)


#멀티인덱스

import pandas as pd

idx = [('row1', 'val1'), ('row1', 'val2'), ('row2', 'val1'), ('row2', 'val2'), ('row2', 'val3'), ('row3', 'val2'),('row3', 'val3')]
dt = [ [1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18], [19,20,21]]

ind = pd.MultiIndex.from_tuples(idx)
df = pd.DataFrame(dt, columns=['col1', 'col2', 'col3'], index = ind)

print(df)

print("\n------------------\n")
print(df.loc["row3"])
print(df.loc[0])

print("\n------------------\n")
print(df.loc[("row3","val3")])

print("\n------------------\n")
print(df.loc[("row3", "val2"),"col1"])

print("\n------------------\n")
print(df.loc[(1, "val2"), "col1"])

#랜덤 데이터 생성

import numpy as np
import pandas as pd

dt = np.random.randint(10, size=(5, 5))
df = pd.DataFrame(data=dt)

print(df)
print("\n------------------\n")
print(df[2])

print("\n------------------\n")
print(df.loc[2])

print("\n------------------\n")
print(df.loc[3][1])

print("\n------------------\n")
print(df.head(3))

print("\n------------------\n")
print(df.tail(2))

print("\n------------------\n")
print(df.sample(1))
print("\n------------------\n")
print(df.sample(3))


#테스트 파일 생성

from faker import Faker as fk
import os

#temp = fk()
temp = fk("ko-KR")
print(temp.name())

folder="data/"
if not os.path.isdir(folder):
    os.mkdir(folder)
    
with open(folder + "fktemp.csv", "w", encoding='utf8') as f :
    f.write("name,address,postcode,company,job,phone,email,id,ip_prv,ip_pub,catch_parase,color\n")

with open(folder + "fktemp.csv", "w", newline='', encoding='utf8') as f :
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
            temp.color_name() + "\n")


#파일열기
import pandas as pd

folder = "data/"
target = folder + "fktemp.csv"

df = pd.read_csv(target)

#print(df)
print(df.values[0])


#인덱스 설정 확인

print(df.index)

print(df.dttpes)


#print(type(df))

print("\n-----------------\n")
print(df.head())
print("\n-----------------\n")

print(df.head(3))
print("\n-----------------\n")

print(df.tail())
print("\n-----------------\n")

print(df.tail(3))
print("\n-----------------\n")

print(df.sample())
print(df.sample(4))


#print(df.values)
print("\n-----------------\n")
#print(df.values[24])

#for el in df.values[12]:
#    print(el)
    
#print(df.info())
#print(df.isnu11())
#print(df.isnu11().sum())

#print(df["name"])
#print(df["color"])
#print(df["postcode"])
#print(df["phone"])
#print(df["id"])
#print(df["ompany"])

#print(df["name","id"])
#post = df[["name","address","postcode"]]
#print(post)

#print(df.postcode.describle())
#print(df.color.describe())

#print(df.color.count())
#print(df.color.value_counts())

#print(df.name == "이민석")

temp = df[df.color=="Beige"].head(1)
#temp = df[df.color=="Beige"].head(2)
print(temp)

'''