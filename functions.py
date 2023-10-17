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
        u=6
        w=2
        print(u-w)

class bashScripts():

    def script1():
        hello = '''
        #! /bin/bash
        echo 'hello world'

        '''
        subprocess.call(['bash', '-c', hello])