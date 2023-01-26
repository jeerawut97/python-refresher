#1
name = "Bob"
print(f"Hello. {name}")

name = "Rolf"
print(f"Hello. {name}")

#2
name = "Bob"
print("Hello. {}".format(name))

name = "Rolf"
print("Hello. {}".format(name))

name = "Bob"
greeting = "Hello, {}"
with_name = greeting.format(name)
with_name2 = greeting.format("Rolf")
print(with_name)
print(with_name2)

#3
longer_phrase = "Hello, {}. Today is {}."
formatted = longer_phrase.format("Rolf", "Monday")
print(formatted)
