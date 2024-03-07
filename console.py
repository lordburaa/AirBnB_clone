#!/usr/bin/python3
"""
    console
"""
import json
import copy
import cmd
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage

class HBNBCommand(cmd.Cmd):
    """cmd module"""
    prompt = "(hbnb) "
    
    def do_create(self, line):
        """command to create new instnace of BaseMode save to the FILE and print id"""
        list_t = line.split()

        if len(list_t) == 0:
            print("** class name missing **")
        elif list_t[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            obj = BaseModel()
            obj.save()
            print(obj.id)
    
    def do_show(self, line):
        """show Method"""
        show_id = storage.all()
        list_t = line.split()
        if len(list_t) < 1:
            print("** class name is missing **")
        elif list_t[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(list_t) == 1:
            print("** instance id missing **")
        else:
            check_dic ="BaseModel."+ str(list_t[1])
            # print(check_dic)
            if check_dic not in show_id:
                print("** no instance found **")
            else:
                #showing the instance value
                print(show_id[check_dic])


    def do_destroy(self, line):
        """destroy command"""

        dic_t = storage.all()
        list_t = line.split()
        rd = {}

        
        if len(list_t) < 1:
            print("** class name is missing **")
        elif list_t[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(list_t) < 2:
            print("** instance id missing **")
        else:
            del_id = "BaseModel." + str(list_t[1])
            dic_test = ""
            with open("file.json", "r") as r:
                dic_test = json.load(r)

            if del_id not in dic_test:
                print("** no instance found **")
            else:

                del storage.all()[del_id]
                storage.save()
                #dic = dic_t.copy()
                #save the ins


    def do_all(self, line):
        """Print all string representaiton of all instnaces based or not on the class name"""
        all_dict = storage.all()
        list_t = line.split()
        #using the for loop
        #print(all_dict)
        dic_t = all_dict.copy()
        if len(list_t) == 0:
                li = []
                for key, value in dic_t.items():
                    
                         
                    li.append(str(all_dict[key]))
                if len(li) != 0:

                    print(li)
        else:
            if list_t[0] == "BaseModel":
                li = []
                for key, value in all_dict.items():
                    li.append(str(all_dict[key]))
                if len(li) != 0:

                    print(li)
            else:
                print("** class doesn't exist **")

    def do_update(self, line):
        """Update an instance based on the class name and id by adding or updating attribute"""
        list_t = line.split()
        dic_obj = storage.all()

        if len(list_t) >= 2:

            check_id = "BaseModel."+ str(list_t[1])
        
        if len(list_t) < 1:
            print("** class name missing **")
        elif list_t[0] != "BaseModel":
            # checkign from the dictionary 
            print("** class doesn't exist **")
        elif len(list_t) < 2:
            print("** instance id missing **")
        elif check_id not in dic_obj:
            #checking wheter id instnace is exist
            print("** no instance found **")

        elif len(list_t) < 3:
            print("** attribute name is missing **")
        elif len(list_t) < 4:
            print("** value missing **")
        elif len(list_t) == 4:

            dict_copy = dic_obj.copy()
            tmp = ""
            for dic_t, value in dict_copy.items():
                base_str, id_str = dic_t.split(".")
                tmp = dic_t
                if id_str == list_t[1]:
                    new = ""       
                    st_r = str(list_t[3])
                    if list_t[3].startswith('"') and list_t[3].endswith('"'):

                        new = list_t[3][1:-1]
                    else:
                        new = str(list_t[3])
                    setattr(value, list_t[2], new)
                    storage.new(value) 
                    storage.save()
                    # t = dic_obj[dic_t]
                    # sv[dic_t] = t.to_dict()

                    
                else:
                    pass
                    # sv[dic_t] = value.to_dict()

            # if os.path.exists("file.json"):
            #    os.remove("file.json")
            # else:
            #    pass
           # with open("file.json", "w") as w:
            #    json.dump(sv, w)
            # for key, value in sv.items():
            #    new = BaseModel value)
            #    new.save()
            #print(dic_obj[tmp].to_dict())
            # instantiate new class for the new class
            
            

                    
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
