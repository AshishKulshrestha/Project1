from select_friend import select_friend
from steganography.steganography import Steganography
from datetime import datetime
import re
from globals import friends
def read_message():
    # choose friend from the list
    sender = select_friend()
    if sender < len(friends):
        temp = True
        while temp:
            pattern = '^[a-zA-Z0-9]+\.jpg$'
            encrypted_image = raw_input("Provide encrypted image : ")
            if(re.match(pattern,encrypted_image)):
                print "Valid image"
                temp = False
            else:
                print "Invalid image"
        secret_message = Steganography.decode(encrypted_image)
        # save the messages
        new_chat = {
            'message': secret_message,
            'time': datetime.now(),
            'sent_by_me': False
        }
        friends[sender]['chats'].append(new_chat)
        print new_chat['message']
    else:
        print "Wrong index entered"