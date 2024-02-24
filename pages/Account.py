import customtkinter
from tkinter import TOP

from user.UserModel import User
from utils import FileOps

geometry = "650x500"


class AccountUI:

    @staticmethod
    def openFile(FileOp: FileOps, fileOutput: customtkinter.CTkLabel, pathLabel: customtkinter.CTkLabel):
        FileOp.openFile()

        if FileOp.fileName != "":
            fileOutput.configure(text="Your file path is:\n" + FileOp.fileName)
        else:
            pathLabel.configure(text="Choose a file path!")
            pathLabel.configure(text_color="red")

    @staticmethod
    def updateHistory(scrollableFrame: customtkinter.CTkScrollableFrame, user: User):

        for activity in user.get_history():
            print(activity.__str__())
            textLabel = customtkinter.CTkLabel(scrollableFrame, text=activity.__str__())
            textLabel.pack(anchor='w')

    def __init__(self, master, user: User):
        self.root = master

        self.root.geometry(geometry)
        self.root.title("Account")

        FileOp = FileOps()

        frame = customtkinter.CTkFrame(master=self.root)
        frame.pack(padx=60, pady=20, fill="both", expand=True)

        label = customtkinter.CTkLabel(master=frame, text="Welcome, " + user.get_username(),
                                       font=("Roboto-Medium.tff", 16))
        label.pack(padx=0, pady=10)

        pathLabel = customtkinter.CTkLabel(master=frame, text="Upload file to be compressed/extracted..")
        pathLabel.pack(side=TOP)

        fileEntry = customtkinter.CTkButton(master=frame,
                                            text="📁 File upload",
                                            command=lambda: self.openFile(
                                                FileOp=FileOp,
                                                fileOutput=fileOutput,
                                                pathLabel=pathLabel
                                            ),
                                            font=("Roboto", 12, "normal"))
        fileEntry.pack(padx=12, pady=10)

        fileOutput = customtkinter.CTkLabel(master=frame,
                                            height=1,
                                            text="Your file path is:\n",
                                            anchor="center")
        fileOutput.pack(padx=12, pady=5)

        compressButton = customtkinter.CTkButton(master=frame,
                                                 text="💾 Compress",
                                                 command=lambda: FileOp.compressFile(
                                                     user,
                                                     FileOp.fileName,
                                                     "D:\\compressedFile.xz"
                                                 ),
                                                 font=("Roboto", 12, "normal"))
        compressButton.pack(padx=12, pady=10)
        extractButton = customtkinter.CTkButton(master=frame,
                                                text="🗂️Extract",
                                                command=lambda: FileOp.extractFile(
                                                    user,
                                                    FileOp.fileName,
                                                    "D:\\extractedFile.txt"
                                                ),
                                                font=("Roboto", 12, "normal"))
        extractButton.pack(padx=12, pady=10)

        scrollable_frame = customtkinter.CTkScrollableFrame(frame,
                                                            label_text="Recent files:",
                                                            width=500,
                                                            height=300)
        scrollable_frame.pack(padx=20, pady=40)
        self.updateHistory(scrollable_frame, user)

        self.root.mainloop()
