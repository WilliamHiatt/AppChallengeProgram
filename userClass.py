class User:
    """Class to create user objects"""

    def __init__(self, userid):
        """Initialize userId, Username, and Password"""
        self.userID = userid
        self.username = "Null"
        self.password = "Null"
        self.first_name = "Null"
        self.last_name = "Null"
        self.appetizer = "Null"

    def setusername(self, in_username):
        self.username = in_username

    def setpassword(self, in_password):
        self.password = in_password

    def setfirst_name(self, in_first_name):
        self.first_name = in_first_name

    def printfirst_name(self):
        print(self.first_name)


    def print_user_info(self):
        print("User ID " + str(self.userID))
        print("Username " + str(self.username))
        print("password " + str(self.password))
        print("first_name " + str(self.first_name))
        print("last_name " + str(self.last_name))
        print("Appetizer " + str(self.appetizer))


        