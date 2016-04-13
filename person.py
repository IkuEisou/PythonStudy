#Person.py

class Person:
    """
     Class to represent a person
    """
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 0 < age <= 150:
            self.__age = age

    def __str__(self):
        return "Person('%s', %s)" % (self.__name, self.__age)

    def __repr__(self):
        return str(self)
