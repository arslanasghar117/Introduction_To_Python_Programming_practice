class parent:
    def __init__(self):
        print("this is parent class")

    def parentfunction(self):
        print("this is parent function")

p = parent()

class child(parent):
    def __init__(self):
        print("this is the child class")
    
    def childfunction(self):
        print("this is the child function")

c = child()


c.parentfunction()
c.childfunction()