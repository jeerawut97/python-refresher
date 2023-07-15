def multiply(*args):
    total = 1
    for arg in args:
        total = total * arg
    
    return total

def add(x, y):
    return x + y

def apply(*args, operator):
    if operator == "*":
        return multiply(args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."

print(multiply(1, 3, 5))
print(add(*[1, 2]))
print(apply(*[1, 2, 3], operator="*"))
print(apply(1, 2, 3, operator="+"))
print(apply(1, 2, 3, operator="-"))
