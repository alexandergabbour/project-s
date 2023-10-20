#!/usr/bin/python3

import subprocess

#throw whatever functions that the shortcut buttons need to reference down here. will need some organization in the future as this scales.
class pyScripts():
    def print_hello():
        print('hello')

    def print_goodbye():
        print('goodbye')

    def add():
        x=3
        y=4
        print(x+y)
    
    def subtract():
        x=7
        y=2
        print(x-y)


class bashScripts():

    def script1(): #test function: bash stuff from user would go in the triple quotes below #! /bin/bash
        hello = '''
        #! /bin/bash
        
        echo 'hello world'
        '''
        subprocess.call(['bash', '-c', hello])
    
    def linux_init():

        #in this case 'init' stores the bash script. this could be stored in a seperate class and called by subprocess in the bashScripts class
        init = '''
        #! /bin/bash

        echo 'initializing your linux machine...'

        echo 'installing predefined software...'

        sudo apt update && sudo apt upgrade

        sudo snap install --classic code

        sudo snap install spotify
        '''
        subprocess.call(['bash', '-c', init])