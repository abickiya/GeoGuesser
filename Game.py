from Entry import *


def run_game() -> None:
    print("Welcome to GeoGuesser!\nType Y to start and Q to quit.")
    while True:
        command = input()
        if command.lower() == "y":
            start_loop()
            return
        elif command.lower() == "q":
            return


def start_loop() -> None:
    print("\nGathering game data!")
    questions = gather_game_data()
    while questions.locations:
        current = questions.locations.pop(0)
        print("Guess this location!")
        current.display()
        while True:
            user_guess = input()
            if current.guess(user_guess):
                print("Correct!")
                break
            else:
                print("Incorrect!")
    return


def gather_game_data() -> Entries:
    locations = Entries()
    locations.read_entries()
    locations.shuffle_entries()
    return locations


if __name__ == '__main__':
    run_game()

