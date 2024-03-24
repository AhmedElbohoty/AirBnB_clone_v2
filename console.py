#!/usr/bin/python3
'''
HBNBCommand:
    the entry point of the command interpreter.
'''
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    '''The entry point of the command interpreter.

    Attributes:
        prompt (str): the command prompt.
        __classes (dict): dictionary contains all classes.
    '''
    __classes = {'BaseModel': BaseModel, 'User': User, 'State': State,
                 'City': City, 'Amenity': Amenity,
                 'Place': Place, 'Review': Review}
    prompt = '(hbnb) '
    types = {
        'number_rooms': int, 'number_bathrooms': int,
        'max_guest': int, 'price_by_night': int,
        'latitude': float, 'longitude': float
    }

    def do_quit(self, _):
        '''Exit the program with 'quit' command'''
        return True

    def do_EOF(self, _):
        '''Exit the program with 'EOF' signal'''
        print('')
        return True

    def emptyline(self):
        '''Don't execute anything'''

    def do_create(self, args):
        ''' Create an object of any class If any parameter doesn’t fit with
            these requirements or can’t be recognized correctly by your program
            it must be skipped'''
        if not args:
            print("** class name missing **")
            return

        args_list = args.split()
        classname = args_list[0]
        if classname not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        kwargs = {}
        for param in args_list[1:]:

            if '=' not in param:
                continue

            try:
                # any double quote inside the value must be escaped with a
                # backslash \
                # all underscores _ must be replace by spaces .
                k, v = param.split('=')
                k = k.replace(' ', '_')
                if v[0] == '"' and v[-1] == '"':
                    v = v[1:-1].replace('\\', '').replace('_', ' ')
                elif '.' in v:
                    # Float: <unit>.<decimal> => contains a dot .
                    v = float(v)
                else:
                    # Integer: <number> => default case
                    v = int(v)
                kwargs[k] = v
            except ValueError:
                continue

        new_instance = HBNBCommand.__classes[classname](kwargs)
        storage.save()
        print(new_instance.id)

        args = "{} {} {}".format(classname, new_instance.id, kwargs)
        self.do_update(args)
        storage.save()

    def do_update(self, args):
        """ Updates a certain object with new info """
        c_name = c_id = att_name = att_val = kwargs = ''

        # isolate cls from id/args, ex: (<cls>, delim, <id/args>)
        args = args.partition(" ")
        if args[0]:
            c_name = args[0]
        else:  # class name not present
            print("** class name missing **")
            return
        if c_name not in HBNBCommand.__classes:  # class name invalid
            print("** class doesn't exist **")
            return

        # isolate id from args
        args = args[2].partition(" ")
        if args[0]:
            c_id = args[0]
        else:  # id not present
            print("** instance id missing **")
            return

        # generate key from class and id
        key = c_name + "." + c_id

        # determine if key is present
        if key not in storage.all():
            print("** no instance found **")
            return

        # first determine if kwargs or args
        if '{' in args[2] and '}' in args[2] and type(eval(args[2])) is dict:
            kwargs = eval(args[2])
            args = []  # reformat kwargs into list, ex: [<name>, <value>, ...]
            for k, v in kwargs.items():
                args.append(k)
                args.append(v)
        else:  # isolate args
            args = args[2]
            if args and args[0] == '\"':  # check for quoted arg
                second_quote = args.find('\"', 1)
                att_name = args[1:second_quote]
                args = args[second_quote + 1:]

            args = args.partition(' ')

            # if att_name was not quoted arg
            if not att_name and args[0] != ' ':
                att_name = args[0]
            # check for quoted val arg
            if args[2] and args[2][0] == '\"':
                att_val = args[2][1:args[2].find('\"', 1)]

            # if att_val was not quoted arg
            if not att_val and args[2]:
                att_val = args[2].partition(' ')[0]

            args = [att_name, att_val]

        # retrieve dictionary of current objects
        new_dict = storage.all()[key]

        # iterate through attr names and values
        for i, att_name in enumerate(args):
            # block only runs on even iterations
            if (i % 2 == 0):
                att_val = args[i + 1]  # following item is value
                if not att_name:  # check for att_name
                    print("** attribute name missing **")
                    return
                if not att_val:  # check for att_value
                    print("** value missing **")
                    return
                # type cast as necessary
                if att_name in HBNBCommand.types:
                    att_val = HBNBCommand.types[att_name](att_val)

                # update dictionary with name, value pair
                new_dict.__dict__.update({att_name: att_val})

        new_dict.save()  # save updates to file

    def do_show(self, arg):
        '''Prints the string representation of an instance
        based on the class name and id.
        '''
        inputs = arg.split()
        is_valid = self.validate_input(inputs, ['classname', 'id'])

        if not is_valid:
            return

        objects = storage.all()
        k = '{}.{}'.format(inputs[0], inputs[1])

        obj = objects.get(k, None)

        print(obj)

    def do_destroy(self, arg):
        '''Deletes an instance based on the class name and id
        and save the change into the JSON file
        '''
        inputs = arg.split()
        is_valid = self.validate_input(inputs, ['classname', 'id'])

        if not is_valid:
            return

        objects = storage.all()
        k = '{}.{}'.format(inputs[0], inputs[1])

        del objects[k]
        storage.save()

    def do_all(self, arg):
        '''Prints all string representation of all instances
        based or not on the class name.
        '''
        inputs = arg.split()
        objects = storage.all()

        res = []
        if len(inputs) < 1:
            for _, v in objects.items():
                res.append(str(v))
            print(res)
            return

        classname = inputs[0]
        if classname not in self.__classes:
            print('** class doesn\'t exist **')
            return

        for _, v in objects.items():
            if v.__class__.__name__ == classname:
                res.append(str(v))
        print(res)

    def do_count(self, arg):
        '''Retrieve the number of instances of a class.
        '''
        counter = 0
        objects = storage.all()
        for _, v in objects.items():
            if v.__class__.__name__ == arg:
                counter += 1
        print(counter)

    def default(self, line):
        args = line.split('.')
        classes = self.__classes

        if len(args) != 2:
            super().default(line)
            return

        classname = args[0]
        if classname not in classes:
            print('** class doesn\'t exist **')
            return

        method = args[1].split('(')[0]
        if method == 'count':
            self.do_count(classname)

        elif method == 'all':
            self.do_all(classname)

        elif method == 'create':
            self.do_create(classname)

        elif method == 'destroy':
            obj_id = args[1].split('(')[1].split(')')[0]
            self.do_destroy('{} {}'.format(classname, obj_id))

        elif method == 'show':
            obj_id = args[1].split('(')[1].split(')')[0]
            self.do_show('{} {}'.format(classname, obj_id))

        elif method == 'update':
            inputs = args[1].split('(')[1].split(')')[0].split(',')
            line = '{} '.format(classname)

            if len(inputs) == 1:
                line += inputs[0].strip()
                self.do_update(line)
                return

            # Check if dictionary representaion is provided
            dict_str = args[1].split('(')[1].split(')')[
                0].partition(',')[2].strip()

            tokens = list(shlex.shlex(
                dict_str, posix=True, punctuation_chars=True))
            if tokens[0] == '{' and tokens[len(tokens)-1] == '}':
                tokens = [x for x in tokens if x not in ',:}{']
                for i in range(0, len(tokens), 2):
                    line = shlex.join([classname,
                                       inputs[0].strip(), tokens[i],
                                       tokens[i+1]])
                    self.do_update(line)
            else:
                for i, inp in enumerate(inputs):
                    line += inp.strip()
                    if i != len(inputs) - 1:
                        line += ' '

            self.do_update(line)

    def validate_input(self, inputs, args):
        '''Validate user input

        Args:
            inp (str): user input.
            args (list): the args to be checked against input.
        '''
        classes = self.__classes

        for i, arg in enumerate(args):
            if arg == 'classname':
                if len(inputs) == 0 or i > len(inputs):
                    print('** class name missing **')
                    return False
                if inputs[i] not in classes:
                    print('** class doesn\'t exist **')
                    return False

            if arg == 'id':
                if i > len(inputs) - 1:
                    print('** instance id missing **')
                    return False

                objects = storage.all()
                k = '{}.{}'.format(inputs[0], inputs[1])

                obj = objects.get(k, None)
                if obj is None:
                    print('** no instance found **')
                    return False

            if arg == 'attribute_name':
                if i > len(inputs) - 1:
                    print('** attribute name missing **')
                    return False

            if arg == 'attribute_value':
                if i > len(inputs) - 1:
                    print('** value missing **')
                    return False

        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
