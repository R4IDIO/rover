from typing import List

from src.Plateau import Plateau
from src.Rover import Rover


def is_valid_script(instructions: List):
    """
        A script is considered as valid if :
            - the number of instructions >= 6
            - two firsts instructions are int (plateau dimensions)
            - Number of instructions
    :param instructions: (List) -> List of instructions
    """
    return len(instructions) >= 6 \
           and str(instructions[0]).isnumeric() \
           and str(instructions[1]).isnumeric() \
           and len(instructions[2:]) % 4 == 0


def run():
    is_rover = False
    print("Starting ...")
    script = input("Enter the input : ")
    instructions = script.split(" ")
    if is_valid_script(instructions):
        edge_x, edge_y = int(instructions[0]), int(instructions[1])
        plateau = Plateau(edge_x, edge_y)
        instructions = instructions[2:]  # Removing plateau dimensions instructions
        for i in range(0, len(instructions), 4):
            curent_instructions = instructions[i:i+4]
            x = int(curent_instructions[0])
            y = int(curent_instructions[1])
            facing = curent_instructions[2]
            movements = curent_instructions[3]
            rover = Rover(x, y, facing, plateau)
            try:
                print(rover.commit_movement(movements))
            except Exception as e:
                print(e)
                pass



if __name__ == '__main__':
    run()
