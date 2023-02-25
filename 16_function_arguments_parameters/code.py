def add(x, y):
    result = x + y
    print(result)

def say_hello(name, surname):
    print(f"Hello, {name} {surname}")

def divide(dividend, divisor):
    if divisor != 0:
        print(dividend / divisor)
    else:
        print("You fool!")

add(5, 3)
say_hello("FOOK", "J")
say_hello(surname="FOOK", name="J")
divide(20, 1)