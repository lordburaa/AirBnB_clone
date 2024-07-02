#!/usr/bin/python3
"""console log"""
import cmd
import json
from models.base_model import BaseModel
from models.user import User
from models import storage
import re


class HBNBCommand(cmd.Cmd):
    """cmd interactive shell"""
    prompt = '(hbnb) '
    clss_name = {"BaseModel": BaseModel, "User": User } # changing from list to dictionary


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
        list_t = list(cls.split(' '))
        if not cls:
            print("** class name missing **")
        elif list_t[0] not in self.clss_name:
            print("** class doesn't exist **")
        else:
            for clss_key, value in self.clss_name.items():
                if clss_key == list_t[0]:
                    v = self.clss_name[clss_key]
                    base = v()
                    break
            print(base.id)
            base.save()

    def do_show(self, clss):
        """prints the string representation of an instance
        based on  the CLASS name"""
        list_t = list(clss.split(' '))
        if not clss:
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
                    le = 0
                    if base_n_id not in json_obj:
                        flag = 1
                    for key, value in json_obj.items():
                        base, idd = key.split('.')
                        base_n_id = list_t[0] + '.' + list_t[1]

                        for k, v in self.clss_name.items():
                            if (base_n_id == key and k == base):
                                va = self.clss_name[k]
                                print(str(va(**value)))
                                le = 1
                                break
                        if (le == 1):
                            break
                    if flag:
                        print("** no instance found **")
            except FileNotFoundError:
                print("** no instance found **")

    def do_destroy(self, clss):
        """destroy an instance basd on the class name"""
        list_t = list(clss.split(' '))
        if not clss:
            print("** class name missing **")
        elif list_t[0] not in self.clss_name:
            print("** class doesn't exist **")
        elif len(list_t) == 1:
            print("** instance id missing **")
        else:
            json_obj = {}
            flag = 0
            try:
                with open('file.json', 'r') as r:
                    json_obj = json.load(r)
                    base_n_id = list_t[0] + '.' + list_t[1]
                    br = 0
                    for key, value in json_obj.items():
                        for k, v in self.clss_name.items():

                            if key == base_n_id:
                                flag = 1
                                del json_obj[key]
                                br = 1
                                break
                        if br:
                            break
            except FileNotFoundError:
                flag = 0
            if flag == 1:
                with open('file.json', 'w') as w:
                    json.dump(json_obj, w)
            else:
                print("** no instance found **")

    def do_all(self, clss):
        """prints all string representation of an instance 
        use bare `all` command to print all instance in the storage
        use `all command_base` if command_base is exist in the storage it will print all the instance
        """
        list_t = []

        arg = list(clss.split(' '))
        if not clss:
            try:
                with open('file.json', 'r') as r:
                    json_obj = json.load(r)
                    for key, value in json_obj.items():
                        base, idd = key.split('.')
                        for k, v in self.clss_name.items():
                            if base == k:
                                inss = self.clss_name[k]
                                list_t.append(str(inss(**value)))
                    print(list_t)
            except FileNotFoundError:
                print(list_t)
        elif arg[0] in self.clss_name:
            with open('file.json', 'r') as r:
                json_obj = json.load(r)
                for key, value in json_obj.items():
                    base, idd = key.split('.')
                    for k, v in self.clss_name.items():
                        
                        if (k == base and k==arg[0]):
                            lss = self.clss_name[k]
                            list_t.append(str(lss(**value)))
                            break
            unq = list(set(list_t))
            print(unq)
        else:
            print("** class doesn't exist **")
    

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
                    for keyy, valuee in json_obj.items():
                        if keyy == key:
                            value = json_obj[key]
                            break
                    if (list_t[3].startswith('"') and list_t[3].endswith('"')) or\
                       (list_t[3].startswith("'") and list_t[3].endswith("'")):
                        att_value = list_t[3][1:-1]
                        value[list_t[2]] = att_value
                    else:
                        value[list_t[2]] = list_t[3].strip()
                    json_obj[key] = value
                    with open('file.json', 'w') as w:
                        json.dump(json_obj, w)

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """ end of the file """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
