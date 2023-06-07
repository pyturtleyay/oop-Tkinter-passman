def readUsers():
    f = open("UsersList.txt", 'r')
    users = f.readlines()
    results = {}
    for user in users:
        tempVariable = user.strip("\n").split(",")
        username = tempVariable[0]
        password = tempVariable[1]
        results[username] = password
    f.close()
    return results
def passwordCheck(password):
    password_length = len(password)
    if password_length < 8:
        raise RuntimeError("The password is too short.")
    if password_length > 32:
        raise RuntimeError("The password is too long.")
    if " " in password:
        raise RuntimeError("Password can't contain space.")
    if "," in password:
        raise RuntimeError("Password can't contain a ','.")
    return True
def usernameCheck(username):
    username_length = len(username)
    if username_length < 8:
        raise RuntimeError("Username too short.")
    if username_length > 25:
        raise RuntimeError("Username too long.")
    if " " in username:
        raise RuntimeError("Username can't contain space.")
    if "," in username:
        raise RuntimeError("Username can't contain ','.")
    return True

def register(UsersList, username, password):
    if username not in UsersList:
        if usernameCheck(username):
            if passwordCheck(password):
                f = open("UsersList.txt", "a")
                string = '\n'+ username + "," +password
                f.write(string)
                f.close()
    else:
        raise RuntimeError("Username already exists.")