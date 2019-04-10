from PIL import Image
import random
import os


class Entry:
    """ A data structure to represent an image that can be guessed """

    def __init__(self, location: "String", path: "String"):
        self.location = location
        here = os.path.dirname(os.path.abspath(__file__))
        self.im_path = os.path.join(here, path)

    def display(self):
        im = Image.open(self.im_path)
        im.show()

    def __str__(self):
        return self.location


class Entries:
    """ A class holding a list of Entry objects, methods built to work with a list """

    def __init__(self):
        self.locations = []

    def add_entry(self, location: "String", path: "String"):
        """ Add an Entry object to the list """
        self.locations.append(Entry(location, path))

    def read_entries(self, path: "String"):
        """ Import Entry objects from a file, at a predetermined spot """
        current_path = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(current_path, path)
        in_text = open(filename, "r")
        for line in in_text:
            line_data = line.split(",")
            self.add_entry(line_data[0], line_data[1])

    def shuffle_entries(self):
        """ Shuffle the order of Entry objects, helpful when starting a game """
        random.shuffle(self.locations)
