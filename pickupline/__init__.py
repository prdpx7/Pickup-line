import argparse
import pyperclip

from .pickuplinesgalore import PickuplinesGalore
from .pickuplinegen import Pickuplinegen

def say_sorry():
    print("Sorry buddy! couldn't found any pickupline ¯\_(ツ)_/¯")

def run(args):
    if args.list:
        pick = PickuplinesGalore()
        print("\n".join(pick.get_list_of_categories()))
        return
    line = None
    if args.keyword:
        pick = PickuplinesGalore()
        line = pick.get_pickupline(args.keyword)
        if not line:
            say_sorry()
    elif args.random:
        pick = Pickuplinegen()
        line = pick.get_pickupline()
        if not line:
            say_sorry()

    if line:
        print(line)
        pyperclip.copy(line)
    else:
        print("try pickup-line --help for more info")

def init():
    parser = argparse.ArgumentParser(description="A CLI tool for generating PickupLine from web", 
                                     epilog="the pickup-line will be copied to the clipboard", 
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-r', '--random', action='store_true', help="get a random pickupline")
    parser.add_argument('-k', '--keyword', help="""Search pickuplines by keyword.
Example:
pickup-line --k trump
pickup-line -keyword geek
pickup-line --keyword scifi
pickup-line -k dirty
    """)
    parser.add_argument('-l', '--list', action="store_true", help="list all existing categories")
    args = parser.parse_args()
    return args

def main():
    args = init()
    try:
        run(args)
    except KeyboardInterrupt:
        print("Error:Interrupted by user !!!")