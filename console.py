#!/usr/bin/python3
"""
    console
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """cmd module"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """empty command to loop empty interactive shell"""
        return False

    def do_EOF(self, line):
        """Exis the interactive shell"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
