import random

answers = []

def bridge_keeper():
    
    questions = ["What is your favourite colour?", "What is the airspeed velocity of an unladen swallow?","What is the capital of Assyria?"]
    correct_answer = "African or European?"

    print("STOP!!!!\nThose who approach the Bridge of Death must answer me these questions three, ere the other side they see.\n")
    # the built in input function can prompt with a string, and then return whatever the user has input into the console as a string.  Even if it's a number!!!
    name = input("What is your name?\n")
    quest = input("What is your quest?\n")
    random_question = random.randint(0,len(questions)-1)
    third = input(f"{questions[random_question]}\n")

    # What is your favourite colour?
    if random_question == 0:
        # checks to see if the color has been guessed already.
        if third in answers:
            print("You have been casted into gorge!!!\n")
            return True
        else:
            answers.append(third)
            print("Right. Off you go.\n")
            return True
    # What is the velocity of an unladen swallow?
    elif random_question == 1:
        if third == correct_answer:
            print("Wait... I don't know.  AHHHHHHH!!!!!!\nThe bridge keeper was casted into the gorge.")
            return False
        else:
            print("You have been casted into gorge!!!\n")
            return True
    # What is the capital of Assyria?
    elif random_question == 2:
        # checks for correct answer
        if third == "Ninevah":
            print("Right. Off you go.\n")
            return True
        else:
            print("You have been casted into gorge!!!\n")
            return True

isGuessing = True

while isGuessing == True:
    isGuessing = bridge_keeper()

# When we initially run this file the first thing that appears in our terminal
# STOP!!!!
# Those who approach the Bridge of Death must answer me these questions three, ere the other side they see.

#first input is What is your name?
#second input is What is your quest?
#third input is one of the three questions at random if this question is what is your favorite color and you answer it with a color that has not been guessed already then we will see
#Right. Off you go.

#Then it goes back to the beginning of the loop and again will display 
#STOP
#Those who approach...
#first and second input again..
# third input will be one of the two questions that have yet to pop up. if the question is the velocity question you must answer the correct_answer = "African or European" to get 
#Wait... I don't know.  AHHHHHHH!!!!!!
#The bridge keeper was casted into the gorge.
# and the loop will end

#if answered anything but the correct_answer you will get the response
#You have been casted into gorge

#if asked the capital of assyria?
# must answer Ninevah 
#which will get the response right off you go 
# and then it will loop again 
#stop
#those who approach..


# the loop will only end if you get the question about the velocity and answer it correctly