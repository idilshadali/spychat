from datetime import datetime #provides classess for manipulating date and time.

class Spy: #a class in simple words is a blueprint of an object,use to reuse our coad without writing it again

    def __init__(me, name, salutation, age, rating):
        me.name = name
        me.salutation = salutation
        me.age = age
        me.rating = rating
        me.is_online = True
        me.chats = []
        me.current_status_message = None


class msz:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()#current date and time
        self.sent_by_me = sent_by_me

spy = Spy('Dilshad', 'Mr.', 21, 4.2)

friend_one = Spy('Rakesh', 'Mr.', 23, 4.5)
friend_two = Spy('Sadaf', 'Ms.', 21, 4.03)
friend_three = Spy('Asif', 'Mr.', 21, 4.6)
friend_four = Spy('Azam', 'Mr.', 21, 5.00)


friends = [friend_one, friend_two, friend_three, friend_four]#details of friends.


