
from databases import authenticateUser, createUser


def authorizeAccess(username, password):
    return (username, authenticateUser(username, password))

def permissionsToAddNewUser(username, password, password2):
    # check for the password requirement before create user.
    if (len(password)>=6 and password==password2) and len(username)>=2:
        createUser(username, password)
        return (True, "Account created successfully. Please login :)")
    else:
        # it's just my basic requiement. Should be change in production.
        return (False, "Password does't requirement (7 characters, 1 capital letter, 2 digits). Try again :)")
    

if __name__ == '__main__':
    print("hello")