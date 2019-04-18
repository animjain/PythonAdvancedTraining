"""
Create a UserDB class that abstracts a structures text file representing
user records - as a dictionary.

Text file format is as below (store the below lines in file users.dat):
   hansson:heine123:David Hansson
   larry:larry567:Larry Wall
   rossum:guido11:Guido Rossum
   steve:steve123:Steven Bourne
   korn:dk1122:David Korn

In the above file format, each line represents the user record composed of 3
fields representing user's name, password and fullname.

Implement the UserDB class such that the following module-level test-cases
work:

    Setup fixtures (creating the users.dat file automatically for
    the following test-cases to work):
        >>> user_records = '''
        hansson:heine123:David Hansson
        larry:larry567:Larry Wall
        rossum:guido11:Guido Rossum
        steve:steve123:Steven Bourne
        korn:dk1122:David Korn
        '''
        >>> with open("users.dat", "w") as userdb_file:
        ...    for line in user_records.splitlines():
        ...        userdb_file.write(line.strip() + "\n")

        >>> users = UserDB("users.dat")
        >>> users
        UserDB(path="file://./users.dat")

    Test case 1: Access a user record ( return an instance of UserDB.User )
        # User larry exists.
        >>> users["larry"]
        User(name='larry', password='larry567', fullname='Larry Wall')

        # User brian does not exist.
        >>> users["brian"]
        Traceback (most recent call last):
        ...
        KeyError: User 'brian' does not exist.

    Test case 2: Access user password/fullname
        >>> users["larry"]["password"]
        larry567

        >>> users["rossum"]["fullname"]
        Guido Rossum

        >>> users["steve"]["role"]
        Traceback (most recent call last):
        ...
        KeyError: User 'steve' has no 'role'.

    Test case 3: Add a new user record
        # The following statement should add a new record to the underlying file.
        >>> users["james"] = User(password="cafe123", fullname="James Gosling")

        >>> users["james"]
        User(name='james', password='cafe123', fullname='James Gosling')

        # Do not allow adding duplicate users
        >>> users["james"] = User(password='test123', fullname='James Whitmire')
        Traceback (most recent call last):
        ...
        KeyError: User 'james' already exists.

    Test case 4: Modify user record
        # Change larry's password
        >>> users['larry']['password'] = 'walls123'
        >>> users['larry']['password']
        walls123

        # Trying to add/change a field that's not 'password' / 'fullname'
        # should raise an exception.
        >>> users['james']['role'] = "admin"
        Traceback (most recent call last):
        ...
        KeyError: User 'james' has no role.

    Test case 5: Delete a user record
        >>> del users["larry"]

        >>> users["larry"]
        Traceback (most recent call last):
        ...
        KeyError: User 'larry' does not exist.

        # Fields of a user record cannot be deleted.
        >>> del users["larry"]["password"]
        Traceback (most recent call last):
        ...
        KeyError: Cannot delete fields of users.


"""
class UserDB:
    pass
