#!/usr/bin/python3
"""
    console
"""
import json
import copy
import cmd
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
        
        
        if len(list_t) < 1:
            print("** class name is missing **")
        elif list_t[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(list_t) < 2:
            print("** instance id missing **")
        else:
            del_id = "BaseModel." + list_t[1]
            
            if del_id not in dic_t:
                print("** no instance found **")
            else:
                #del
                del dic_t[del_id]
                #save the ins
                # .save()

    def do_all(self, line):
        """Print all string representaiton of all instnaces based or not on the class name"""
        all_dict = storage.all()
        list_t = line.split()
        #using the for loop
    
        if len(list_t) == 0:
                li = []
                for key, value in all_dict.items():
                    li.append(str(value))
                print(li)
        else:
            if list_t[0] == "BaseModel":
                li = []
                for key, value in all_dict.items():
                    li.append(str(value))
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

            
            for dic_t, value in dict_copy.items():
                base_str, id_str = dic_t.split(".")
                if id_str == list_t[1]:
                    #dic may conatin the memory addres
                    
                    setattr(value, str(list_t[2]), str(list_t[3]))
                    # obj.save()
                    # print(obj)
                    # break
                    
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
