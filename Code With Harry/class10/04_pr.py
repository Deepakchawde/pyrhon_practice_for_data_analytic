# WAP to make a class and capable ot print dquare , cube and square root

class calculator():
    def __init__(self, num):
        self.number = num

    def square(self):
        print(f"the square of {self.number} is {self.number**2}")

    def cube(self):
        print(f"cube of the number {self.number} is {self.number**3}")
        
    def squareroot(self):
        print(f"square root of the number {self.number} is {self.number**0.5}")

    @staticmethod
    def greet():
        print(f"good evening every one welcome ot the best calculator in the world")
a= calculator(9)
a.square()
a.cube()
a.squareroot()
a.greet()