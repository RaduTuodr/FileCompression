import customtkinter
from pages import Login

geometry = "500x350"


class HomeUI:

    @staticmethod
    def load(agreeCheck, master, frame):

        if agreeCheck.get():
            frame.destroy()
            Login.LoginUI(master)
        else:
            agreeCheck.configure(border_color="red")

    def __init__(self, master):
        self.root = master

        self.root.geometry(geometry)
        self.root.title("Home")

        frame = customtkinter.CTkFrame(master=self.root)
        frame.pack(padx=60, pady=20, fill="both", expand=True)

        label = customtkinter.CTkLabel(master=frame, text="Welcome!", font=("Roboto-Medium.tff", 24))
        label.pack(padx=12, pady=20)

        label = customtkinter.CTkLabel(master=frame, text="Login to be able to compress \nand decompress files", font=("Roboto-Medium.tff", 16))
        label.pack(padx=12, pady=40)

        button = customtkinter.CTkButton(master=frame, text="Login", command=lambda: self.load(
            termsCheckBox,
            self.root,
            frame
        ))
        button.pack(padx=12, pady=10)

        termsCheckBox = customtkinter.CTkCheckBox(master=frame, text="Agree to download locally")
        termsCheckBox.pack(padx=10, pady=20)

        self.root.mainloop()
