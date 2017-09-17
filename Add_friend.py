# import statements.
from Spy_detail import Spy
import re
from globals import friends
spy = Spy("Star Boy","Mr",20,3.0,True)
# add new friends.
def add_friend():
    new_friend = {
        'name': '',
        'salutation': '.',
        'age': 0,
        'rating': 0.0,
        'is_online': False,
        'chats': []
    }
    temp_variable = True
    while temp_variable:
        pattern = '^[a-zA-Z\s][a-zA-Z\s]*$'
        new_friend['name'] = raw_input("Please add your friend's name: ")
        if (re.match(pattern, new_friend['name'])):
            temp_variable = False
            print "Please provide some more information of yours."
        else:
            print "Please input only alphabetical characters."
    temp_variable = True
    while temp_variable:
        new_friend['salutation']= raw_input("Are they Mr. or Ms.?: ")
        pattern = '^ms|mr|MR|MS|Mr|Ms'
        if (re.match(pattern, new_friend['salutation'])):
           new_friend['name'] = new_friend['salutation'] + " " + new_friend['name']
           temp_variable = False
        else:
            print "Please provide correct saluttion."
    while True:
        try:
            new_friend['age'] = int(raw_input("Age? "))# converting users input to integer (typecasting)
            break
        except ValueError:
            print "Stupid idiot! write a numeric value"

    new_friend['rating'] = float(raw_input("Spy rating? "))

    # users input validations
    if len(new_friend['name']) > 0 and new_friend['age'] > 12 and new_friend['age'] < 50 and new_friend['rating']> spy.rating:
        friends.append(new_friend)
        print 'Friend Added!'
    else:
        print 'Sorry! Something went wrong. We can\'t add spy with the details you provided'

    # returning total no of friends.
    return len(friends)