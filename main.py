from src.Game import Game


def run():
    print("Starting ...")
    script = str(input("Enter the script : "))  # User input containing the whole script
    g1 = Game(script)
    result = g1.start()  # Playing the script
    for position in result:
        print(position)  # Showing result


if __name__ == '__main__':
    run()
