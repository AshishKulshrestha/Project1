from select_friend import select_friend
from steganography.steganography import Steganography
from datetime import datetime
from globals import friends
def read_message():
    # choose friend from the list
    sender = select_friend()

    encrypted_image = raw_input("Provide encrypted image : ")
    secret_message = Steganography.decode(encrypted_image)

    # save the messages
    new_chat = {
        'message': secret_message,
        'time': datetime.now(),
        'sent_by_me': False
    }

    friends[sender]['chats'].append(new_chat)
    print new_chat['message']