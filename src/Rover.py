from src.Exceptions import FacingError, MoveError, InvalidTileCountError
from src.Plateau import Plateau


class Rover:

    def __init__(self, x: int, y: int, facing: str, plateau: Plateau):

        self.x = x
        self.y = y
        self.facing = facing
        self.plateau = plateau

    def move(self, tile_count: int):
        """
            Private method
            Allows the rover to move forward
            :param tile_count: (int) -> Number of tiles for the rover to move
        """
        if tile_count < 0:
            raise InvalidTileCountError("Movement can't be negative!")
        if self.facing == "E":
            self.x += tile_count
        elif self.facing == "N":
            self.y += tile_count
        elif self.facing == "W":
            self.x -= tile_count
        elif self.facing == "S":
            self.y -= tile_count
        else:
            raise FacingError("Invalid cardinal compass value")

    def is_move_valid(self, tile_count: int):
        """
            Private method
            Used to detect if a move is valid or not
        :param tile_count: (int) -> Number of tiles for the rover to move
        :return: (boolean) -> True if the move is valid, else False
        """
        if self.facing == "E":
            return self.x + tile_count <= self.plateau.edge_x
        elif self.facing == "W":
            return self.x - tile_count >= 0
        elif self.facing == "N":
            return self.y + tile_count <= self.plateau.edge_y
        elif self.facing == "S":
            return self.y - tile_count >= 0
        else:
            raise FacingError("Invalid cardinal compass value")

    def rotate(self, direction: str):
        """
            Private method
            Used to rotate the rover to left or right
        :param direction: (str) -> Direction to rotate the rover, could be L or R
        """
        if (self.facing == "E" and direction == "L") or (self.facing == "W" and direction == "R"):
            self.facing = "N"
        elif (self.facing == "S" and direction == "L") or (self.facing == "N" and direction == "R"):
            self.facing = "E"
        elif (self.facing == "W" and direction == "L") or (self.facing == "E" and direction == "R"):
            self.facing = "S"
        else:
            self.facing = "W"

    def commit_movement(self, movement_sequence: str):
        """
            Public method
            Used to handle the movement sequence
            Called by the "game" class
        :param movement_sequence: (str) -> Movement sequence of the rover
        """
        for movement in movement_sequence:
            if movement in ["L", "R"]:
                self.rotate(movement)
            elif movement == "M":
                if self.is_move_valid(1):
                    self.move(1)
                else:
                    raise MoveError("Invalid instruction, rover would leave the plateau !")
            else:
                raise MoveError(f"Invalid instruction : {movement}")
        return f"{self.x} {self.y} {self.facing}"
