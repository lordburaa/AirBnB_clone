#!/usr/bin/python3
"""console log"""
import cmd
import json
import shlex
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.user import User
from models import storage
import re


class HBNBCommand(cmd.Cmd):
    """cmd interactive shell"""
    prompt = '(hbnb) '
    clss_name = {"BaseModel": BaseModel, "User": User,
                'State': State, 'City': City, 'Place': Place,
                'Review': Review, 'Amenity': Amenity}

    def default(self, arg):
        """default when no argument is passed"""
        val_dict = {
                "all": self.do_all,
                "count": self.do_count,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "update": self.do_update
                }
        arg = arg.strip()
        values = arg.split(".")
        if len(values) != 2:
            cmd.Cmd.default(self, arg)
            return 
        class_name = values[0]
        command = values[1].split("(")[0]
        line = ""

        if (command == "update" and values[1].split("(")[1][-2] == "}"):
            inputs = values[1].split("(")[1].split(",", 1)
            inputs[0] = shlex.split(inputs[0])[0]
            line = "".join(inputs)[0:-1]
            line = class_name + " " + line
            self.do_update2(line.strip())
            return
        try:
            inputs = values[1].split("(")[1].split(",")
            num = 0
            for num in range(len(inputs)):
                if (num != len(inputs) - 1):
                    line = line + " " + shlex.split(inputs[num])[0]
                else:
                    line = line + " " + shlex.split(inputs[num][0: -1])[0]
        except IndexError:
            inputs = ""
            line = ""
        line = class_name + line
        if command in val_dict.keys():
            val_dict[command](line.strip())

    def help(self):
        """Help command"""
        return True

    def emptyline(self):
        """empty line"""
        pass

    def do_create(self, cls):
        """
        Create new instance of class
        variable lis_t => list_t[0] is class name to be created

        """
        list_t = list(cls.split(' '))
        if not cls:
            print("** class name missing **")
        elif list_t[0] not in self.clss_name:
            print("** class doesn't exist **")
        else:
            obj = self.clss_name[list_t[0]]()
            print(obj.id)
            storage.new(obj)
            storage.save()
    
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
            """REFRACTE THE BELOW ELSE CODE """
            dic_t = {}
            storage.reload()
            dic_t = storage.all()
            key = list_t[0] + '.' + list_t[1]
            if key in dic_t:
                print(str(dic_t[key]))
            else:
                print("** no instance found **")
            
            
            """END OF THE REFRACTOR """
            """
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
            """
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
            storage.reload()
            dic_t = storage.all()
            key = list_t[0] + '.' + list_t[1]
            if key in dic_t:
                del dic_t[key]
                storage.save()
            else:
                print("** no instance found **")

            """
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
            """

    def do_all(self, clss):
        """prints all string representation of an instance
        use bare `all` command to print all instance in the storage
        use `all command_base` if command_base is exist in the storage
        it will print all the instance
        """
        list_t = []

        arg = list(clss.split(' '))
        storage.reload()
        dic_t = storage.all()
        flag = 0
        if not clss:
            for key, value in dic_t.items():
                flag = 1
                list_t.append(str(value))
        else:
            class_name = arg[0]
            for key, value in  dic_t.items():
                base, idd = key.split('.')
                if base == class_name:
                    flag = 1
                    list_t.append(str(value))
        if flag == 1:
            print(list_t)
        else:
            print("** class doesn't exist **")

        """if not clss:
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
                        if (k == base and k == arg[0]):
                            lss = self.clss_name[k]
                            list_t.append(str(lss(**value)))
                            break
            unq = list(set(list_t))
            print(unq)
        else:
            print("** class doesn't exist **")
        """
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
                    if (list_t[3].startswith('"') and list_t[3].endswith('"')) or (list_t[3].startswith("'") and list_t[3].endswith("'")):
                        att_value = list_t[3][1:-1]
                        value[list_t[2]] = att_value
                    else:
                        value[list_t[2]] = (list_t[3])
                        #remove the strip
                    json_obj[key] = value
                    with open('file.json', 'w') as w:
                        json.dump(json_obj, w)

    def do_count(self, arg):
        """count func"""
        count = 0
        json_dict = {}
        list_t = arg.split(" ")
        with open('file.json') as w:
            json_dict = json.load(w)
        if json_dict:
            for key, value in json_dict.items():
                base, idd = key.split(".")
                if base == list_t[0]:
                    count = count + 1
        print(count)

    def do_update2(self, arg):
        """
        update
        """
        if not arg:
            print("** class name missing **")
            return 
        my_dictionary = "{" + arg.split("{")[1]
        my_data = shlex.split(arg)
        dic_t = {}
        try:
            with open('file.json') as r:
                dic_t = json.load(r)
        except FileNotFoundError:
            pass
        if my_data[0] not in self.clss_name:
            print("** class doesn't exist **")
            return
        if (len(my_data) == 1):
            print("** instance id missing **")
            return
        try:
            key = my_data[0] + "." + my_data[1]
            dic_t[key]
                
        except KeyError:
            print("** no instance found **")
            return
        
        if (my_dictionary == "{"):
            print("** attribute name missing **")
            return
        my_dictionary = my_dictionary.replace("\'", "\"")
        my_dictionary = json.loads(my_dictionary)
        my_instance = dic_t[key]

        con = {**my_dictionary, **my_instance}
        dic_t[key] = con
        # save to the file
        with open("file.json", "w") as rw:
            json.dump(dic_t, rw)

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """ end of the file """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
