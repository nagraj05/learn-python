from select import select

message = "test"
print(message)
print(len(message))
print(message[0:-1])
print(message[1:])
print(message.lower())
print(message.upper())
print(message.count("t"))
print(message.find("t"))
replacedmessage = message.replace("test", "oh boy")
print(replacedmessage)

name = "Nagraj"
greetings = "Hello"

new_greetings = f"{greetings}!{name.upper()}"
print(new_greetings)

print(dir(name))

print(help(str))
