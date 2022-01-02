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
        self.total_score = self.taste_score + self.effort_score + self.presentation_score
        self.number_of_tens = 0
        self.voted = False
        self.admin = False

    def print_user_info(self):
        # Prints all user information besides scores. These are kept confidential
        # until the end of the program once winners are announced
        print("\n\nUser ID " + str(self.userID))
        print("Username " + str(self.username))
        print("password " + str(self.password))
        print("first_name " + str(self.first_name))
        print("last_name " + str(self.last_name))
        print("Appetizer " + str(self.appetizer))
        print("\n\n")

    def change_username(self):
        # Makes sure user wants to change their username and then changes
        # if the user does want to change
        selection = input("Your current username is " + self.username +
                          ". Do you still want to change it? ('yes' or 'no'\n")

        while True:
            if selection.lower() == "yes":
                new_value = input("What is the new username? ")
                self.username = str(new_value)
                print("\nUpdated: Note these changes won't save until you select 6 to exit\n")
                return
            elif selection.lower() == "no":
                return
            else:
                selection = input("Please enter 'yes' or 'no': ")

    def change_password(self):
        # Requires user to enter current password and then requests new password
        current_pswd = input("Please enter your current password: ")

        while True:
            if str(current_pswd) == self.password:
                # Requires two passwords to ensure that there aren't any typo's when entering
                new_pswd = input("\nPlease enter your new password: ")
                new_pswd2 = input("Please re-enter your new password: ")

                # Confirms passwords match
                if new_pswd == new_pswd2:
                    self.password = new_pswd
                    break

                else:
                    print("\nThe two passwords don't match.\n")

            if str(current_pswd) != self.password:
                print("\nIncorrect password.\n")
                current_pswd = input("Please re-enter your password: ")

    def change_firstname(self):
        # Makes sure user wants to change their firstname and then changes
        # if the user does want to change
        selection = input("Your current first name is " + self.first_name +
                          ". Do you still want to change it? ('yes' or 'no'\n")
        while True:
            if selection.lower() == "yes":
                new_value = input("What is the new first name? ")
                self.first_name = str(new_value)
                print("\nUpdated: Note these changes won't save until you select 6 to exit\n")
                return
            elif selection.lower() == "no":
                return
            else:
                selection = input("Please enter 'yes' or 'no': ")

    def change_lastname(self):
        # Makes sure user wants to change their lastname and then changes
        # if the user does want to change
        selection = input("Your current last name is " + self.last_name +
                          ". Do you still want to change it? ('yes' or 'no'\n")

        while True:
            if selection.lower() == "yes":
                new_value = input("What is the new last name? ")
                self.last_name = str(new_value)
                print("\nUpdated: Note these changes won't save until you select 6 to exit\n")
                return
            elif selection.lower() == "no":
                return
            else:
                selection = input("Please enter 'yes' or 'no': ")

    def change_appetizer(self):
        # Makes sure user wants to change their appetizer and then changes
        # if the user does want to change
        selection = input("Your current appetizer is " + self.appetizer +
                          ". Do you still want to change it? ('yes' or 'no'\n")
        while True:
            if selection.lower() == "yes":
                new_value = input("What is the new appetizer? ")
                self.appetizer = str(new_value)
                print("\nUpdated: Note these changes won't save until you select 6 to exit\n")
                return
            elif selection.lower() == "no":
                return
            else:
                selection = input("Please enter 'yes' or 'no': ")