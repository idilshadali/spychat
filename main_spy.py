from spy_detail import spy_name, spy_salutation, spy_rate, spy_age, spy_password, friends
from steganography.steganography import Steganography

from datetime import datetime

statuses = ["Hello! friends what's up", "what a cool weather", "Hanging out with music", "what a busy day!"]
friends_name = []
friends_age = []
friends_rating = []
friends_is_online = []
spy_ask1 = "Do you want to continue as " + spy_salutation + " " + spy_name + " (Y/N)? "
spy_perform = raw_input(spy_ask1)


def new_status(updated):
    current_status = None
    if updated != None:
        print "Your current status is \n" + updated
    else:
        print "You have no status right now\n"
    ask = raw_input("Do you want to select from your previous statuses? (Y/N)")
    if ask == "N" or ask == "n":
        new_update = raw_input("Please type your status")
        if len(new_update) > 0:
            statuses.append(new_update)
            current_status = new_update
    elif ask == 'Y' or ask == "y":
        position = 1
        for message in statuses:
            print '%d. %s' % (position, message)
            position = position + 1
        select = int(raw_input("\nPlease select your status "))
        if len(statuses) >= select:
            current_status = statuses[select - 1]
    else:
        print 'Wrong input'
    if current_status:
        print "Congratulation! your new status is " + current_status
    else:
        print "It seems You did not update you status"
    return current_status


def add_friend():
    friend_name = raw_input("Enter your friend's name: ")
    friend_salutation = raw_input(" Mr. or Ms.?: ")
    friend_name = friend_name + " " + friend_salutation
    friend_age = raw_input("Age?")
    friend_age = int(friend_age)
    friend_rating = raw_input("Spy rating?")
    friend_rating = float(friend_rating)

    if len(friend_name) > 0 and friend_age >= 18 and friend_age <= 45 and friend_rating >= 2.5 and friend_rating <= 5.0:
        friends_name.append(friend_name)
        friends_age.append(friend_age)
        friends_rating.append(friend_rating)
        friends_is_online.append(True)
        print 'Friend Added!'
    else:
        print "Sorry ! couldn't proceed \neither you have entered wrong input or your friend's details doesn't fulfil our requirements"

    return len(friends_name)


def chat_begin(spy_name, spy_age, spy_rate):
    updated = None
    spy_name = spy_salutation + " " + spy_name
    if spy_age >= "18" and spy_age <= "40":
        print "Welcome "
        menu = True
        while menu:
            menu_list = "Please select \n 1. Add a status \n 2. Add a friend \n 3. Send a secret message \n 4. Receive a secret message \n 5. Read your chat history \n 6. Exit"
            menu_choice = raw_input(menu_list)
            if menu_choice == "1":
                updated = new_status(updated)
            elif menu_choice == "2":
                number_of_friends = add_friend()
                print 'You have %d friends' % (number_of_friends)
            elif menu_choice == "3":
                send_message()
            elif menu_choice == "4":
                receive_message()
            elif menu_choice == "5":
                exit()
            else:
                menu = False
    else:
        print "Sorry!could not proceed\neither you have entered wrong input or your details doesn't fulfil our requirements"


def select_a_friend():
    item_number = 0

    for friend in friends:
        print '%d. %s aged %d with rating %.2f is online' % (item_number + 1, friend['name'],
                                                             friend['age'],
                                                             friend['rating'])
        item_number = item_number + 1

    friend_choice = raw_input("Choose from your friends")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position


def send_message():
    friend_choice = select_a_friend()

    original_image = raw_input("What is the name of the image?")
    output_path = "output.jpg"
    text = raw_input("What do you want to say? ")
    Steganography.encode(original_image, output_path, text)

    new_chat = {
        "message": text,
        "time": datetime.now(),
        "sent_by_me": True
    }

    friends[friend_choice]['chats'].append(new_chat)

    print "Your secret message image is ready!"


def receive_message():
    sender = select_a_friend()

    output_path = raw_input("What is the name of the file?")

    secret_text = Steganography.decode(output_path)

    new_chat = {
        "message": secret_text,
        "time": datetime.now(),
        "sent_by_me": False
    }

    friends[sender]['chats'].append(new_chat)

    print "Your secret message has been saved!"


if spy_perform == "Y" or spy_perform == "y":
    password = raw_input("Enter your password")
    if password == spy_password:
        chat_begin(spy_name, spy_age, spy_rate)
    else:
        print"wrong password"
        exit()
elif spy_perform == "N" or spy_perform == "n":
    spy_online = False
    new_user_name = raw_input("Your Name:")
    new_user_salutation = raw_input("Are you Mr. or Ms. ?")
    new_user_age = raw_input("Your Age:")
    new_user_rating = raw_input("Your rating(out of 5):")
    if new_user_rating <="2.0":
        print "Your Spy rating is not enough."
        exit()
    elif new_user_rating >"2.0" and new_user_rating <= "3.0":
        print "your Spy rating is good  "
    elif new_user_rating >"3.0" and new_user_rating <= "5.0":
        print "your rating id very good."
    else:
        print "Sorry! Wrong input."
        exit()
    spy_online = True
    chat_begin(spy_name, spy_age, spy_rate)
else:
    print("wrong input")
    exit()
