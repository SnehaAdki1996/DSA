#the single _ is the protected
#current & immediate derived are accessible for the protected one


class Student:
    _School_Name = 'D R M School' #protected

    def __init__(self, name, age):
        self._name=name  #protected
        self._age=age  #protected

    def _get_attr(self):
        print("From Base Class-------------")
        print(self._School_Name)
        print(self._name, self._age)


class College(Student):
    College_Name = 'SSWP'

    def __init__(self, name, age):
        super().__init__(name, age)

    def get_details(self):
        print("School Name:",self._School_Name)
        print("College Name:",self.College_Name)
        print("Other Details")
        self._get_attr()


s1= College('Sneha',20)
s1.get_details()



