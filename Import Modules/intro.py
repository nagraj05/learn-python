# import my_module as mm
# import sys
import os

from my_module import find_index

courses = ["History", "Maths", "Computer Science"]

index = find_index(courses, "Maths")
print(index)


test = "test String"
index1 = find_index(test, "t")
print(index1)

# print(sys.path)
print(os.__file__)
