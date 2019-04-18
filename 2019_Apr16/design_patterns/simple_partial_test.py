def default_username(fn):
    def wrapper(*args, **kwargs):
        return fn("John", *args, **kwargs)
    return wrapper

@default_username
def add(username, role, dept):
    print("Adding username = {}, role = {}, dept = {}".format(username, role, dept))

@default_username
def modify(username, data):
    print("Modifying {} for username = {}".format(data, username))

@default_username
def remove(username):
    print("Removing", username)


add("Admin", "IT")
modify("sdfsfsdf")
remove()

#add("John", "Admin", "IT")
#modify("John")
#remove("John")