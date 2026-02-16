courses = ["History", "Maths", "Physics", "ComputerSci"]
courses_2 = ["Biology", "Paleontology"]
# print(len(courses))
# courses.insert(2, "Art")
# courses.insert(0, courses_2)
# courses.extend(courses_2)
# print(courses)
# courses.remove("Maths")
# courses.reverse()
# courses.sort()
# sourted_course = sorted(courses)
# print(sourted_course)
# courses.sort()
# print("sorted- courses", courses)

# courses.insert(1, courses_2)
# print(courses)

# num = [67, 99, 56, 34, 900]
# num.sort()
# print(num)
# print(min(num))
# print(max(num))
# print(sum(num))

# print("Art" in courses)
# print("Maths" in courses)

# for index, item in enumerate(courses, start=1):
#     print(index, item)
#

# course_string = "-".join(courses)
# new_list = course_string.split("-")
# print(new_list)

# tuple_1 = ("History", "Geography", "Physics")
# tuple_2 = tuple_1

# tuple_1[0] = "test"
# print(tuple_1)
# print(tuple_2)


new_sets = {"History", "Math", "Physics", "Compsci", "Math"}
new_sets_1 = {"History", "Math", "Art", "Compsci", "zone"}

print(new_sets.intersection(new_sets_1))
print(new_sets.difference(new_sets_1))
print(new_sets.union(new_sets_1))
