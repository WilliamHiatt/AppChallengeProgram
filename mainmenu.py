from userClass import User
from mainProgram import *

### GETS CONNECTED TO THE DATABASE ###
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Hiatt1234",
    database="appetizerchallenge"
    )
### SETS OUR CURSOR FOR THE DATABASE ###
mycursor = db.cursor()

#mycursor.execute("INSERT INTO users (username, password) VALUES (%s,%s)", ("Valval0721", "Babyface27"))
#db.commit()

userID = []
usersDic = {}

def menu():
    """This is the main menu of the program"""
    case = True
    while case == True:
        selection = input("1\tLogin\n2\tCreate Account\n3\tExit\n")
        if selection == '1':
            login()
        elif selection == '2':
            new_user()
        elif selection == '3':
            print("We exited")
            case = False
        else:
            print("Please select one of the above options.")


def user_menu(userinst):
    """This is the function that starts the users menu that allows them to vote, change and print user info"""
    while True:
        print("Please select one of the following: ")
        selection = input(" 1. Print your info.\n"
                          " 2. Change your info.\n"
                          " 3. Score Appetizers\n"
                          " 4. Exit\n")

        if selection == '1':
            userinst.print_user_info()
        elif selection == '2':
            ####### NEED TO FINISH THIS PART ########
            print("Not finished yet")
        elif selection == '3':
            getscores(usersDic, userinst.username)
        elif selection == '4':
            break
        else:
            print("Please select one of the above options.")

def new_user():
    """This gets the users information to create an account and loads it into the databse"""
    username = input("Please enter your username: ")
    ##checks to make sure the user isn't already in the system
    check = check_user(username)
    if check == True:
        print("You already have an account.")

    #hits if the user isn't in the database. Asks for all user information then
    #sends it to the database to create a new user
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
        getDatabaseInfo()


def login():
    """This verifies the user and logs them in"""
    status = False
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")

    #Makes sure the user has an account already
    if check_user(username):
        #Gets the class location of user and puts it into userinst (user instance)
        userinst = usersDic.get(username)
        real_password = userinst.password
        #Loop to continue to ask for user password if it is incorrect
        while(status != True):
            #Hits here if password is correct
            if real_password == password:
                status = True
            #hits here if password is not correct and requests the user try again
            else:
                print("Incorrect Password")
                password = input("Please re-enter password: ")
    else:
        print("There is no account under that username.\n" )
        selection = input("Would you like to\n "
                            "1. Create a new account\n "
                            "2. Try another username\n")
        if selection == "1":
            new_user()
            login()
        else:
            login()

    user_menu(userinst)

def check_user(username):
    """Checks to make sure the user doesn't already have an account"""
    ##will run through the dictionary of users to see if the user is already in the system
    if username in usersDic:
        return True

def getDatabaseInfo():
    """This function gets all the user information from the database"""
    mycursor.execute("SELECT userId FROM users")
    #Puts all userID's into the userID list. This list is then used to start creating
    #objects once the user class is made
    for x in mycursor:
        userID.append(x)

    #Loops through the current user ID and inputs data into a dictionary
    for x in userID:
        newUser = User(x[0])
        mycursor.execute("SELECT username FROM users WHERE userId = " + str(x[0]) + "")
        for y in mycursor:
            newUser.username = y[0]

        mycursor.execute("SELECT password FROM users WHERE userId = " + str(x[0]) + "")
        for y in mycursor:
            newUser.password = y[0]

        mycursor.execute("SELECT first_name FROM users WHERE userId = " + str(x[0]) + "")
        for y in mycursor:
            newUser.first_name = y[0]

        mycursor.execute("SELECT last_name FROM users WHERE userId = " + str(x[0]) + "")
        for y in mycursor:
            newUser.last_name = y[0]

        mycursor.execute("SELECT appetizer FROM users WHERE userId = " + str(x[0]) + "")
        for y in mycursor:
            newUser.appetizer = y[0]

        mycursor.execute("SELECT taste_score FROM users WHERE userId = " + str(x[0]) + "")
        for y in mycursor:
            newUser.taste_score = y[0]

        mycursor.execute("SELECT effort_score FROM users WHERE userId = " + str(x[0]) + "")
        for y in mycursor:
            newUser.effort_score = y[0]

        mycursor.execute("SELECT presentation_score FROM users WHERE userId = " + str(x[0]) + "")
        for y in mycursor:
            newUser.presentation_score = y[0]

        mycursor.execute("SELECT number_of_tens FROM users WHERE userId = " + str(x[0]) + "")
        for y in mycursor:
            newUser.number_of_tens = y[0]

        #Stores instance into dictionary with username as key
        usersDic[newUser.username] = newUser


getDatabaseInfo()

print("Annual Appetizer Challenge")

menu()