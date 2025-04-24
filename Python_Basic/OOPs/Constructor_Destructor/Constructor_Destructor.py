class Student:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
    
    def get_data (self):
        print(self.name)
        print(self.age)

    def __del__(self):
        print("Object Deletion")


s1 = Student('Sneha',30)
s1.get_data()
del s1