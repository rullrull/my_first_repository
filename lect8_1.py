'''
#cls, self

class MyClass :
    count = 0
    
    def __init__(self, num):
        self.count = num
    
    @classmethod
    def clasMEthod(cls):
        cls.count += 1
        print(f"cls count = {cls.count}")
        
    def instMethod(self):
        self.count += 1
        print(f"instance ={self.count}")
        
MyClass.clsMethod()

obj = MyClass(10)

obj.instMethod()
print(obj.count)

print(MyClass.count)
print(MyClass.count)


class Champion:
    Iv = 1
    movSpd = 0
    basicMovSpd = 325
    atkSpd = 0.658
    
    def __init__(self, chmpNam, speed):
        self.hp =100
        self.chmpNam = chmpNam
        self.level =1
        self.setSpeed(speed)
        self.setAtkSpd()
        self.setMovSpd()
        
    def setAtkSpd(self):
        self.atkSpd =0.658*((1.0334)**(Champion.Iv - 1))
        
    def beAtk(self, dem):
        print("be attack", dem.. 1-100.0/(100.0+100))
        self.dem = dem*(100.0/(100.0+100))
        print(self.dem)
        self.hp = self.hp-self.dem
        
    def setSpeed(self, sp):
        if(sp ==1):
            self.speed = 50
        else:
            self.speed = 0
            
            
    def setMovSpd(self):
        print("set Mov Spd")
        self.movSpd = (20 + self.speed)*(1.00)*(100)
        
    def printStatus(self):
        print("campNam:%s, hp:%f, Iv%d, mvSpd%f, atkSpd%f" % (self.chmpNam, self))
        
ashe=Campion("ashe", 474.0)
mipo = Cmpion("mipo", 520.0)

ashe.printStatus()
mipo.printStatus()

mipo.beAtk(63.0)
mipo.printStatus()
'''
'''
class Campion :
    def __init__(self, name) :
        self.name = name
        self.level = 1
        
class Yasuo(Champion) :
    def getName(self):
        print(self.name)
        
    def attck(self, key):
        print(f"attack = {key}")
        
    def levelup(self):
        self.level += 1
        
    def getLevel(self):
        print(self.level)
        
user1 = Tasuo("pyhon")
user2 = Garen("hello")

user1.getName()
user1.getLevel()

user2.getName()
user2.getLevel()
        
        
        
class Champion:
    def __init__(self, name):
        self.name = name
        self.level = 1
        
    def getName(self) :
        print(self.name)
        
    def attck(self, key):
        print(f"attack = {key}")
        
    def levelup(self):
        self.level +=1
        
    def getLevel(self) :
        print(self.level)
        
class Yasuo(Champion) : 
    def attck(self, key):
        print(f"attack - {key} steel tempest")
        return
class Garen(Champion) : 
    def attck(self, key):
        print(f"attack - {key} demacian justice")
        return
    
user1 = Yasuo("pyhon")
user2 = Garen("hello")  

user1.getLevel()
user2.getLevel()

user1.attck("q")
user2.attck("r")

user1.levelup()
user2.levelup()

user1.getLevel()
user2.getLevel()
 '''
 
 from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


circ = Circle(5)
rect = Rectangle(4, 6)

print(circ.area())
print(rect.area())

sett = [circ, rect]
for st in sett :
    print(st.area())
    
    
#정보은닉

class Person:
    def __init__(self, name, age, num):
        self._name = name
        self._age = age
        self._number = num

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    def number(self):
        return self._number

    @name.setter
    def name(self, new):
        self._number = new

    @age.setter
    def age(self, nAge):
        self._age = nAge
        
user1= Person("Alice", 30, "01011112222")

print(user1.age)
print(user1._age)
print(user1.name)
print(user1._name)
print(user1.number)
print(user1._number)

user1._age = 21
user1.age = 23
print(user1.age)