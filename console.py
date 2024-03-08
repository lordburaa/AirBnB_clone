#!/usr/bin/python3
"""
    console
"""
import json
import copy
import cmd
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
from models import storage

class HBNBCommand(cmd.Cmd):
    """cmd module"""
    prompt = "(hbnb) "
    clss = ["BaseModel", "User", "Amenity"]

    def do_create(self, line):
        """command to create new instnace of BaseMode save to the FILE and print id"""
        list_t = line.split()
        dic_t = {"BaseModel": BaseModel(), "User": User(), "Amenity": Amenity()}

        if len(list_t) == 0:
            print("** class name missing **")
        elif list_t[0] not in self.clss:
            print("** class doesn't exist **")
        else:
            obj = dic_t[list_t[0]]
            obj.save()
            print(obj.id)
    
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


    def do_all(self, line):
        """Print all string representaiton of all instnaces based or not on the class name"""
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
