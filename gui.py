#!/usr/bin/python3

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                                                                                                                           #
# ________    ________      ________         ___      _______       ________      _________                   ________      #
#|\   __  \  |\   __  \    |\   __  \       |\  \    |\  ___ \     |\   ____\    |\___   ___\                |\   ____\     #
#\ \  \|\  \ \ \  \|\  \   \ \  \|\  \      \ \  \   \ \   __/|    \ \  \___|    \|___ \  \_|  ____________  \ \  \___|_    #
# \ \   ____\ \ \   _  _\   \ \  \\\  \   __ \ \  \   \ \  \_|/__   \ \  \            \ \  \  |\____________\ \ \_____  \   #
#  \ \  \___|  \ \  \\  \|   \ \  \\\  \ |\  \\_\  \   \ \  \_|\ \   \ \  \____        \ \  \ \|____________|  \|____|\  \  #
#   \ \__\      \ \__\\ _\    \ \_______\\ \________\   \ \_______\   \ \_______\       \ \__\                   ____\_\  \ #
#    \|__|       \|__|\|__|    \|_______| \|________|    \|_______|    \|_______|        \|__|                  |\_________\#
#                                                                                                               \|_________|#
#                                                             v0                                                            #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
                                                                                                                           
                                                                                                                           
import customtkinter
from functions import pyScripts
from functions import bashScripts
from const import *

customtkinter.set_appearance_mode('system')
customtkinter.set_default_color_theme('blue')


#layout of the interface
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry(config.dflt_windowSize)
        self.title('Project-S')
        self.grid_columnconfigure(0, weight=0) #weight set to 0 to collapse the column to the size of the frame
        self.grid_columnconfigure(1, weight=1) #weight set to 1 to take up the remaining space
        self.grid_rowconfigure(0, weight=1)

        self.menu = Menu(self)
        self.menu.grid(row=0, column=0, padx=20, pady=20, sticky='nsw')

        self.SCCats = SCCats(self)
        self.SCCats.grid(row=0, column=1, padx=20, pady=20, sticky='nsew')

#menu buttons
class Menu(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        c_rad = 10
        b_size = 30
        b_colour = 'transparent'

        self.home = customtkinter.CTkButton(self, font=(config.app_font, config.app_fontSize), fg_color=b_colour, corner_radius=c_rad, height=b_size, width=b_size, text='home')
        self.home.grid(row=0, column=0, padx=10, pady=10, sticky='ew')

        self.favourites = customtkinter.CTkButton(self, font=(config.app_font, config.app_fontSize), fg_color=b_colour, corner_radius=c_rad, height=b_size, width=b_size, text='favourites')
        self.favourites.grid(row=1, column=0, padx=10, pady=10, sticky='ew')

        self.profile = customtkinter.CTkButton(self, font=(config.app_font, config.app_fontSize), fg_color=b_colour, corner_radius=c_rad, height=b_size, width=b_size, text='profile')
        self.profile.grid(row=2, column=0, padx=10, pady=10, sticky='ew')

        self.settings = customtkinter.CTkButton(self, font=(config.app_font, config.app_fontSize), fg_color=b_colour, corner_radius=c_rad, height=b_size, width=b_size, text='settings')
        self.settings.grid(row=3, column=0, padx=10, pady=10, sticky='ew')    

#shortcuts categories contents
class SCCats(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)

        self.category1 = Cat1(self)
        self.category1.grid(row=0, column=0, padx=10, pady=10, sticky='ew')

        self.category2 = Cat2(self)
        self.category2.grid(row=1, column=0, padx=10, pady=10, sticky='ew')


#shortcuts to go into category 1
class Cat1(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.label = customtkinter.CTkLabel(self, font=(config.app_font, config.app_fontSize), text='String Functions')
        self.label.grid(row=0, column=0, padx=(15, 0), pady=(20, 10), columnspan=2, sticky='w')

        self.sc1 = customtkinter.CTkButton(self, font=(config.app_font, config.app_fontSize), height=config.sc_height, width=config.sc_width, text='Hello', command=pyScripts.print_hello)
        self.sc1.grid(row=1, column=0, padx=20, pady=20)

        self.sc2 = customtkinter.CTkButton(self, font=(config.app_font, config.app_fontSize), height=config.sc_height, width=config.sc_width, text='Goodbye', command=pyScripts.print_goodbye)
        self.sc2.grid(row=1, column=1, padx=20, pady=20)

#shortcuts to go into category 2
class Cat2(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.label = customtkinter.CTkLabel(self, font=(config.app_font, config.app_fontSize), text='Math Operations')
        self.label.grid(row=0, column=0, padx=(15, 0), pady=(20, 10), columnspan=2, sticky='w')

        self.sc1 = customtkinter.CTkButton(self, font=(config.app_font, config.app_fontSize), height=config.sc_height, width=config.sc_width, text='3+4', command=pyScripts.add)
        self.sc1.grid(row=1, column=0, padx=20, pady=20)

        self.sc2 = customtkinter.CTkButton(self, font=(config.app_font, config.app_fontSize), height=config.sc_height, width=config.sc_width, text='6-2', command=pyScripts.subtract)
        self.sc2.grid(row=1, column=1, padx=20, pady=20)

#run app
app = App()
app.mainloop()