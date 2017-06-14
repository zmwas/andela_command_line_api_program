doc="""
Anga Weather App.

Usage:
    anga fetch_weather <city>
    anga help
    anga exit


Examples:
    anga fetch_weather Nairobi

"""
import cmd
from docopt import docopt, DocoptExit
from weather import fetch_weather


def doc_opt(f):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        """
        The DocoptExit is thrown when the args do not match.
        We print a message to the user and the usage block.
        The SystemExit exception prints the usage for --help
        """
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            return

        return f(self, opt)

    fn.__name__ = f.__name__
    fn.__doc__ = f.__doc__
    fn.__dict__.update(f.__dict__)
    return fn


class InteractiveWeather(cmd.Cmd):
    intro = '\n' + ' ' \
            + '\n' + ' ' \
            + (' ' * 9 + '* ' * 10) + 'ANGA. GET TO KNOW THE WEATHER WITHOUT LEAVING THE HOUSE!!' + (' *' * 10) \
            + '\n' + ' ' \
            + '\n' + ' ' \
            + '\n' + ' ' \
            + '\n' + (' ' * 12 + ' ' * 23) + 'Type help for a list of commands' \
            + '\n' + ' ' \
            + '\n' + '- ' * 53

    prompt = '(anga>>)'

    @doc_opt
    def do_fetch_weather(self, arg):
        """Usage: fetch_weather <city>"""
        if arg['<city>']:
            fetch_weather(arg['<city>'])
    @doc_opt
    def do_exit(self, arg):
        """Usage: exit"""
        print ('Bye!')
        exit()



if __name__ == '__main__':
    try:
        InteractiveWeather().cmdloop()
    except KeyboardInterrupt:
        print('Please try again')
        exit()
