#!/usr/bin/python3

#from typing import Optional, Tuple, Union
from typing import Optional, Tuple, Union
import customtkinter

# customtkinter.set_appearance_mode("system")
# customtkinter.set_default_color_theme("blue")


#outline of the interface
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self = customtkinter.CTk()
        self.geometry("1200x800")
        self.grid_columnconfigure((0, 1), weight=1)

        self.menu = Menu(self)
        self.menu.grid(row=0, column=0, padx=20, pady=20, sticky="nsw")

        self.sc_cats = SC_cats(self)
        self.sc_cats.grid(row=0, column=1, padx=20, pady=20, sticky="ew")

#menu contents
class Menu(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.home = customtkinter.CTkButton(self, text="home")
        self.home.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")

        self.favourites = customtkinter.CTkButton(self, text="favourites")
        self.favourites.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")        

#shortcuts categories contents
class SC_cats(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

app = App()
app.mainloop()
