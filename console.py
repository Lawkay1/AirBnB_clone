#!/usr/bin/python3
"""cmd interpreter"""


import cmd


class HBNBCommand(cmd.Cmd):
    """cmd hbnh"""
    intro = 'Welcome to the AirBnB shell.   Type help or ? to list commands.\n'
    prompt = '(hbnb) '

    def emptyline(self):
        """empty line"""

    def do_EOF(self, arg):
        """exit the program"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
