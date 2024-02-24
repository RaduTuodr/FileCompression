from typing import List
from user.activity.ActivityModel import Activity


class User:

    def __init__(self, username, password, remember, activity_history=List[Activity]):
        self.username = username
        self.password = password
        self.remember = remember
        self.activity_history = activity_history

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_remember(self):
        return self.remember

    def get_history(self):
        return self.activity_history

    def __str__(self):
        line_to_write = self.get_username() + ' ' + self.get_password() + ' ' + str(self.get_remember())
        for activity in self.get_history():
            line_to_write += ' ' + str(activity.getFilePath())
            line_to_write += ' ' + str(activity.getFileOperation())
        line_to_write += '\n'
        return line_to_write
