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
        """default when no argument is passed"""
        pass

    def help(self):
        """Help command"""
        return True

    def emptyline(self):
        """empty line"""
        pass

    def do_create(self, cls):
        """create new instance of BaseModel and Save to JSON File"""
        if not cls:
            print("** class name missing **")
        elif cls not in self.clss_name:
            print("** class doesn't exist **")
        else:
            base = BaseModel()
            print(base.id)
            base.save()

    def do_show(self, clss):
        """prints the string representation of an instance
        based on  the CLASS name"""
        list_t = list(clss.split(' '))
        print(list_t)
        if len(list_t) == 0:
            print("** class name missing **")
        elif list_t[0] not in self.clss_name:
            print("** class doesn't exist **")
        elif len(list_t) == 1:
            print("** instance id missing **")
        else:
            try:
                with open('file.json', 'r') as r:
                    json_obj = json.load(r)
                    base_n_id = list_t[0] + '.' + list_t[1]
                    flag = 0
                    if base_n_id not in json_obj:
                        flag = 1
                    for key, value in json_obj.items():
                        if (base_n_id == key):
                            print(BaseModel(**value))
                    if flag:
                        print("** no instance found **")
            except FileNotFoundError:
                print("** no instance found **")

    def do_destroy(self, clss):
        """destroy an instance basd on the class name """
        list_t = list(clss.split(' '))
        if not clss:
            print("** class name missing **")
        elif list_t[0] not in self.clss_name:
            print("** class doesn't exist **")
        elif len(list_t) == 1:
            print("** instance id missing **")
        else:
            json_obj = {}
            with open('file.json', 'r') as r:
                json_obj = json.load(r)
                for key, value in json_obj.items():
                    base, idd = key.split('.')
                    if idd == list_t[1]:
                        del json_obj[key]
                        break
            with open('file.json', 'w') as w:
                json.dump(json_obj, w)

    def do_all(self, clss):
        """prints all string representation of all instance
        based or not on the class name"""
        list_t = []
        if clss not in self.clss_name:
            print("** class doesn't exist **")
        else:
            arg = list(clss.split(' '))
            try:
                with open('file.json', 'r') as r:
                    json_obj = json.load(r)
                    for key, value in json_obj.items():
                        base, idd = key.split('.')
                        if (arg[0] == base):
                            list_t.append(str(BaseModel(**value)))
                    print(list_t)
            except FileNotFoundError:
                print(list_t)

    def do_update(self, arg):
        """updates an instance based on the class name and id"""
        list_t = list(arg.split(' '))

        if not arg:
            print("** class name missing **")
        elif list_t[0] not in self.clss_name:
            print("** class doesn't exist **")
        elif len(list_t) == 1:
            print("** instance id missing **")
        else:
            json_obj = {}
            with open('file.json', 'r+') as w:
                json_obj = json.load(w)
                key = list_t[0] + '.' + list_t[1]
                if key not in json_obj:
                    print("** no instance found **")
                elif len(list_t) == 2:
                    print("** attribute name missing **")
                elif len(list_t) == 3:
                    print("** value missing **")
                else:
                    att_name = re.search("^[\\w_]+", list_t[2])
                    att_value = re.search("\\w+", list_t[3])
                    value = json_obj[key]
                    value[att_name.group(0)] = att_value.group(0)
                    json_obj[key] = value
                    w.seek(0)
                    json.dump(json_obj, w)

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """ end of the file """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
