from select_friend import select_friend
from steganography.steganography import Steganography
from datetime import datetime
from globals import friends
import  re
def send_message():
    # choose a friend from the list.
    friend_choice = select_friend()
    if friend_choice < len(friends):
        pattern = '^[a-zA-Z0-9]+\.jpg$'
        temp_variable = True
        while temp_variable:
        # prepare the message
            original_image = raw_input("Provide the name of the image to hide the message : ")
            if(re.match(pattern,original_image)):
                temp_variable = False
                print "Valid image"
            else:
                print "Invalid image"
        temp_variable = True
        while temp_variable:
            output_image = raw_input("Provide the name of the output image  : ")
            if (re.match(pattern, output_image)):
                temp_variable = False
                print "Valid image"
            else:
                print "Invalid image"
        text = raw_input("Enter your message here : ")
        if text.__len__()==0:
            print "come on buddy have you forgotten your words"
        elif text.__len__()>0 and text.__len__()<100:
            pattern = '^farah|beautiful|cute|pyari'
            if re.match(pattern,text):
                if text.__eq__('farah'):
                    print "Farah is most beautiful girl on Earth.inna sona kyun rab ne usse bnaya"
                elif text.__eq__('beautiful'):
                    print "Farah is beautiful,cute,adorable..Its very hard to get my Eyes off from you"
                elif text.__eq__('cute'):
                    print "Farah is the cutest girl i have ever met"
                elif text.__eq__('pyari'):
                    print "One word for Farah, Bhut pyari hai yaar"

                Steganography.encode(original_image, output_image, text)

                new_chat = {
                    'message': text,
                    'time': datetime.now(),
                    'sent_by_me': True
                }

                friends[friend_choice]['chats'].append(new_chat)
            else:
                # Encrypt the message
                Steganography.encode(original_image, output_image, text)

                new_chat = {
                    'message': text,
                    'time': datetime.now(),
                    'sent_by_me': True
                }

                friends[friend_choice]['chats'].append(new_chat)
                print "your secret message is ready."
                   # Successful message
        else:
            print friends[friend_choice]['name']
            friends.remove(friends[friend_choice])
            print "Can't speak more than 100 words.Please register yourself again."

    else:
        print "Wrong index entered."
