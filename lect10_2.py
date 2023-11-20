
'''

import pandas as pd

folder = "data/"
target = folder + "fktemp.csv"

df = pd.read_csv(target)

#print(df.name == "김병철")
print(df.company == "박박정")



temp = df[df.postcode > 70000]
print(temp)

temp = df[df.postcode>70000].head(3)
print(temp)

res = df[df.postcode>70000][["name", " postcode", "address"]]
print(res)
print(res.count())

#temp=df.postcode.mean()
#temp = df.postcode.sum()
#print(temp)

#temp = df[df.color =="Ivory"].postcode.sum()
#print(temp)

#temp = df[df.postcode > df.postcode.mean()][["name", "postcode"]]
#temp = df[df.postcode>df.postcode.mean()]
print(temp)

#temp = df[df.postcode.isnull()]
#temp = df.name.empty
temp = df[df.company.isnull()][["name", "postcode"]]
print(temp)

temp = df.company.isnull()
    for el in temp :
        if el ==True :
            print(el)
            
#temp = df.name.empty
#temp = df[df.company.isnull()][["name", "postcode"]]
#print(temp)

#temp = df[(df.color == "Ivory")]
#temp = df[~(df.color == "Ivory")]
temp = df[~(df.color == "Ivory")][["name"]]
#print(temp.count())
print(temp.color.count())

#temp = df[(df.color == "Ivory")]&(df.postcode > 70000)]
#temp = df[(df.color == "Ivory")]|(df.postcode > 70000)]
#temp = df[(df.color == "Ivory")]|(df.postcode > 70000)][["name"]]
#print(temp)

#temp = df.sort_values("postcode")
#temp = df.sort_values("postcode", ascending=False)
#temp = df.sort_values("name", ascending=False)
print(temp)

#pivot, 데이터 재배열

import pandas as pd

col = ['Machine','Country','Price','Brand']
data = [['TV','Korea',1000,'A'],
        ['TV','Japan',1300,'B'],
        ['TV','China',300,'C'],
        ['PC','Korea',2000,'A'],
        ['PC','Japan',3000,'E'],
        ['PC','China',450,'F']]
df = pd.DataFrame(data=data, columns=col)
print(df)

print("\n------------------\n")
#print(df.pivot(index='Machine',columns='Country',values='Price'))
#print(df.pivot(index='Brand',columns='Machine',values='Price'))
#print(df.pivot(index='Country',columns='Machine',values='Price'))
#print(df.pivot(index='Price',columns='Brand',values='Machine'))


'''



