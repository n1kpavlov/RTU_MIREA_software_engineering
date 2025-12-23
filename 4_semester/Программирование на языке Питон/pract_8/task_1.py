class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._protected_attr = "protected"
        self.__private_attr = "private"

    def greet(self):
        print(f"Hello, my name is {self.name}!")

    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy birthday! Now I'm {self.age} years old.")

    def __hidden_method(self):
        print("This is a private method")


#1.1
print('#1.1')

def print_object_fields(obj):
    print([attr for attr in dir(obj) if not attr.startswith('__')])

person = Person('Nikita', 19)
print_object_fields(person)


#1.2
print('\n#1.2')

def call_method_by_name(obj, method_name):
    getattr(obj, method_name)()

call_method_by_name(person, 'greet')


#1.3
class A:
    pass

class B(A):
    pass

class C(B):
    pass


#1.4
print('\n#1.4')

get_inheritance = lambda cls: ' -> '.join(c.__name__ for c in cls.__mro__)

print(get_inheritance(C))