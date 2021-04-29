# inheritance

# class Animal:
# class Fish(Animal):

# you know the rest!

# NOTE: all class inherit from object class

# issubclass(Fist, object) is true => directly/indirectly

# in subclass, needa call parents contructor first using super() but you can put the super at the bottom unlike in Java >>>

# def __init__(self):
# self.weight = 2
# super().__init__()

# ****************************

# python supports multiple inheritance >>>
# class Manager(Employee, Person)

# ****************************

from collections import namedtuple
from abc import ABC, abstractmethod


class Stream(ABC):
    @abstractmethod
    def read(self):
        pass

# cannot instantiate this class cause it's an abstract class
# classes which derive from this class needa implement the abstract method

# ****************************
# extending built-in types


class Text(str):
    def duplicate(self):
        return self + self


text = Text("Python")
text.duplicate()

# another example >>>


class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)


list = TrackableList()
list.append("1")
# ****************************

# data classes
# note: namedtuples are immutable
# from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])

p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)

p1 == p2
# will be True even without implementing the __eq__ magic method
