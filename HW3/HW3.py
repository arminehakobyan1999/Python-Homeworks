class Car:
    def _init_(self, model, color, max_speed):
        self.model = model
        self.color = color
        self.max_speed = max_speed
    
    def compareCar(self, car2):
        if self.max_speed > car2.max_speed:
            print("car1 is better than car2")
        else:
            print("car2 is better than car1")


class Person:
    def _init_(name, last_name, age, gender, student, password):
        self.name = name
        self.last_name = last_name 
        self.age = age
        self.gender = gender
        self.student = student
        self.password = password
        
    @dec
    def Greeting(self, second_person):
        print("Welcome dear " + second_person.name)
        
    def Goodbye(self):
        print("Bye everyone!")
    
    def Favourite_num(self, num1):
        print("My favourite number is " + num1)
        
    def Read_file(self, filename):
        file_1 = open(filename + ".txt", encoding="utf8").read()
        print(file_1)
        
    def set_code(self, new_code):
        self.__password = new_code
    
    def get_code(self):
        return self.__password    

