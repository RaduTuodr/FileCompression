import lzma
from tkinter import filedialog

from user import UserService
from user.UserModel import User
from user.activity.ActivityModel import Activity


class FileOps:
    def __init__(self):
        self.fileName = ""
        self.openedFile = False
        self.initialdir = 'Documents'
        self.directoryName = 'Documents'

    def openFile(self):
        file = filedialog.askopenfile(initialdir=self.initialdir,
                                      filetypes=[("Text files", "*.txt"),
                                                 ("Archived files", "*.xz")])
        if file is None:
            return
        self.fileName = file.name

    @staticmethod
    def compressFile(user: User, filePath, zipPath):

        if filePath == "" or filePath.endswith(".xz"):
            return

        UserService.add_activity(user, Activity(filePath, "Compressed"))

        with open(filePath, 'rb') as fileIn, lzma.open(zipPath, 'wb') as fileOut:
            fileOut.write(fileIn.read())

    @staticmethod
    def extractFile(user, zipPath, filePath):

        if filePath == "" or filePath.endswith(".txt"):
            return

        UserService.add_activity(user, Activity(zipPath, "Extracted"))

        with lzma.open(zipPath, 'rb') as fileIn, open(filePath, 'wb') as fileOut:
            fileOut.write(fileIn.read())
