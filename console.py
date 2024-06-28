#!/usr/bin/python3
"""console log"""
import cmd
import json
from models.base_model import BaseModel
from models import storage
import re

class HBNBCommand(cmd.Cmd):
    """cmd interactive shell"""
    prompt = '(hbnb) ' 
    clss_name = ["BaseModel"]
    
    def default(self, line):
        print("default printed")
    
    def help(self):
        return True

    def emptyline(self):
        return cmd.Cmd.emptyline(self)

    def do_create(self, cls):
        """create new instance of BaseModel"""
        if not cls:
            print("** class name missing **")
        elif cls not in self.clss_name:
            print("**class doesn't exist **")
        else:
            base = BaseModel()
            print(base.id)
            base.save()
    def do_show(self, clss):
        """prints the string representation of an instance"""
        list_t = list(clss.split(' '))
        if len(list_t) ==  0:
            print("class name is missing ")
        elif list_t[0] not in self.clss_name:
            print("class doesn't exist **")
        elif len(list_t) <= 1:
            print("** instance id missing **")
        else:
            with open('file.json') as r:
                json_obj = json.load(r)
                for key, value in json_obj.items():
                    base, idd = key.split('.')
                    if (idd == list_t[1]):
                        print(BaseModel(**value))
    
    def do_destroy(self, clss):
        """destroy an instance"""
        list_t = list(clss.split(' '))
        if len(list_t) == 0:
            print("** class name is missing **")
        elif list_t[0] not in self.clss_name:
            print("** class doesn't exist **")
        elif len(list_t[0]) == 1:
            print("** instance id missing **")
        else:
            with open('file.json', 'r') as r:
                json_obj = json.load(r)
                for key, value in json_obj.items():
                    base, idd = key.split('.')
                    if idd == list_t[1]:
                        del[json_obj[key]]
                        print(json_obj)
                        with open('file.json', 'w') as w:
                            json.dump(json_obj)

    def do_all(self, clss):
        """prints all string representation of all instance based or not on the class name"""
        list_t = []
        dic_t = {}
        if clss not in self.clss_name:
            print("** class doesn't exist **")
        else:
            arg = list(clss.split(' '))
            with open('file.json', 'r') as r:
                json_obj = json.load(r)
                for key, value in json_obj.items():
                    base, idd = key.split('.')
                    if (arg[0] ==  base):
                        list_t.append(str(BaseModel(**value)))
                print(list_t)
                
    def do_update(self, arg):
        """updates an instance based on the class name and id"""
        list_t = list(arg.split(' '))

        if len(list_t) == 0:
            print("** class name is missing **")
        elif list_t[0] not in self.clss_name:
            print("** class doesn't exist **")
        elif len(list_t) == 1:
            print("** instance id missing **")
        else:
            sr = {}
            with open('file.json', 'r+') as r:
                json_obj = json.load(r)
                key = list_t[0] + '.' + list_t[1]
                if key not in json_obj:
                    print("** no instance found **")
                elif len(list_t) == 2:
                    print("** attribute name missing **")
                elif len(list_t) == 3:
                    print("** value missing **")
                else:
                    value = json_obj[key]
                    value[list_t[2]] = list_t[3]
                    json_obj[key] = value
                    sr = json_obj.copy()
            if sr:
                with open('file.json', 'w') as w:
                    json.dump(sr, w)

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """ end of the file """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
