from operator import contains
import numpy
import json
import logging
import sys


logger = logging.getLogger()
logger.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Load map
def check_validity(i_map, index, objects):
    # Check that file is valid json
    logging.info("Checking validity....")
    try:
        with open(i_map) as f:
            map = json.load(f)
    except(ValueError):
        logging.critical(" !!!! Map is not a valid json, please double check !!!!")
        return False

    logging.info("Map is a valid json, checking that provided starting room exists....")
    room_ids= set([x["id"] for x in map["rooms"]])
    if index not in room_ids:
        logger.critical("!!!! Starting point provided not present !!!!")
        return False
    
    logging.info("Checking that all rooms are connected")
    directions = ["north", "south", "west", "east"]
    #generate list of connected rooms
    connected_rooms = set()
    for x in map["rooms"]:
        for i in directions:
            if i in x:
                connected_rooms.add(x[i])
    if room_ids != connected_rooms:
        logger.critical(f"!!!! One or more room are isolated! Rooms {room_ids-connected_rooms} not connected !!!!")
        return False
    return True
