from unicodedata import name
from wsgiref import validate
from click import prompt
import numpy
import json
import argparse
import sys
import os.path
import tests.validate_map as checker
import logging

#init logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('[%(asctime)s] - %(levelname)s > %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

'''
# Flow
1. Check arguments and show help message
2. Check map validation -> All rooms are accessible, all objects passed are collectible, starting room exists
3. Standard iteration through json
4. Print path
'''
class MyParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help(sys.stderr)
        sys.exit(2)


def solve_map(map, index, objects):
    print("hello")

def main():
    parser = MyParser() # Create parser class
    parser.add_argument('--json_map', action= 'store', default=None, required=True, help="Path to json map") # Arguments
    args = parser.parse_args() # Parse args
    #Check map exists before moving forwards
    map_path = args.json_map
    if not os.path.isfile(map_path):
        logging.critical("Map doesn't exist")
        sys.exit(1)
    starting_room=""
    objects_to_collect = ""
    err = True
    while err:
        try:
            starting_room = int(input("Starting room id: "))
        except(ValueError):
            logging.error("Only integers allowed")
        err = False
    while err:
        objects_to_collect = input("Objects to collect: ").split(",")
        if len(objects_to_collect) == 0:
            logging.error("Provide more than one object separated by commas")
        err = False
    
    if(checker.check_validity(map_path, starting_room, objects_to_collect)):
        solve_map(map_path, starting_room, objects_to_collect)
    else:
        logging.critical("Validity check not passed, check validator logs")
        sys.exit(2)


if __name__ == "__main__":
    main()