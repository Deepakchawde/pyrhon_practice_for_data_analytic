# WAP to create a class rogrammer for storing information of few programmer workkinh at microsoft

class programmer():
    company="Microsoft"

    def __init__(self, name, unit):
        self.name= name
        self.unit= unit

    def getinfo(self):
        print(f"the name of the programmeris {self.name} and the unit he was working is {self.unit}")


deepak=programmer('deepak','paint')
deepak.getinfo()


