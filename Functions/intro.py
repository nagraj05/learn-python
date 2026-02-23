def hello_func(greeting, name="Nagraj"):
    return f"{greeting} {name}"


# hello_func()
# hello_func()
# hello_func()
# print(hello_func)
print(hello_func("Hi", "Roy"))


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


courses = ["Math", "physics"]
info = {"name": "Nagraj", "age": 29}
student_info(*courses, **info)
