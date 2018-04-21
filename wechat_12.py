
class Message(object):

    def __init__(self, message):
        self.message = message

    def __newMessage__(self, newMessage):
        self.message = newMessage


class User(object):

    def __init__(self, name, age, sex, brithday, phoneNem):
        self.name = name
        self.age = age
        self.sex = sex
        self.brithday = brithday
        self.phoneNum = phoneNem

class Room(object):
    def __init__(self, userList):
        self.userList = userList

    def __newuser__(self, newUser):
        self.userList.append(newUser)

    def __delUser__(self, index):
        del self.userList[index]