import customtkinter
from pages import Account
from user import UserRepository
from user import UserModel

geometry = "500x350"


class LoginUI:

    @staticmethod
    def login(master, frame, userEntry, passwordEntry, rememberEntry):

        username = userEntry.get()
        password = passwordEntry.get()
        remember = rememberEntry.get()

        repository = UserRepository.UserRepository()

        newUser = UserModel.User(userEntry.get(), password, remember)

        if repository.addUser(newUser) is True:  # new guest
            frame.destroy()
            Account.AccountUI(master, newUser)
            return True
        else:
            user = repository.getUser(newUser.get_username())
            if user.get_password() == password:
                frame.destroy()
                Account.AccountUI(master, user)
                return True

        userEntry.configure(border_color="red")
        passwordEntry.configure(border_color="red")

        print("Login Unsuccessful")
        return False

    def __init__(self, master):
        self.root = master

        self.root.geometry(geometry)
        self.root.title("Login")

        frame = customtkinter.CTkFrame(master=self.root)
        frame.pack(padx=60, pady=20, fill="both", expand=True)

        label = customtkinter.CTkLabel(master=frame, text="Login", font=("Roboto-Medium.tff", 24))
        label.pack(padx=12, pady=10)

        userEntry = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
        userEntry.pack(padx=10, pady=12)

        passwordEntry = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
        passwordEntry.pack(padx=10, pady=12)

        button = customtkinter.CTkButton(master=frame, text="Login", command=lambda: self.login(
            self.root,
            frame,
            userEntry,
            passwordEntry,
            checkBox
        ))
        button.pack(padx=10, pady=12)

        checkBox = customtkinter.CTkCheckBox(master=frame, text="Remember me")
        checkBox.pack(padx=10, pady=12)

        self.root.mainloop()
