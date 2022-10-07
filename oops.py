class person:
    pass

p = person()
print(p)

class person:
    def getname(self):
        print("arslan")
    def getage(self):
        print("32")

p = person()
p.getname()
p.getage()

class person2():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def getName(self):
        print("your name is " + self.name)
    def getAge(self):
        print("your age is " + self.age)

p1 = person2("arslan", "31")
p1.getName()
p1.getAge()