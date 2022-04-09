import pytest

from src.Plateau import Plateau
from src.Rover import Rover
from src.Exceptions import InvalidTileCountError, FacingError, MoveError


class TestRover:
    """
        Test class regarding the Rover class
    """

    def test_rover(self):
        """
            Used to test that the object created is a Rover and to check the position of it
        """
        p1 = Plateau(5, 5)
        r1 = Rover(1, 1, "N", p1)
        assert isinstance(r1, Rover) and r1.x == 1 and r1.y == 1 and r1.facing == "N"

    def test_move_one_step_north(self):
        """
            Used to test for a single step of the rover and check if the rover still facing North
        """
        p1 = Plateau(5, 5)
        r1 = Rover(1, 1, "N", p1)
        r1.move(1)
        assert (r1.x == 1 and r1.y == 2 and r1.facing == "N")

    def test_move_one_step_east(self):
        """
            Used to test for a single step of the rover and check if the rover still facing East
        """
        p1 = Plateau(5, 5)
        r1 = Rover(1, 1, "E", p1)
        r1.move(1)
        assert (r1.x == 2 and r1.y == 1 and r1.facing == "E")

    def test_move_multiple_step(self):
        """
            Used to test for multiple steps of the rover and check if the rover still facing West
        """
        p1 = Plateau(5, 5)
        r1 = Rover(4, 4, "W", p1)
        r1.move(3)
        assert (r1.x == 1 and r1.y == 4 and r1.facing == "W")

    def test_move_negative_step(self):
        """
            Used to test is an InvalidTileCountError exception is raised while doing a negative move
        """
        p1 = Plateau(5, 5)
        r1 = Rover(1, 1, "N", p1)
        with pytest.raises(InvalidTileCountError):
            r1.move(-1)

    def test_move_multiple_operation(self):
        """
            Used to test is an InvalidTileCountError exception is raised while doing a negative move
        """
        p1 = Plateau(10, 10)
        r1 = Rover(5, 7, "S", p1)
        r1.move(1)
        r1.move(3)
        assert (r1.x == 5 and r1.y == 3 and r1.facing == "S")

    def test_move_invalid_facing(self):
        """
            Used to test is an FacingError exception is raised while moving with an invalid rover facing
        """
        p1 = Plateau(5, 5)
        r1 = Rover(1, 1, "O", p1)
        with pytest.raises(FacingError):
            r1.move(1)

    def test_rotate_one_left(self):
        """
            Used to test if the rover facing is updated with a rotation to the left
        """
        p1 = Plateau(5, 5)
        r1 = Rover(1, 1, "N", p1)
        r1.rotate("L")
        assert (r1.x == 1 and r1.y == 1 and r1.facing == "W")

    def test_rotate_multiple_left(self):
        """
            Used to test if the rover facing is updated with multiple rotations to the left
        """
        p1 = Plateau(5, 5)
        r1 = Rover(1, 1, "N", p1)
        r1.rotate("L")
        r1.rotate("L")
        assert (r1.x == 1 and r1.y == 1 and r1.facing == "S")

    def test_rotate_one_right(self):
        """
            Used to test if the rover facing is updated with a rotation to the right
        """
        p1 = Plateau(5, 5)
        r1 = Rover(1, 1, "N", p1)
        r1.rotate("R")
        assert (r1.x == 1 and r1.y == 1 and r1.facing == "E")

    def test_rotate_multiple_right(self):
        """
            Used to test if the rover facing is updated with multiple rotations to the right
        """
        p1 = Plateau(5, 5)
        r1 = Rover(1, 1, "N", p1)
        r1.rotate("R")
        r1.rotate("R")
        assert (r1.x == 1 and r1.y == 1 and r1.facing == "S")

    def test_rotate_right_and_left(self):
        """
            Used to test if the rover facing is updated with multiple rotations to the right and left
        """
        p1 = Plateau(5, 5)
        r1 = Rover(1, 1, "N", p1)
        r1.rotate("R")
        r1.rotate("L")
        assert (r1.x == 1 and r1.y == 1 and r1.facing == "N")

    def test_commit_movement_simple_m(self):
        """
            Used to test if the rover position is updated with a single movement
        """
        p1 = Plateau(5, 5)
        r1 = Rover(1, 1, "E", p1)
        result = r1.commit_movement("M")
        assert result == "2 1 E"

    def test_commit_movement_multiple_m(self):
        """
            Used to test if the rover position is updated with multiple movements
        """
        p1 = Plateau(5, 5)
        r1 = Rover(1, 1, "E", p1)
        result = r1.commit_movement("MMM")
        assert result == "4 1 E"

    def test_commit_movement_invalid_move(self):
        """
            Used to test is a MoveError exception is raised while doing a invalid move
            which would cause the exit of the plateau
        """
        p1 = Plateau(5, 5)
        r1 = Rover(1, 1, "E", p1)
        with pytest.raises(MoveError):
            r1.commit_movement("MMMMMMM")

    def test_commit_movement_unrecognized_move(self):
        """
            Used to test is a MoveError exception is raised while doing an invalid move input
        """
        p1 = Plateau(5, 5)
        r1 = Rover(1, 1, "E", p1)
        with pytest.raises(MoveError):
            r1.commit_movement("O")

    def test_commit_movement_rotate_simple(self):
        """
            Used to test if the rover facing is updated while committing a right movement
        """
        p1 = Plateau(5, 5)
        r1 = Rover(3, 1, "E", p1)
        result = r1.commit_movement("R")
        assert result == "3 1 S"

    def test_commit_movement_rotate_multiple(self):
        """
            Used to test if the rover facing is updated while committing multiple right and left movements
        """
        p1 = Plateau(5, 5)
        r1 = Rover(3, 1, "E", p1)
        result = r1.commit_movement("RLRRRL")
        assert result == "3 1 W"

    def test_commit_movement_rotate_and_move(self):
        """
            Used to test if the rover facing and position is updated while committing multiple right, left and move
             movements
        """
        p1 = Plateau(5, 5)
        r1 = Rover(3, 1, "W", p1)
        result = r1.commit_movement("RMMRML")
        assert result == "4 3 N"

    def test_commit_movement_empty(self):
        """
           Used to test if the rover facing and position are still the same while committing an empty move
       """
        p1 = Plateau(7, 7)
        r1 = Rover(6, 0, "S", p1)
        result = r1.commit_movement("")
        assert result == "6 0 S"

    def test_is_move_valid_one_step(self):
        """
           Used to test if a single step is considered as a valid move
       """
        p1 = Plateau(5, 5)
        r1 = Rover(1, 1, "N", p1)
        is_valid = r1.is_move_valid(1)
        assert is_valid is True

    def test_is_move_valid_multiple_step(self):
        """
           Used to test if multiple steps are considered as a valid move
       """
        p1 = Plateau(5, 5)
        r1 = Rover(4, 1, "W", p1)
        is_valid = r1.is_move_valid(3)
        assert is_valid is True

    def test_is_move_invalid(self):
        """
           Used to test if a move is detected as invalid
       """
        p1 = Plateau(5, 5)
        r1 = Rover(3, 0, "S", p1)
        is_valid = r1.is_move_valid(3)
        assert is_valid is False

    def test_is_move_valid_error(self):
        """
           Used to test if an FacingError exception is raised while checking for a move with an invalid rover facing
       """
        p1 = Plateau(5, 5)
        r1 = Rover(3, 4, "O", p1)
        with pytest.raises(FacingError):
            r1.is_move_valid(1)
