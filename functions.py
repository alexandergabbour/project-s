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
#
#                                                          FUNCTIONS

import subprocess

#throw whatever functions that the shortcut buttons need to reference down here. will need some organization in the future as this scales.
class pyScripts(): #need to inherit from a class in a seperate file for modularity
    def print_hello():
        print('hello')

    def print_goodbye():
        print('goodbye')

class bashScripts():
    
    def test():
        subprocess.call("./bash/test-script.sh", shell=True)

    def init():
        subprocess.call("./bash/linux-init.sh", shell=True)