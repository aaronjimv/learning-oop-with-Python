"""
@staticmethod and @classmethod are decorators 
used to define methods that belong to a class 
rather than an instance of that class.
"""
"""
A @staticmethod is a method that does not 
depend on the state of the object and can be
called without creating an instance of the class. 
It is defined using the @staticmethod decorator 
and takes no self parameter.
"""
"""
A @classmethod is a method that operates on the class
itself rather than on instances of the class. It is
defined using the @classmethod decorator and takes the
class itself as its first parameter, usually named cls.
"""

class MyClass:
    class_attribute = 7

    def __init__(self, color):
        self.color = color
    
    @staticmethod
    def static_method(color):
        print(f"This is a static method of color {color}")
    
    @classmethod
    def class_method(cls):
        print(cls.__name__)
        # print("This is a class method with the class attribute", cls.class_attribute)

my_class = MyClass("Yellow")
MyClass.static_method("Yellow")
MyClass.class_method()
