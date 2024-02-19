#!/usr/bin/python3
"""
    console
"""
import cmd


class cm(cmd.Cmd):
    """cmd module"""
    def do_quit(self):
        """quit interuption signal"""
        return True
 
    def do_EOF(self, line):
        """Exis the interactive shell"""
        return True


if __name__ == "__main__":
    cm().cmdloop()
