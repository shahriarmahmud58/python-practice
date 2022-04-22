class animal :
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def walk (self):
        print(self.name + "walks")

class dog(animal):
    def __init__ (self,name,age):
        super()
        
        