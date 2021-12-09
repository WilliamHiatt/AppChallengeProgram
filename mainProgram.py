from userClass import User

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

def getscores(usersDic, currentUserName):
    #Used to prompt the user for the scores and adds them
    for x in usersDic:
        if x != currentUserName:
            userinst = usersDic.get(x)
            print("You are now scoring the appetizer " + str(userinst.appetizer) + ".")
            score = input("\nEnter a score of 1-10 for the taste category: ")
            score = checkscore(score)
            userinst.taste_score = userinst.taste_score + score
            score = input("\nEnter a score of 1-10 for the effort category: ")
            score = checkscore(score)
            userinst.effort_score = userinst.effort_score + score
            score = input("\nEnter a score of 1-10 for the presentation category: ")
            score = checkscore(score)
            userinst.presentation_score = userinst.presentation_score + score
            print("Finished scoring " + str(userinst.appetizer) + ".\n\n\n\n\n\n")

            #Updates the users scores in the databse with the newley entered scores
            mycursor.execute("UPDATE users SET "
                             "taste_score = %s, "
                             "effort_score = %s,"
                             "presentation_score = %s, "
                             "number_of_tens = %s, "
                             "total_score = %s "
                             "WHERE username = %s",
                             (userinst.taste_score,
                              userinst.effort_score,
                              userinst.presentation_score,
                              userinst.number_of_tens,
                              userinst.total_score,
                              userinst.username))

            db.commit()

def checkscore(score):
    while(True):
        if int(score) >= 0 and int(score) <= 10:
            return int(score)
        else:
            print("The score must be between 1-10.")
            input("Please re-enter the score: ")



def sort_high_to_low(usersDic):
    #Finds the highest scores
    #Uses lists with strings having the users first name + the score they received.
    tasteList = []
    effortList = []
    presentationList = []
    totalScoreList = []

    #Loops through the userDic to compare each user to each user to every user in each class.
    for x in usersDic:
        userinst = usersDic.get(x)
        #Orders taste list
        for y in tasteList:
            currentUser = usersDic.get(y)
            if(userinst.taste_score > currentUser.taste_score):
                tasteList.insert(y, userinst.first_name + " with a score of " + str(userinst.taste_score))
            elif(y == len(tasteList)):
                tasteList.append(userinst.first_name + " with a score of " + str(userinst.taste_score))

        #orders effort list
        for y in effortList:
            currentUser = usersDic.get(y)
            if (userinst.effort_score > currentUser.effort_score):
                tasteList.insert(y, userinst.first_name + " with a score of " + str(userinst.effort_score))
            elif (y == len(effortList)):
                tasteList.append(userinst.first_name + " with a score of " + str(userinst.effort_score))

        #orders presentation list
        for y in presentationList:
            currentUser = usersDic.get(y)
            if (userinst.presentation_score > currentUser.presentation_score):
                tasteList.insert(y, userinst.first_name + " with a score of " + str(userinst.presentation_score))
            elif (y == len(presentationList)):
                tasteList.append(userinst.first_name + " with a score of " + str(userinst.presentation_score))

        ###STILL NEED TO DO TOTAL CATAGORY###

    #Prints out the winners in each catagory.
    print("The winners in the taste category are: \n")
    for x in range(2):
        if (x == 0):
            print("1st place " + tasteList[0])

        elif (x == 1):
            print("2nd place " + tasteList[1])

        elif (x == 2):
            print("3rd place " + tasteList[2])


    print("The winners in the effort category are: \n")
    for x in range(2):
        if (x == 0):
            print("1st place " + effortList[0])

        elif (x == 1):
            print("2nd place " + effortList[1])

        elif (x == 2):
            print("3rd place " + effortList[2])

    print("The winners in the presentation category are: \n")
    for x in range(2):
        if (x == 0):
            print("1st place " + presentationList[0])

        elif (x == 1):
            print("2nd place " + presentationList[1])

        elif (x == 2):
            print("3rd place " + presentationList[2])
