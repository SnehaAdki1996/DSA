class Member:
    def __init__(self,member_id,member_name) -> None:
        self.mem_id = member_id
        self.mem_name = member_name

    def get_details(self):
        print(self.mem_id,self.mem_name)


m1 = Member(12,'sneha')
print(vars(m1))
print(dir(m1))


# vars(m1)
# {'mem_id': 12, 'mem_name': 'sneha'}

# dir(m1)
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'get_details', 'mem_id', 'mem_name']


