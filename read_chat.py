from globals import friends
from select_friend import select_friend
from colorama import Fore
def read_chat_history():
    friend = select_friend()
    if friend < len(friends):
        for chat in friends[friend]['chats']:
            print Fore.RED,friends[friend]['Name']
            print Fore.BLUE, chat['time']
            print Fore.CYAN, chat['mesage']
            print Fore.RESET
    else:
        print "Entered index is not correct. Please input correct index"


