#!/usr/bin/python3
"""
    console
"""
import json
import copy
import cmd
import os
import re
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from models import storage

class HBNBCommand(cmd.Cmd):
    """cmd module"""
    prompt = "(hbnb) "
    clss = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

    def do_create(self, line):
        """command to create new instnace of BaseMode save to the FILE and print id"""
        list_t = line.split()
        dic_t = {"BaseModel": BaseModel(), "User": User(), "State": State(), "City": City(), "Amenity": Amenity(), "Place": Place(), "Review": Review()}

        if len(list_t) == 0:
            print("** class name missing **")
        elif list_t[0] not in self.clss:
            print("** class doesn't exist **")
        else:
            obj = dic_t[list_t[0]]
            obj.save()
            print(obj.id)
    
    def default(self, line):
        """catch commands if nothing else matches then."""
        self._precmd(line)


    def precmd(self, line):
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not match:
            return line
        classname = match.group(1)
        method = match.group(2)
        args = match.group(3)

        match_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_uid_and_args:
            uid = match_uid_and_args.group(1)
            attr_or_dict = match_uid_and_args.group(2)
        else:
            uid = args
            attr_or_dict = False

        attr_and_value = ""
        if method == "update" and attr_or_dict:
            match_dict = re.search('^({.*})$', attr_or_dict)
            if match_dict:
                self.update_dict(classname, uid, match_dict.group(1))
                return ""

            match_attr_and_value = re.search('^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict)
            if match_attr_and_value:
                attr_and_value = (match_attr_and_value.group(1) or "") + " " + (match_attr_and_value.group(2) or "")
        command = method + " " + classname + " " + uid + " " + attr_and_value
        self.onecmd(command)
        return command

    def do_show(self, line):
        """show Method"""
        storage.reload()
        show_id = storage.all()
        list_t = line.split()
        if len(list_t) < 1:
            print("** class name missing **")
        elif list_t[0] not in self.clss:
            print("** class doesn't exist **")
        elif len(list_t) == 1:
            print("** instance id missing **")
        else:
            check_dic = str(list_t[0]) + "." + str(list_t[1])
            # print(check_dic)
            if check_dic not in show_id:
                print("** no instance found **")
            else:
                #showing the instance value
                print(show_id[check_dic])


    def do_destroy(self, line):
        """destroy command"""
        storage.reload()
        dic_t = storage.all()
        list_t = line.split()


        if len(list_t) == 0:
            print("** class name missing **")
        elif list_t[0] not in self.clss:
            print("** class doesn't exist **")
        elif len(list_t) == 1:
            print("** instance id missing **")
        else:

            del_id = str(list_t[0]) + "." + str(list_t[1])

            if del_id not in dic_t:
                print("** no instance found **")
            else:

                del storage.all()[del_id]
                storage.save()
                storage.reload()

    """
    def do_all(self, line):
        Print all string representaiton of all instnaces based or not on the class name
        storage.reload()
        all_dict = storage.all()
        list_t = line.split()
        
        if len(list_t) == 0:
                li = []
                for key, value in all_dict.items():
                    li.append(str(all_dict[key]))
                
                if len(li) != 0:
                    print("[",end="")
                    l = 0
                    
                    for item in li:
                        print("\"", end="")
                        print(item, end="")
                        print("\"", end="")
                        
                        if l != len(li) - 1:
                            print(", ", end="")
                        l = l + 1
                        
                    print("]")
                

        else:
            if list_t[0] in self.clss:
                li = []
                
                for key, value in all_dict.items():
                    if type(key).__name__ == list_t[0]:

                        li.append(str(all_dict[key]))
                
                if len(li) != 0:
                    l = 0
                    print("[", end="")
                    
                    for item in li:
                        print("\"", end="")
                        print(item, end="")
                        print("\"", end="")
                        
                        if l != len(li) - 1:
                            print(", ", end="")
                        l = l + 1
                        
                    print("]")

            else:
                print("** class doesn't exist **")
    """
    def do_all(self, line):
        """prints all string representatio of lal instnace
        """
        if line != "":
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                nl = [str(obj) for key, obj in storage.all().items() if type(obj).__name__ == words[0]]
                print(nl)
        else:
            new_list = [str(obj) for key, obj in storage.all().items()]
            print(new_list)

    def do_update(self, line):
        """Update an instance based on the class name and id by adding or updating attribute"""
        storage.reload()
        list_t = line.split()
        dic_obj = storage.all()

        if len(list_t) >= 2:
            
            check_id = str(list_t[0]) + "." + str(list_t[1])
        
        if len(list_t) == 0:
            print("** class name missing **")
        elif list_t[0] not in self.clss:
            print("** class doesn't exist **")
        elif len(list_t) == 1:
            print("** instance id missing **")
        elif check_id not in dic_obj:
            #checking wheter id instnace is exist
            print("** no instance found **")

        elif len(list_t) == 2:
            print("** attribute name missing **")
        elif len(list_t) == 3:
            print("** value missing **")
        elif len(list_t) == 4:

            dict_copy = dic_obj.copy()
            
            for dic_t, value in dict_copy.items():
                base_str, id_str = dic_t.split(".")
                
                if id_str == list_t[1]:

                    setattr(value, list_t[2], list_t[3])
                    storage.new(value) 
                    storage.save()
                    storage.reload() 
                else:
                    pass
                    
        else:
            pass

    def do_count(self, line):
        """count number of instance"""
        list_t = line.split(' ')
        cl = storage.all()
        cnt = 0
        for key in cl.items():
            tmp = key[0]
            ky = tmp.split(".")
            if list_t[0] == ky[0]:
                cnt = cnt + 1
        
        print(cnt)

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """empty command to loop empty interactive shell"""
        pass

    def do_EOF(self, line):
        """Exis the interactive shell"""
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
