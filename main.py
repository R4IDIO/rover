from src.Game import Game


def run():
    print("Starting ...")
    script = input("Enter the input : ")
    g1 = Game(script)
    result = g1.start()
    for position in result:
        print(position)


if __name__ == '__main__':
    run()
