#by default all access specifier are public


class Student:
    School_Name = 'D R M School'

    def __init__(self, name, age):
        self.name=name 
        self.age=age 

    def get_attr(self):
        print("From Base Class-------------")
        print(self.School_Name)
        print(self.name, self.age)


class College(Student):
    College_Name = 'SSWP'

    def __init__(self, name, age):
        super().__init__(name, age)

    def get_details(self):
        print("School Name:",self.School_Name)
        print("College Name:",self.College_Name)
        print("Other Details")
        self.get_attr()


s1= College('Sneha',20)
s1.get_details()



