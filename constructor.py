class data:
    name="muskan"
    age=20
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(f"the name is {self.name} and the age is {self.age}")
    def info(self):
        print(f"the name is {self.name}")   

a=data("shlok",17)
b=data("yash",100)
a.name="shlok"
a.age=17
b.name="yash"
b.age=100
a.info()
b.info()