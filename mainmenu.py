from userClass import User
from mainProgram import *

# GETS CONNECTED TO THE DATABASE #
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Hiatt1234",
    database="appetizerchallenge"
    )
# SETS OUR CURSOR FOR THE DATABASE #
mycursor = db.cursor()

userID = []
usersDic = {}


def menu():
    """This is the main menu of the program"""
    case = True
    while case == True:
        selection = input("1\tLogin\n2\tCreate Account\n3\tExit\nAdmin 4 for sort 5 for set 0\n")
        if selection == '1':
            login()
        elif selection == '2':
            new_user()
        elif selection == '3':
            print("We exited")
            case = False
        # TEMPT FOR TESTING
        elif selection == '4':
            sort_high_to_low(usersDic)
        elif selection == '5':
            set_scores_zero()
        else:
            print("Please select one of the above options.")


def user_menu(userinst):
    """This is the function that starts the users menu that allows them to vote, change and print user info"""
    while True:
        print("\nPlease select one of the following: ")
        selection = input(" 1. Print your info.\n"
                          " 2. Change your info.\n"
                          " 3. Score Appetizers\n"
                          " 4. Logout\n")

        if selection == '1':
            userinst.print_user_info()
        elif selection == '2':
            change_user_info_menu(userinst)
        elif selection == '3':
            if userinst.voted != True:
                getscores(usersDic, userinst.username)
            else:
                print("\nYou already voted.\n")
        elif selection == '4':
            break
        else:
            print("Please select one of the above options.")


def new_user():
    """This gets the users information to create an account and loads it into the databse"""
    username = input("Please enter your username: ")
    # checks to make sure the user isn't already in the system
    check = check_user(username)
    if check == True:
        print("You already have an account.")

    # hits if the user isn't in the database. Asks for all user information then
    # sends it to the database to create a new user
    else:
        password = input("Please enter your password: ")
        first_name = input("Please enter your first name: ")
        last_name = input("Please enter your last name: ")
        appetizer = input("Please enter your appetizer: ")
        mycursor.execute("INSERT INTO users "
                         "(username, "
                         "password, "
                         "first_name, "
                         "last_name,"
                         "appetizer) "
                         "VALUES (%s,%s,%s,%s,%s)",
                         (username,
                          password,
                          first_name,
                          last_name,
                          appetizer))
        db.commit()

        usersDic.clear()
        get_database_info()


def change_user_info_menu(userinst):
    """This function allows the user to change their info"""
    # Loop to allow the user to make multiple changes
    while True:
        # Lists menu to let the user pick what they want to change
        print("Select one of the following options: ")
        selection = input(" 1. Change Username\n"
                          " 2. Change Password\n"
                          " 3. Change Appetizer\n"
                          " 4. Change First Name\n"
                          " 5. Change Last Name\n"
                          " 6. Exit\n")

        if int(selection) == 1:
            userinst.change_username()
            # Needs to call get_database_info() so that we can update
            # the key for the current user as the key is the users username
            get_database_info()
        elif int(selection) == 2:
            userinst.change_password()
        elif int(selection) == 3:
            userinst.change_appetizer()
        elif int(selection) == 4:
            userinst.change_firstname()
        elif int(selection) == 5:
            userinst.change_lastname()
        # Breaks loop and exits function when user selects 6
        elif int(selection) == 6:
            update_user_info(userinst)
            print("\nUpdates have been saved!\n")
            return
        else:
            print("Please select one of the options.\n")

def login():
    """This verifies the user and logs them in"""
    status = False
    username = input("\nPlease enter your username: ")
    password = input("Please enter your password: ")

    # Makes sure the user has an account already
    if check_user(username):
        # Gets the class location of user and puts it into userinst (user instance)
        userinst = usersDic.get(username)
        real_password = userinst.password
        # Loop to continue to ask for user password if it is incorrect
        while status != True:
            # Hits here if password is correct
            if real_password == password:
                status = True
            # Hits here if password is not correct and requests the user try again
            else:
                print("Incorrect Password")
                password = input("Please re-enter password: ")

        user_menu(userinst)

    else:
        print("There is no account under that username.\n" )
        selection = input("Would you like to\n "
                          " 1. Create a new account\n "
                          " 2. Try another username\n")
        if selection == "1":
            new_user()
            login()
        else:
            login()


def check_user(username):
    """Checks to make sure the user doesn't already have an account"""
    # will run through the dictionary of users to see if the user is already in the system
    if username in usersDic:
        return True


def get_database_info():
    """This function gets all the user information from the database"""
    mycursor.execute("SELECT userId FROM users")
    # Puts all userID's into the userID list. This list is then used to start creating
    # objects once the user class is made
    for x in mycursor:
        userID.append(x)

    # Loops through the current user ID and inputs data into a dictionary
    for x in userID:
        newuser = User(x[0])
        mycursor.execute("SELECT username FROM users WHERE userId = " + str(x[0]) + "")
        for y in mycursor:
            newuser.username = y[0]

        mycursor.execute("SELECT password FROM users WHERE userId = " + str(x[0]) + "")
        for y in mycursor:
            newuser.password = y[0]

        mycursor.execute("SELECT first_name FROM users WHERE userId = " + str(x[0]) + "")
        for y in mycursor:
            newuser.first_name = y[0]

        mycursor.execute("SELECT last_name FROM users WHERE userId = " + str(x[0]) + "")
        for y in mycursor:
            newuser.last_name = y[0]

        mycursor.execute("SELECT appetizer FROM users WHERE userId = " + str(x[0]) + "")
        for y in mycursor:
            newuser.appetizer = y[0]

        mycursor.execute("SELECT taste_score FROM users WHERE userId = " + str(x[0]) + "")
        for y in mycursor:
            newuser.taste_score = y[0]

        mycursor.execute("SELECT effort_score FROM users WHERE userId = " + str(x[0]) + "")
        for y in mycursor:
            newuser.effort_score = y[0]

        mycursor.execute("SELECT presentation_score FROM users WHERE userId = " + str(x[0]) + "")
        for y in mycursor:
            newuser.presentation_score = y[0]

        mycursor.execute("SELECT number_of_tens FROM users WHERE userId = " + str(x[0]) + "")
        for y in mycursor:
            newuser.number_of_tens = y[0]

        # Stores instance into dictionary with username as key
        usersDic[newuser.username] = newuser


def set_scores_zero():
    for x in usersDic:
        userinst = usersDic.get(x)

        mycursor.execute("UPDATE users SET "
                         "taste_score = %s, "
                         "effort_score = %s,"
                         "presentation_score = %s, "
                         "number_of_tens = %s, "
                         "total_score = %s "
                         "WHERE username = %s",
                         (0, 0, 0, 0, 0, userinst.username))

        db.commit()


def update_user_info(userinst):
    mycursor.execute("UPDATE users SET "
                     "username = %s, "
                     "password = %s, "
                     "first_name = %s, "
                     "last_name = %s,"
                     "appetizer = %s "
                     "WHERE userId = %s",
                     (userinst.username,
                      userinst.password,
                      userinst.first_name,
                      userinst.last_name,
                      userinst.appetizer,
                      userinst.userID))
    db.commit()

get_database_info()

print("Annual Appetizer Challenge")

menu()
