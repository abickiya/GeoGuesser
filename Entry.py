from PIL import Image
import random
import os


class Entry:
    """ A data structure to represent an image that can be guessed """

    def __init__(self, location: "String", path: "String") -> None:
        self.name = location.lower()
        here = os.path.dirname(os.path.abspath(__file__))
        self.im_path = os.path.join(here, path)

    def display(self) -> None:
        im = Image.open(self.im_path)
        im.show()
        return

    def guess(self, l_guess: "String") -> bool:
        if l_guess.lower() == self.name:
            return True
        else:
            return False

    def __str__(self) -> "String":
        return self.name


class Entries:
    """ A class holding a list of Entry objects, methods built to work with a list """

    def __init__(self) -> None:
        self.locations = []

    def add_entry(self, location: "String", path: "String") -> None:
        """ Add an Entry object to the list """
        self.locations.append(Entry(location, path))
        return

    def read_entries(self, path: "String" = "") -> None:
        """ Import Entry objects from a file, at a given spot """
        current_path = os.path.dirname(os.path.abspath(__file__))
        if path == "":
            filename = os.path.join(current_path, "images/tuples.txt")
        else:
            filename = os.path.join(current_path, path)
        in_text = open(filename, "r")
        for line in in_text:
            line_data = line.split(",")
            self.add_entry(line_data[0], line_data[1])
        return

    def shuffle_entries(self) -> None:
        """ Shuffle the order of Entry objects, helpful when starting a game """
        random.shuffle(self.locations)
        return

    def print_countries(self) -> None:
        for x in self.locations:
            print(x)
        return
