from userClass import User

def getscores(usersDic):
    for x in usersDic:
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

        ###NEED TO UPDATE DATABASE WITH THE SCORES AT THIS POINT

def checkscore(score):
    while(True):
        if int(score) >= 0 and int(score) <= 10:
            return int(score)
        else:
            print("The score must be between 1-10.")
            input("Please re-enter the score: ")



def sort_high_to_low(category, usersDic):
    returndict = {}
    for x in usersDic:
        userinst = usersDic.get(x)
        returndict[userinst.first_name] = userinst.taste

    sorteddict = sorted(returndict.items(), key=lambda x: x[1], reverse = True)

    for x in sorteddict:
        print(x)
        print("With a score of " + str(sorteddict[x]))


