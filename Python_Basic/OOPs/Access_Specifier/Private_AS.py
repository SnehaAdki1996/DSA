#the double __ is the protected
#current are accessible for the private members
#private members are not inhertiated

class Student:
    __School_Name = 'D R M School' #private

    def __init__(self, name, age):
        self.__name=name  #protected
        self.__age=age  #protected

    def _get_attr(self):
        print("From Base Class we can access the private data members-------------")
        print(self.__School_Name)
        print(self.__name, self.__age)


class College(Student):
    College_Name = 'SSWP'

    def __init__(self, name, age):
        super().__init__(name, age)

    def get_details(self):
        print("College Name:",self.College_Name)
        print("Other Details")
        self._get_attr()


s1= College('Sneha',20)
s1.get_details()
