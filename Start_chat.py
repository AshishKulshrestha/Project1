# import statements
#from globals import current_status_message
from Spy_detail import Spy
from read_chat import read_chat_history
from Add_status import add_status
from Add_friend import add_friend
from send_message import send_message
from read_message import read_message

spy = Spy("Star Boy","Mr",20,3.0,True)
# start_chat() function definition.
def start_chat(name, age, rating, status):
    error_message = None # variabmainle for storing error messages.
    welcome_massage = "Authentication complete. welcome\n" \
               "Name : %s" %spy.name + "\n" \
               "Age: %d" %spy.age + "\n" \
               "Rating %f: " %spy.rating + "\n" \
               "Proud to have you onboard"
      # displaying menu for user.
    show_menu = True
    while show_menu:
            menu_choices = "What do you want to do? \n " \
                           "1. Add a status update \n " \
                           "2. Add a friend \n " \
                           "3. Send a secret message \n " \
                           "4. Read a secret message \n " \
                           "5. Read Chats from a user \n " \
                           "6. Close Application \n"
            result = int(raw_input(menu_choices))

            # validating users input
            if (result == 1):
                current_status_message = None
                print current_status_message
                current_status_message = add_status(current_status_message)
            elif (result == 2):
                number_of_friends = add_friend()
                print 'You have %d friends' % (number_of_friends)
            elif(result == 3):
                send_message()
            elif (result == 4):
                read_message()
            elif (result == 5):
                read_chat_history()
            elif (result == 6):
                # close application
                show_menu = False
            else:
                print "wrong choice try again."