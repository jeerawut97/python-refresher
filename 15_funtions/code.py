def hello():
    print("Hello!")

def user_age_in_seconds():
    user_age = int(input("Enter your age: "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age in seconds is {age_seconds}.")

friends = ["Rolf", "Bob"]
def add_friend():
    friend_name = input("Enter your friend name: ")
    friends.append(friend_name)
    print(friends)

# hello()
# user_age_in_seconds()
add_friend()
add_friend()
add_friend()