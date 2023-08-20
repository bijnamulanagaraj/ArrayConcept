class Student:
    def __init__(self,name,rollnum,marks):
        self.name = name
        self.rollnum = rollnum
        self.marks = marks
    def talk(self):
        print("Hello my name is:", self.name)
        print("My roll num is:", self.rollnum)
        print("My marks are:", self.marks)

S = Student("Nagaraj",1,550)
S.talk()