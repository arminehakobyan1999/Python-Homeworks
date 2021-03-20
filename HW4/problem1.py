class Calculation:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def addition(self):
        return self.x + self.y
    
    def subtraction(self):
        return self.x - self.y
    
class MyCalculation(Calculation):
    
    def __init__(self, x, y):
        super().__init__(x, y)
    
    def multiplication(self):
        return self.x * self.y
    
    def division(self):
        return self.x/self.y

M_c = MyCalculation(3, 5)
print(M_c.addition())
print(M_c.subtraction())
print(M_c.multiplication())
print(M_c.division())


