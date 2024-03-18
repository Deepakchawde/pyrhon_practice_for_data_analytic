class railway():
    def __init__(self,name,number, set):
        self.name=name
        self.number=number
        self.set= set

    def ticket(self):
        print(f"The name of the train is {self.name}")
        
    def status(self):
        print(f"the status of the train  is  {self.set}")

    def getfare(self):
        print(f"the fair train number is {self.number}")

intercity = railway("Duronn", 41245,45)
intercity.ticket()
intercity.status()
intercity.getfare()