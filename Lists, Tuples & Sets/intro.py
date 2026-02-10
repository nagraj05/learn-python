courses = ["History", "Maths", "Physics", "ComputerSci"]
courses_2 = ["Biology", "Paleontology"]
print(len(courses))
# courses.insert(2, "Art")
# courses.insert(0, courses_2)
courses.extend(courses_2)
print(courses)
courses.remove("Maths")
courses.reverse()
# courses.sort()
sourted_course = sorted(courses)
print(sourted_course)
