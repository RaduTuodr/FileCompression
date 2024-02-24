import customtkinter
from pages import Home

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

Home.HomeUI(root)
