'''
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

import pandas as pd

folder = "data/"
target = folder + "fktemp.csv"
df = pd.read_csv(target)

#rank 매기기
df["aver"]= df.postcode.rank(method="average")
print(df[["postcode", "aver"]])

df["dense"]= df.postcode.rank(method="dense")
print(df[["postcode", "dense"]])

df["first"]= df.postcode.rank(method="first")
print(df[["postcode", "first"]])

df["min"]= df.postcode.rank(method="min")
print(df[["postcode", "min"]])

df["max"]= df.postcode.rank(method="max", ascending=False)
print(df[["postcode", "max"]])

print(df[["postcode", "max", "first","dense", " aver"]])


#전치 컬럼-로우변환
print(df.transpose())

#누적 계산
print(df["postcode"].expanding.sum())

#내림차순 기준
print(df.postcode.idxmax(axis=0))
print(df.postcode.idxmin(axis=0))

#empty 추가
print(df.empty)
print(df.postcode.empty)

#검색
print(df.isin([48742]))
print(df.isin(["장상호"]))

#print(df.isin([48742, 12834]))
print(df.isin([48742,12834, "정상호"]))

#### 기간 계산

period = pd.period_range(start="2023-11-10 00:00:00", end="2023-11-10 02:30:00", freq="30T")
dt = {"col1":[1,2,3,4,5,6],"col2":period}
idx = ["row1","row2","row3","row4","row5","row6"]
pf = pd=DataFrame(data=dt, index=idx)
print(pf)

#인덱스
i = pd.date_range("2023-11-10", periods=10, freq="1H")

i = pd.date_range("2023-11-10", periods=10, freq="1H")
df = pd.DataFrame({"col1":[1,2,3,4,5,6,7,8,9,10]}, index=i)
print(df)

print("\n------------------------\n")

print(df.between_time(start_time="12:00", end_time="00:00"))


#시간간격 데이터 생성

i = pd.date_range("2023-11-10", periods=10, freq="3D")
#i = pd.date_range("2023-11-10", periods=10, freq="5D")
df = pd.DataFrame({'col1':[1,2,3,4,5,6,7,8,9,10]}, index=i)
print(df)

print(df.first("30"))

print(df.first("70"))

print(df.last("70"))

#코스피지수
import FinanceDataReader as fdr

ksp = fdr.DataReader("KS11", "2001")
print(ksp)
print("\n------------------------\n")

#최고가
#res = ksp["High"].max()
#print(res)

#res = ksp["High"].idxmax()
#print(res)

#최저가
#res = ksp["Low"].min()
#print(res)

#res = ksp["Low"].idxmin()
#print(res)

#최고가 
#res=ksp["Volume"].nsmallest(n=5)
#res=ksp["Close"].nsmallest(n=5)
res=ksp["Close"].nlargest(n=5)
print(res)

#kospi 3000 달성 최초일 찾기
cond = ksp["Close"] >= 3000
res=ksp[cond].index[0]
print(res)

res=ksp["Volume"]> kep["Volume"].shift()
print(res)

#위(shift) 값 참조, 처리
ksp["up"] != ksp["up"].shift().cumsum()
print(ksp)

#res=ksp["up"] != ksp["up"].shift().cumsum()
#print(res)

ksp["grp"].groupby(ksp["grp"].values).cumcount() + 1
print(ksp)

#연속 증가값 확인
ksp["up_cnt"]=ksp["grp"].groupby(ksp["grp"].values
#print(ksp)

print(ksp["up_cu"].max())
'''

#변환
import pandas as pd
 
target = "./data/apt.csv"

df = pd.read_csv(target, encoding="CP949")

df.to_csv("./data/apttt.csv", encoding="utf8")

print(df.head())


import pandas as pd

df = pd.read_csv("./data/apttt.csv", index_col=0)
print(df.head())

df.rename(columns={"분양가격(제곱미터)":"분양가"})
#print(df)
#print(df.dtypes)

df["분양가"]= df["분양가"].convert_dtypes()
#print(df.dtypes)

#array
arr = df.to_numpy()
print(arr)
#print(len(arr))

print(df.describe())
print(df.transpose())
print(df.T.head())























