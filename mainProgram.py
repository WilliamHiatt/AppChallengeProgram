from userClass import User

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


def getscores(usersDic, currentUserName):
    # Used to prompt the user for the scores and adds them
    for x in usersDic:
        if x != currentUserName:
            userinst = usersDic.get(x)
            print("You are now scoring the appetizer " + str(userinst.appetizer) + ".")
            score = input("\nEnter a score of 1-10 for the taste category: ")
            score = checkscore(score, userinst)
            userinst.taste_score = userinst.taste_score + score
            score = input("\nEnter a score of 1-10 for the effort category: ")
            score = checkscore(score, userinst)
            userinst.effort_score = userinst.effort_score + score
            score = input("\nEnter a score of 1-10 for the presentation category: ")
            score = checkscore(score, userinst)
            userinst.presentation_score = userinst.presentation_score + score
            print("Finished scoring " + str(userinst.appetizer) + ".\n\n\n\n\n\n")

            userinst.total_score = userinst.total_score + userinst.taste_score + \
                                   userinst.presentation_score + userinst.effort_score

            # Updates the users scores in the databse with the newley entered scores
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
    currentuser = usersDic.get(currentUserName)
    currentuser.voted = False

def checkscore(score, instance):
    # Makes sure that the entered score falls within the required
    # parameters.
    while(True):
        if int(score) >= 0 and int(score) <= 10:
            # Checks to see if it's a perfect score. If it is tallies it.
            if int(score) == 10:
                instance.number_of_tens += 1
            return int(score)
        else:
            print("The score must be between 1-10.")
            input("Please re-enter the score: ")


def sort_high_to_low(usersDic):
    # Finds the highest scores
    # Lists consist of user class instances
    tasteList = []
    effortList = []
    presentationList = []
    totalScoreList = []

    # Counter user to keep track of where we are in the list
    counter = 0
    # Insert sort into tasteList
    for x in usersDic:
        userinst = usersDic.get(x)
        # Hits if we have an empty list
        if len(tasteList) == 0:
            tasteList.append(userinst)

        else:
            for y in tasteList:
                # Hits if the current instance is greater than the current position in the list
                if userinst.taste_score >= y.taste_score:
                    tasteList.insert(counter, userinst)
                    break
                # Hits if we are in the last position in the list
                elif len(tasteList) == counter + 1:
                    tasteList.append(userinst)
                    break
                # Increments counter to next list position
                counter += 1
    # Sets the counter back to 0
    counter = 0
    # Insert sort of effort list
    for x in usersDic:
        userinst = usersDic.get(x)
        # Hits if empty list
        if len(effortList) == 0:
            effortList.append(userinst)

        else:
            for y in effortList:
                # Hits if the current instance is greater than the current position in the list
                if userinst.effort_score >= y.effort_score:
                    effortList.insert(counter, userinst)
                    break
                # Hits if last element in list
                elif len(effortList) == counter + 1:
                    effortList.append(userinst)
                    break
                # Increments list
                counter += 1
    # sets counter back to 0
    counter = 0
    # Insert sort for presentation list
    for x in usersDic:
        userinst = usersDic.get(x)
        # Hits if the list is empty
        if len(presentationList) == 0:
            presentationList.append(userinst)

        else:
            for y in presentationList:
                # Hits if the current instance is greater than the current position in the list
                if userinst.presentation_score >= y.presentation_score:
                    presentationList.insert(counter, userinst)
                    break
                # Hits if we are on the last element of the list
                elif len(presentationList) == counter + 1:
                    presentationList.append(userinst)
                    break

                counter += 1

    counter = 0
    # Insert sort for total score list
    for x in usersDic:
        userinst = usersDic.get(x)
        # Hits if the list is empty
        if len(totalScoreList) == 0:
            totalScoreList.append(userinst)

        else:
            for y in totalScoreList:
                # Hits if the current instance is greater than the current position in the list
                if userinst.total_score >= y.total_score:
                    totalScoreList.insert(counter, userinst)
                    break
                # Hits if we are at the last element in the list
                elif len(totalScoreList) == counter + 1:
                    totalScoreList.append(userinst)
                    break

                counter += 1

    # Prints out the top 3 and the score each received taste
    counter = 2
    while counter >= 0:
        currentuser = tasteList[counter]
        if counter == 2:
            print("In 3rd place for taste with a score of " + str(currentuser.taste_score) + ", "
                  + currentuser.first_name + "!")
            counter -= 1
        elif counter == 1:
            print("In 2nd place for taste with a score of " + str(currentuser.taste_score) + ", "
                  + currentuser.first_name + "!")
            counter -= 1
        elif counter == 0:
            print("In 1st place for taste with a score of " + str(currentuser.taste_score) + ", "
                  + currentuser.first_name + "!\n")
            counter -= 1

        # Prints out the top 3 and the score each received in effort
    counter = 2
    while counter >= 0:
        currentuser = effortList[counter]
        if counter == 2:
            print("In 3rd place for effort with a score of " + str(currentuser.effort_score) + ", "
                    + currentuser.first_name + "!")
            counter -= 1
        elif counter == 1:
            print("In 2nd place for effort with a score of " + str(currentuser.effort_score) + ", "
                    + currentuser.first_name + "!")
            counter -= 1
        elif counter == 0:
            print("In 1st place for effort with a score of " + str(currentuser.effort_score) + ", "
                    + currentuser.first_name + "!\n")
            counter -= 1

    # Prints out the top 3 and the score each received in presentation
    counter = 2
    while counter >= 0:
        currentuser = presentationList[counter]
        if counter == 2:
            print("In 3rd place for presentation with a score of " + str(currentuser.presentation_score) + ", "
                    + currentuser.first_name + "!")
            counter -= 1
        elif counter == 1:
            print("In 2nd place for presentation with a score of " + str(currentuser.presentation_score) + ", "
                    + currentuser.first_name + "!")
            counter -= 1
        elif counter == 0:
            print("In 1st place for presentation with a score of " + str(currentuser.presentation_score) + ", "
                    + currentuser.first_name + "!\n")
            counter -= 1

    # Prints out the top 3 and the score each received in total category
    counter = 2
    while counter >= 0:
        currentuser = totalScoreList[counter]
        if counter == 2:
            print("In 3rd place for overall with a score of " + str(currentuser.total_score) + ", "
                    + currentuser.first_name + "!")
            counter -= 1
        elif counter == 1:
            print("In 2nd place for overall with a score of " + str(currentuser.total_score) + ", "
                    + currentuser.first_name + "!")
            counter -= 1
        elif counter == 0:
            print("In 1st place for overall with a score of " + str(currentuser.total_score) + ", "
                    + currentuser.first_name + "!\n")
            counter -= 1

