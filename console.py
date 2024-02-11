#!/usr/bin/env python3
"""
Command line interpreter

This module is runs the cmd module to allow the user
to Interact with the system
"""
import cmd
import re
import readline

from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

print(dir(cmd.Cmd))


class HBNBCommand(cmd.Cmd):
    prompt = "(Type your command here): "

    CLASSES = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

    def emptyline(self):
        """This function does nothing on an empty line on the cmd interpreter """
        pass

    def do_EOF(self, arg):
        """Exit the console by holding (ctrl+D) command"""
        print()
        return True

    def do_quit(self, arg):
        """This quits or exits the program"""
        return True

    def help_quit(self):
        """ Helps to define the quit function"""
        print("Quit command to exit the program\n")

    def handle_custom_command(self, class_name, action):
        """This function handle custom commands """
        parts = action.split("(")
        if len(parts) == 2 and parts[1].endswith(")"):
            action_name = parts[0]
            action_args = parts[1][:-1].split(",")

            # Strip quotes from arguments
            action_args = [arg.strip('"') for arg in action_args]

            if action_name == "show":
                key = "{}.{}".format(class_name, action_args[0])
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print("** no instance found **")

            elif action_name == "all":
                objs = [str(v) for k, v in storage.all().items()
                        if k.startswith(class_name)]
                print(objs)

            elif action_name == "count":
                count = 0
                for k in storage.all():
                    if k.startswith(class_name + '.'):
                        count += 1
                print(count)

            elif action_name == "destroy":
                key = "{}.{}".format(class_name, action_args[0])
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                else:
                    print("** no instance found **")

            elif action_name == "update":
                key = "{}.{}".format(class_name, action_args[0])
                if key in storage.all():
                    obj = storage.all()[key]
                    attribute_name = action_args[1]
                    attribute_value = action_args[2]

                    # Update the attribute with the given value
                    setattr(obj, attribute_name, attribute_value)
                    obj.save()
                else:
                    print("** no instance found **")

            else:
                print(f"** invalid action: {action_name}.\
                Type 'help' for assistance **")

        else:
            print(f"** invalid syntax: {action}.\
             Type 'help' to get assistance**")

    def default(self, line):
        """Handles default behavior when command is not recognized"""
        if not line:
            return
        commands = line.split('.')
        if len(commands) < 2:
            print("** invalid syntax **")
            return
        classname = commands[0]
        argument = '.'.join(commands[1:])
        if classname not in HBNBCommand.CLASSES:
            print("** class doesn't exist **")
            return
        if not argument:
            print("** missing command **")
            return
        self.handle_custom_command(classname, argument)

    def do_create(self, line):
        """Creates a new instance, saves it, and prints the id"""

        if not line:
            print("** class name missing **")
            return
        # Parse the class name and args from the line
        args = line.split()
        classname = args[0]

        # Validate the class name
        if classname not in HBNBCommand.CLASSES:
            print("** class doesn't exist **")
            return
        # Create instance
        try:
            new_instance = eval(classname)()
        except Exception as e:
            print("** class doesn't exist **")
            return
        # Save new instance and print id
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id."""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.CLASSES:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = line.split()
        if len(args) < 2:
            print("** instance id missing **")
            return

        classname = args[0]
        instance_id = args[1]

        key = f"{classname}.{instance_id}"
        obj = storage.all().get(key)

        if not obj:
            print("** no instance found **")
        else:
            del storage.all()[key]
            storage.save()

    def do_all(self, line):
        """Deletes an instance based on the class name and id
            the updates are then saved
        """
        args = line.split()
        # objects = storage.all()
        if not args:
            print([str(obj) for obj in storage.all().values()])
        elif args[0] not in self.CLASSES:
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            instances = [
                str(obj) for key, obj in storage.all().items()
                if key.startswith(class_name + '.')
            ]
            print(instances)

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        """
        args = line.split()

        if not args:
            print("** class name missing **")
            return

        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s(".*"|[^"]\S*)?)?)?)?'
        match = re.search(rex, line)

        if not match:
            print("** invalid command format **")
            return

        classname, uid, attribute, value = match.groups()

        if classname not in self.CLASSES:
            print("** class doesn't exist **")
            return
        elif not uid:
            print("** instance id missing **")
            return

        key = f"{classname}.{uid}"
        if key not in storage.all():
            print("** no instance found **")
            return
        elif not attribute:
            print("** attribute name missing **")
            return
        elif not value:
            print("** value missing **")
            return

        obj = storage.all()[key]

        # Simplify attribute handling (without explicit checks)
        setattr(obj, attribute, value)

        storage.all()[key].save()

    # aliasing
    do_exit = do_quit


if __name__ == "__main__":
    # readline.parse_and_bind("tab: complete") for UNIX
    readline.parse_and_bind("bind ^rl_complete")  # for MAC
    interface = HBNBCommand()
    interface.cmdloop()
