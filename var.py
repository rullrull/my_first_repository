my_var = 10
print(my_var)
my_list = [1, 2, 3]
print(*my_list)

#정수
my_int = 10
#부동 소수점
my_float = 3.14
#복소수
my_complex = 3 +4j

my_character = 'A'
my_char = "@"

my_string ='Hello, Wold!'
str_name = "python"

my_bool = True
bFlag = False

my_list = [1, 2, 'three', True]
lsElement = [3.14, "b", 'two', False]

my_list = [10, 3, 8, 9, 42, "hello"]

my_list = [10, 3, 8, 9, 42, 8, "hello"]
print(my_list)

print(my_list.__len__())

my_list = [10, 3, 8, 9, 42, "hello"]
print(my_list)

print(my_list[3])

my_list = [10, 3, 8, 9, 42, "hello"]
print(my_list)

print(my_list[3])

list_el = my_list[2]

print(list_el)

my_list = [10, 3, 8, 9, 42, "hello"]
print(my_list)

my_list[3] = 11

print(my_list)

my_list = [10,3, 8, 9, 42, "hello"]
print(my_list)

n_add = my_list[3] + my_list[2]
print(n_add)

my_list = [10, 3, 8, 9, 42, "hello"]
print(my_list[2:5])

my_list = [10, 3, 8, 9, 42, "hello"]
print(my_list[:3])

my_list = [10, 3, 8, 9, 42, "hello"]
print(my_list[0:3])

my_list = [10, 3, 8, 9, 42, "hello"]
print(my_list[4:])

my_list = [10, 3, 8, 9, 42, "hello", [5, 4, 2, "world"]]
print(my_list)
print(my_list[6][1])

my_list = [10, 3, 8, 9, 42, "hello", [5, 4, 2, "world"]]
print(my_list)
print(my_list[6][2:])

my_list = [10, 3, 8, 9, 42, 8, "hello"]
print(my_list)

my_list.insert(2, 4)

print(*my_list)

my_list = [10, 3, 8, 9, 42, "hello"]
print(my_list.index(3))

my_list = [10, 3, 8, 9, 42, 8, "hello"]
print(my_list)

my_list.append(22)
print(*my_list)

my_list =[10, 3, 8, 9, 42, 8, "hello"]
print(my_list.count(8))

my_list = [10, 3, 8, 9, 42, 8, "hello"]

print(my_list)
print(my_list.pop())
print(*my_list)

my_list = [10, 3, 8, 9, 42, 8]

print(my_list)
my_list.sort()

print(*my_list)

my_list = [10, 3, 8, 9, 42, 8, "hello"]
print(my_list)
my_list.sort()

print(*my_list)

my_list =[10, 3, 8, 9, 42, 8, "hello"]

print(my_list)
my_list.reverse()

print(*my_list)

my_list = [10, 3, 8, 9, 42, 8, "hello"]
list_tmp = [5, 7, "world"]

print(my_list, list_tmp)
my_list.extend(list_tmp)
print(*my_list)
list_tmp.clear()
print(list_tmp)

my_list = [10, 3, 8, 9, 42, 8, "hello"]
print(my_list)

my_list.remove(3)
print(*my_list)

my_tuple = (1, 2, 'three', True)
tpItem = (3.14, "b" , 'two', False)

my_tup =(4, 2, 6, 1, "py", "w")

my_tup = (4, 2, 6, 1, "py", "w")
print(my_tup)
print(my_tup[2])
print(*my_tup)

my_tup = (4, 2, 6, 1, "py", "w")
print(my_tup)
print(my_tup[2])
my_tup[3] = 2
print(*my_tup)

my_tup = (4, 2, 6, 1, "py", "w")
print(my_tup)
print(my_tup[2] + my_tup[0])
print(*my_tup)

my_tup = (4, 2, 6, 1, "py", "w")
print(my_tup)
n_add = my_tup[1] + my_tup[3]
print(n_add)

my_tup = (4, 2, 6, 1, "py", "w")
print(my_tup.index(2, 0, 3))

my_tup = (4, 2, 6, 1, "py", "w")
print(my_tup.index("py", 3, 5))

my_tup = (4, 2, 6, 1, "py", "w")
print(my_tup.index(1, 0, 3))

my_dict = {'key1': 'value1', 'key2': 'value2'}
dicData = {"name" : "pyhon", "number" : 23564897}

my_dict = {'key1' : 'value1', 'key2': 'value2'}
my_item = my_dict.items()
print(my_item)

idx = ("key1", "key2", "key3")
dicts = dict.fromkey(idx, "0")
print(dicts)

my_dict = {'key1' : 'valuel1', 'key2' : 'value2'}
my_str = {"name" : "python", "number" : 23564897}

print(my_dict["key1"])

my_dict = {'key2': 'value1', 'key2': 'value2'}

my_str = my_dict.get("key2")

print(my_str)

my_dict = {'key1': 'value1', 'key2': 'value2'}

print(my_dict.pop("key1"))
print(my_dict)

my_dict = {'key1': 'value1', 'key2': 'value2'}
dicts = my_dict.copy()
print(dicts)
print(my_dict)

my_dict = {'key1' : 'valuel1', 'key2' : 'value2'}
my_str = {"name" : "python", "number" : 23564897}
my_dict["key3"] = "value3"
print(my_dict)

my_dict = {'key1' : 'valuel1', 'key2' : 'value2'}
my_dict.setdefault("key3")
print(my_dict)

my_dict = {'key1' : 'valuel1', 'key2' : 'value2'}
my_dict.update({"key1" : "v4"})
print(my_dict)

my_dict = {'key1' : 'valuel1', 'key2' : 'value2'}
del my_dict["key2"]
print(my_dict)    

my_dict = {'key1' : 'valuel1', 'key2' : 'value2'}
print("key2" in my_dict)
print("key3" in my_dict)     

my_dict = {'key1' : 'valuel1', 'key2' : 'value2'}
my_list = list(my_dict.keys())
print(my_list)

my_dict = {'key1' : 'valuel1', 'key2' : 'value2'}
my_set = set(my_dict.keys())
print(my_set)

my_dict = {'key1' : 'valuel1', 'key2' : 'value2'}
my_dict.clear()
print(my_dict)

my_set = {5, 8, 3, 7, 1, "h"}

my_set = set([5, 8, 3, 7, 1, "h"])
print(my_set)

set_tmp = set("hello")
print(set_tmp)

my_set = {5, 8, 3, 7, 1, "h"}
set_item = {7, 8, 4, 2, "h"}

print(my_set | set_item)

my_set = {5, 8, 3, 7, 1, "h"}
set_item = {7, 8, 4, 2, "h"}

# print(my_set | set_item)

print(my_set.union(set_item))

my_set = {5, 8, 3, 7, 1, "h"}
set_item = {7, 8, 4, 2, "h"}

print(my_set | set_item)
print(my_set - set_item)

my_set = {5, 8, 3, 7, 1, "h"}
set_item = {7, 8, 4, 2, "h"}

print(my_set | set_item)

#print(my_set - set_item)

print(my_set.difference(set_item))

my_set = {5, 8, 3, 7, 1, "h"}
set_item = {7, 8, 4, 2, "h"}

print(my_set | set_item)
print(my_set & set_item)

my_set = {5, 8, 3, 7, 1, "h"}
set_item = {7, 8, 4, 2, "h"}

print(my_set | set_item)

# print(my_set & set_item)

print(my_set.intersection(set_item))

my_set = {5, 8, 3, 7, 1, "h"}

print(my_set)
my_set.add(9)
print(my_set)

my_set = {5, 8, 3, 7, 1, "h"}
print(my_set)
my_set.update([5, 9, 7, 4])
print(my_set)

my_set = {5, 8, 3, 7, 1, "h"}
print(my_set)
my_set.clear()

my_set = {5, 8, 3, 7, 1, "h"}
print(my_set)
my_set.remove(5)

my_set = {5, 8, 3, 7, 1, "h"}
print(my_set)
my_set.discard(2)
print(my_set)

my_set = {5, 8, 3, 7, 1, "h"}
set_item = {7, 8, 4, 2, "h"}
print(my_set)
my_set.difference_update(set_item)
print(my_set)

my_int = 10
my_str = str(my_int)

my_int = 10
print(my_int)
print(my_int + 10)

my_int = 10
print(my_int)
print(my_int + 10)
my_str = str(my_int)
print(my_str)

my_int = 10
print(my_int)
print(my_int + 10)
my_str = str(my_int)
print(my_str)
print(my_str + 10)

my_int = 10
print(my_int)
print(my_int + 10)
my_str = str(my_int)
print(my_str)
print(my_str + "hello")

my_str = '10'
my_int = int(my_str)

my_int = '10'
print(my_int)
my_int = int(my_str)
print(my_int)

my_int = '10'
print(my_int)
my_int = int(my_str)
print(my_int)
print(my_int + 10)

my_int = '10'
print(my_int)
my_int = int(my_str)
print(my_int)
print(my_int + 10)
my_int2 = int("ten")
print(my_int2)
         