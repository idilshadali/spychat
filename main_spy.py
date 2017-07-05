from detail import spy, Spy, msz, friends  #use to transfr data frm spy_details file to main
from steganography.steganography import Steganography #use to hide info in plain sight
from datetime import datetime

prev_status = ["I just dont know how to think less.\n If you know how, then teach me.", "Roming on the road", "Chilling with friens","In the bar.\n Kal se chod dunga yar!"]#use to update status


print "Hello! buddy Let\'s start."

ask = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? "
avl = raw_input(ask)

#if y, below  if statement will execute
#if n, below else ststement will execute
def add_status():  #it defines atatus update

    updated_status = None #it desplays current status

    if spy.current_status_message!= None:

        print 'Your current status message is %s \n' % (spy.current_status_message)
    else:
        print 'You don\'t have any status message currently \n'

    default = raw_input("Do you want to select from the older status (y/n)? ")

    if default.upper() == "N":# if user type N,n user type new status
        new_status = raw_input("What status message do you want to set? ")


        if len(new_status) > 0:
            prev_status.append(new_status) #satus will store
            updated_status = new_status

    elif default.upper() == 'Y':#if user type y, it select prevous status

        item_position = 1

        for message in prev_status:
            print '%d. %s' % (item_position, message)
            item_position = item_position #current typed status is stored

        message_selection = int(raw_input("\nChoose from the above messages "))


        if len(prev_status) >= message_selection:
            updated_status = prev_status[message_selection - 1]

    else:
        print 'The option you chose is not valid! Press either y or n.'

    if updated_status:
        print 'Your updated status message is: %s' % (updated_status)
    else:
        print 'You current don\'t have a status update'

    return updated_status#current status value is returned


def add_friend(): #defining new friend

    new_friend = Spy('','',0,0.0)

    new_friend.name = raw_input("Please add your friend's name: ")
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")

    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = raw_input("Age?")
    new_friend.age = int(new_friend.age)

    new_friend.rating = raw_input("Spy rating?")
    new_friend.rating = float(new_friend.rating) #details of new friend

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend) #storing info of new friend
        print 'Your New Friend Is Added!'
    else:
        print 'Sorry! Your input is wrong. We can\'t add spy with the details you provided'

    return len(friends)  #redurning length of added friend to count no. of friend


def select_a_friend(): #defining friend selection.
    item_number = 0

    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % (item_number +1, friend.salutation, friend.name,
                                                   friend.age,
                                                   friend.rating)
        item_number = item_number + 1

    friend_choice = raw_input("Choose from your friends")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position #returning position


def send_message(): #defining send messages, use to send secrate message

    friend_choice = select_a_friend()

    original_image = raw_input("What is the name of the image?")
    output_path = "output.jpg"
    text = raw_input("What do you want to say? ")
    Steganography.encode(original_image, output_path, text) #to hide text, encode is done

    new_chat = msz(text,True)

    friends[friend_choice].chats.append(new_chat)

    print "Your secret message image is ready!"


def read_message(): #to read secrate message

    sender = select_a_friend()

    output_path = raw_input("What is the name of the file?")

    secret_text = Steganography.decode(output_path) #decoding is done to access the hidden text in image

    new_chat = msz(secret_text,False)

    friends[sender].chats.append(new_chat)

    print "Your secret message has been saved!"


def read_chat_history(): #to check message history

    read_for = select_a_friend()

    print '\n6'

    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print '[%s] %s: %s' % (chat.time.strftime("%d %B %Y"), 'You said:', chat.message)
        else:
            print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read_for].name, chat.message)


def start_chat(spy):

    spy.name = spy.salutation + " " + spy.name


    if spy.age > 12 and spy.age < 70:


        print "You are sucessfully authenticated. Welcome " + spy.name + " Your age is: " \
              + str(spy.age) + " and rating is: " + str(spy.rating) + " Happy to see you here. :)"

        show_menu = True

        while show_menu: #while loop continues until show_menu = fals
            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0: #len counts length of text
                menu_choice = int(menu_choice) #converts str into int

                if menu_choice == 1:
                    spy.current_status_message = add_status() #execute add_status() defined earlier
                elif menu_choice == 2:
                    number_of_friends = add_friend() #moves and executes add_friend() defined above
                    print 'You have %d friends' % (number_of_friends)
                elif menu_choice == 3:
                    send_message()#execute send_message() defined above
                elif menu_choice == 4:
                    read_message()#execute read_message() defined above
                elif menu_choice == 5:
                    read_chat_history()#execute read_chat_hostory defined above
                else:
                    show_menu = False#while loop terminates
    else:
        print 'Sorry you are not of the correct age to be a spy'


if avl == "Y" or avl == "y":#for old spy user
    username =raw_input("Your Username:")
    password=raw_input("Password")
    if username=="idilshad" and password=="1111a": #if else if used for username of password
        start_chat(spy)
    else:
        print("invalied username or password")
elif avl == "N" or avl == "n": #for new user
    spy = Spy('','',0,0.0)


    spy.name = raw_input("Welcome to spy chat, Enter your name please.: ")

    if len(spy.name) > 0:
        spy.salutation = ("You are Mr. or Ms.?:")
        spy_salutation=raw_input(spy.salutation)
        if spy_salutation == "Mr." or spy_salutation == "Ms.":
            spy.age = raw_input("Enter your age please?")
            spy.age = int(spy.age)

            spy.rating = raw_input(" And your Spy rating?")
            spy.rating = float(spy.rating)

            start_chat(spy)#details of new user
        else: #else statement executes if then user input doesn't satisfy if and elif condition.
            print("wrong input! Enter as mentioned")
            exit()


    else:
        print 'Please add a valid spy name'
else:
    print "Rong input."
    exit()
