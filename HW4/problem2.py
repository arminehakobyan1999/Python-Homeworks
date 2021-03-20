class My_Time:
    def __init__(self, t):
        self.t = t
    def printTime(self):
        print("The current time is", self.t)

class My_Date:
    def __init__(self, d):
        self.d = d
    def printDate(self):
        print("The current date is", self.d)
        
class Date_Time(My_Date, My_Time):
    def __init__(self, d, t):
        My_Date.__init__(self, d)
        My_Time.__init__(self, t)


D_t = Date_Time("13.10.1997", "12 PM")
D_t.printTime()
D_t.printDate()

