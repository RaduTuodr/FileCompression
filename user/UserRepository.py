from user import UserModel
from user.UserModel import User
from user.activity.ActivityModel import Activity

DB_path = 'DB.txt'


def getData():
    users = []

    with open(DB_path, 'r') as file:
        for line in file:
            parts = line.split()

            username = parts[0]
            password = parts[1]
            remember = parts[2]

            try:
                remember = int(remember)
            except ValueError:
                remember = 0

            activityRecord = []
            for index in range(3, len(parts), 2):
                activity = Activity(parts[index], parts[index + 1])
                activityRecord.append(activity)

            newUser = User(username, password, remember, activityRecord)
            users.append(newUser)

    return users


def postUser(user):
    with open(DB_path, 'a') as file:
        file.write(user.__str__())


def postUsers(users):
    with open(DB_path, 'w') as file:
        for user in users:
            file.write(user.__str__())


class UserRepository:

    def __init__(self):
        self.users = getData()

    def getUser(self, username):
        for user in self.users:
            if user.get_username() == username:
                return user
        return None

    def addUser(self, user: User):
        if self.getUser(user.get_username()) is None:
            self.users.append(user)
            postUser(user)
            return True
        return False

    def addActivity(self, username: str, activity: Activity):
        for user in self.users:
            if user.get_username() == username:
                user.activity_history.append(activity)

    def update(self):
        postUsers(self.users)
