class Person:
    def __init__(self, name , last_name , age , gender, student: bool, password):
        try:
            assert type(name)==str
        except:
            print('The type of name needs to be string, but you inputed', type(name))
        self.name = name
        
        try:
            assert type(last_name)==str
        except:
            print('The type of last name needs to be string, but you inputed', type(last_name))
        self.last_name = last_name
        
        try:
            assert type(age)==int
        except:
            print('The type of age needs to be string, but you inputed', type(age))
        self.age = age
        
        try:
            assert type(gender)==str
        except:
            print('The type of name needs to be string, but you inputed', type(gender))
        self.gender = gender
        
        try:
            assert type(student)==bool
        except:
            print('The type of student needs to be boolean, but you inputed', type(student))
        self.student = student
        
        self.__password = password
    
    def Greeting(self, second_person):
        print("Welcome dear", second_person.name)
    
    def Goodbye(self):
        print("Bye everyone!")
    
    def Favourite_num(self, num1:int):
        return ("My favourite number is: " + str(num1))
    
    def Read_file(self, filename):
        try:
            f = open((filename + ".txt"), "r")
            print(f.read())
        except FileNotFoundError:
            print("Please double check, I think the file doesn't exist")
        
    def Set_password(self, new_password):
        self.__password = new_password
    
    def Get_password(self):
        return self.__password

person_1 = Person("Armien", "Hakobyan", 22, "F", False, "Asdewq**9090")
person_2 = Person("Ani", "Grigoryan", 25, "F", False, "oplkj^^32")
person_1.Greeting(person_2)
person_2.Goodbye()
person_1.Favourite_num(1)
person_1.Read_file("txt_file")
person_1.Read_file("text")
person_1.Get_password()
person_1.Set_password("o")