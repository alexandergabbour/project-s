#!/usr/bin/python3

from typing import Optional, Tuple, Union
import customtkinter

from functions import *

customtkinter.set_appearance_mode('system')
customtkinter.set_default_color_theme('blue')


#outline of the interface
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self = customtkinter.CTk()
        self.geometry('1200x800')
        self.title('Project-S')
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=5)

        self.menu = Menu(self)
        self.menu.grid(row=0, column=0, padx=20, pady=20, sticky='nsw')

        self.sc_cats = SC_cats(self)
        self.sc_cats.grid(row=0, column=1, padx=20, pady=20, sticky='nsw')

#menu buttons
class Menu(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.home = customtkinter.CTkButton(self, text='home')
        self.home.grid(row=0, column=0, padx=10, pady=(10, 0), sticky='w')

        self.favourites = customtkinter.CTkButton(self, text='favourites')
        self.favourites.grid(row=1, column=0, padx=10, pady=(10, 0), sticky='w')

        self.profile = customtkinter.CTkButton(self, text='profile')
        self.profile.grid(row=2, column=0, padx=10, pady=(10, 0), sticky='w')

        self.settings = customtkinter.CTkButton(self, text='settings')
        self.settings.grid(row=3, column=0, padx=10, pady=(10, 0), sticky='w')    

#shortcuts categories contents
class SC_cats(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.category1 = Cat1(self)
        self.category1.grid(row=0, column=0, padx=10, pady=10, sticky='ew')

        self.category2 = Cat2(self)
        self.category2.grid(row=1, column=0, padx=10, pady=10, sticky='ew')


#shortcuts to go into category 1
class Cat1(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.label = customtkinter.CTkLabel(self, text='Category 1')
        self.label.grid(row=0, column=0, padx=(15, 0), pady=(20, 10), columnspan=2, sticky='w')

        self.sc1 = customtkinter.CTkButton(self, text='Shortcut 1', command=print_hello)
        self.sc1.grid(row=1, column=0, padx=10, pady=10)

        self.sc2 = customtkinter.CTkButton(self, text='Shortcut 2', command=print_goodbye)
        self.sc2.grid(row=1, column=1, padx=10, pady=10)

#shortcuts to go into category 2
class Cat2(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.label = customtkinter.CTkLabel(self, text='Category 2')
        self.label.grid(row=0, column=0, padx=(15, 0), pady=(20, 10), columnspan=2, sticky='w')

        self.sc1 = customtkinter.CTkButton(self, text='Shortcut 1', command=add)
        self.sc1.grid(row=1, column=0, padx=10, pady=10)

        self.sc2 = customtkinter.CTkButton(self, text='Shortcut 2', command=subtract)
        self.sc2.grid(row=1, column=1, padx=10, pady=10)

#run app
app = App()
app.mainloop()
