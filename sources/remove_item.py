import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from backend.database import Database
from argparse import ArgumentParser
from backend.vars import Vars
if __name__ == "__main__":
    database = Database(Vars.json_path)
    parser = ArgumentParser(epilog = "GBS Database item remover ")
    parser.add_argument("-d","--delete",help = "Remove item from database")
    parser.add_argument("-l","--list-items",required = False,action = "store_true")
    args = parser.parse_args()
    if args.list_items:
        print(database.read())
    elif args.delete:
        if database.exists(item):
            database.delete_item(item)
            print("Deleted from database " + item)
        else:
            print("Not existing item: " + item)
        exit(0)
    else:
        parser.print_help()
