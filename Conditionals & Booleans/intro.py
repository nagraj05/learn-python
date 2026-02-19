# Comparisions:
# Equal: ==
# Not Equal: !=
# Greater than: >
# Less than: <
# Greater or Equal to : >=
# Less or Equal: <=
# Object Identity: is
#
# and
# or
# not

# language = "Java"

# if language == "Python":
#     print("Language is python")
# elif language == "Java":
#     print("Language is Java")
# else:
#     print("No match")
#


user = "Admin"
is_loggedin = True

# if user == "Admin" and is_loggedin:
#     print("Admin Page")
# else:
#     print("Invalid Credentials")

if not is_loggedin:
    print("Please log in")
else:
    print("Bad credentials")
