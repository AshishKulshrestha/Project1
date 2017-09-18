# import statements
from Spy_detail import Spy
from Start_chat import  start_chat
import re
spy = Spy("Star Boy","Mr",20,3.0,True)
print "Let's begin the application!"
question = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N): "
existing = raw_input(question)
# validating users input
if (existing.upper() == "Y") :
    spy.name = spy.name = spy.salutation + ". " + spy.name
    print "Welcome " + spy.name
    # starting chat application.
    start_chat(spy.name, spy.salutation, spy.age, spy.rating)
elif (existing.upper() == "N"):
    # user wants to continue as new user

    temporary_variable = True
    while temporary_variable:
        pattern = '^[a-zA-Z\s][a-zA-Z\s]*$'
        spy.name = raw_input("Provide your name here :")
        if (re.match(pattern, spy.name)):
            print spy.name
            temporary_variable = False
        else:
            print "Sorry! cant find alphabets."

    temporary_variable = True
    while temporary_variable:
        spy.salutation = raw_input("What should we all you ? : ")
        pattern = '^[ms|mr|MR|MS|Mr|Ms]'
        if (re.match(pattern, spy.salutation)):
            print spy.salutation
            temporary_variable = False
        else:
            print "Ooopssss! Find your gender."

    while True:
        try:
            spy.age = int(raw_input("Enter your age: ")) # converting users input to integer (typecasting)
            break
        except ValueError:
            print "Stupid idiot! write a numeric value"

    if spy.age >12 or spy.age <= 50:
        print "You are eligible to be a spy"
        spy.rating = float(raw_input("What is your spy rating?")) # converting users input to float (typecasting)
        if spy.rating>4.7 and spy.rating<=5:
            print "The spy is doin an Excellent job. You are the next James bond."
        elif spy.rating<4.7 and spy.rating <=3.7:
            print "The spy is doin a good job. you can be the next James bond"
        elif spy.rating <3.7 and spy.rating<2.5:
            print "Spy is doin Average job. Come on, you can do it"
        else:
            print "Spy is not doin a good job. Dont even think that you can be the next James bond. Get lost"


        spy.is_Online = int(raw_input("Enter 1 if online else enter 0 : "))
        if spy.is_Online == 1:
            print "Spy is online"
            print "Spy named %s" %spy.name + " Age: %d" %spy.age + " Rating : %f" %spy.rating
        elif spy.is_Online ==0:
            print "Spy is sleeping"
            print "Spy named %s" % spy.name + " Age: %d" % spy.age + " Rating : %f" % spy.rating
        # starting chat application.
        start_chat(spy.name, spy.age, spy.rating, spy.is_Online)

