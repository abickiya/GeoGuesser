
def run_game():
    print("Welcome to GeoGuesser!\nType Y to start and Q to quit.")
    while True:
        command = input()
        if command.lower() == "y":
            start_loop()
            return
        elif command.lower() == "q":
            return
    return


def start_loop():
    print("Game Started!")
    return


if __name__ == '__main__':
    run_game()

