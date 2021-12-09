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
        self.taste_score = 0
        self.effort_score = 0
        self.presentation_score = 0
        self.total_score = 0
        self.number_of_tens = 0


    def print_user_info(self):
        print("\n\nUser ID " + str(self.userID))
        print("Username " + str(self.username))
        print("password " + str(self.password))
        print("first_name " + str(self.first_name))
        print("last_name " + str(self.last_name))
        print("Appetizer " + str(self.appetizer))
        print("\n\n")


        