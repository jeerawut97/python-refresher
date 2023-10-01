# def named(**kwargs):
#     print(kwargs)

# named(name="Bob", age=25)

def named(name, age):
    print(name, age)

details = {"name": "Bob", "age": 25}

named(**details)

print('----------')

def print_nicely(**kwrgs):
    named(**kwrgs)
    for arg, value in kwrgs.items():
        print(f"{arg}: {value}")

print_nicely(name="Bob", age=25)

print('----------')

def both(*args, **kwagrs):
    print(args)
    print(kwagrs)

both(1, 3, 5, name="Bob", age=25)