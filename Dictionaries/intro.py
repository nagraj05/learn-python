student = {"name": "Nagraj", "age": 29, "courses": ["Maths", "Physics"]}
student["phone"] = "9348217080"
student.update({"name": "Nagrajjjj"})
# del student["age"]
# print(student["courses"])

# print(student.get("age"))
# print(student.get("test", "Not Found"))
# print(student)


# print(student.keys())
# print(student.values())
# print(len(student))
# print(student.items())

for key, value in student.items():
    print(key, value)
