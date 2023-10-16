import functools
# user = {"username": "jose", "access_level": "guest"}
user = {"username": "jose", "access_level": "admin"}


def make_secure(acces_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] == acces_level:
                return func(*args, **kwargs)
            else:
                return f"No {acces_level} permission for {user['username']}"

        return secure_function

    return decorator


@make_secure("admin")
def get_admin_password():
    return "1234"


@make_secure("guest")
def get_billing_password():
    return "super_secure_password"


print(get_admin_password())
print(get_admin_password.__name__)
print("\n")
print(get_billing_password())
print(get_billing_password.__name__)