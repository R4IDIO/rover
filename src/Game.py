from src.Plateau import Plateau
from src.Rover import Rover
from typing import List


class Game:

    def __init__(self, script: str):
        """
            Initialization of the Game object
        :param script: (str) -> Script of the game
        """
        self.instructions = script.upper().split(" ")

    def start(self):
        """
            Used to start the "game" and execute the script
        :return: (List[str]) -> List of rover position
        """
        result = []
        if self.is_valid_script(self.instructions):
            edge_x, edge_y = int(self.instructions[0]), int(self.instructions[1])
            plateau = Plateau(edge_x, edge_y)
            instructions = self.instructions[2:]  # Removing plateau dimensions instructions
            for i in range(0, len(instructions), 4):
                current_instructions = instructions[i:i + 4]
                x = int(current_instructions[0])
                y = int(current_instructions[1])
                facing = current_instructions[2]
                movements = current_instructions[3]
                rover = Rover(x, y, facing, plateau)
                try:
                    result.append(rover.commit_movement(movements))
                except Exception as e:
                    result.append(str(e))
                    pass
        else:
            result.append("The dimensions of the plateau or the script are not correct.")
        return result

    @staticmethod
    def is_valid_script(instructions: List):
        """
            A script is considered as valid if :
                - the number of instructions >= 6
                - two firsts instructions are int (plateau dimensions)
                - Number of instructions
        :param instructions: (List) -> List of instructions
        """
        return len(instructions) >= 6 and str(instructions[0]).isnumeric() and str(instructions[1]).isnumeric() and len(
            instructions[2:]) % 4 == 0
