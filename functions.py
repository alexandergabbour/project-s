#!/usr/bin/python3

import subprocess

#throw whatever functions that the shortcut buttons need to reference down here. will need some organization in the future as this scales.
class pyScripts():
    def print_hello():
        print('hello')

    def print_goodbye():
        print('goodbye')


class bashScripts():
    
    def test():
        subprocess.call("./bash/test-script.sh", shell=True)

    def init():
        subprocess.call("./bash/linux-init.sh", shell=True)