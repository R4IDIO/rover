from src.Game import Game


class TestGame:
    """
        Test class regarding the Game class
    """

    def test_game(self):
        """
            Used to test that the object created is a Game and to check the instructions of it
        """
        script = "10 10 4 3 S mmrm"
        g1 = Game(script)
        assert isinstance(g1, Game) and g1.instructions == ["10", "10", "4", "3", "S", "MMRM"]

    def test_is_valid_script(self):
        """
            Used to test is a script is considered as valid
        """
        script = "10 10 4 3 S MMRM"
        g1 = Game(script)
        is_valid = g1.is_valid_script(g1.instructions)
        assert is_valid is True

    def test_is_invalid_script(self):
        """
            Used to test is a script is considered as invalid because of the number of instructions
        """
        script = "10 10 4"
        g1 = Game(script)
        is_valid = g1.is_valid_script(g1.instructions)
        assert is_valid is False

    def test_is_invalid_script_plateau(self):
        """
            Used to test is a script is considered as invalid because of the plateau dimensions
        """
        script = "10 A 4 3 S MMRM"
        g1 = Game(script)
        is_valid = g1.is_valid_script(g1.instructions)
        assert is_valid is False

    def test_start_one_result(self):
        """
            Used to test if a single result is returned and that the result is the one expected
        """
        script = "10 10 4 3 S MMRM"
        g1 = Game(script)
        result = g1.start()
        assert len(result) == 1 and result[0] == "3 1 W"

    def test_start_multiple_result(self):
        """
            Used to test if multiple results are returned and that results are the one expected
        """
        script = "10 10 4 3 S MMRM 2 2 W LM"
        expected_value = ["3 1 W", "2 1 S"]
        g1 = Game(script)
        result = g1.start()
        assert len(result) == 2 and result == expected_value

    def test_start_invalid_script(self):
        """
            Used to test if there is no result while launching the "game" with an invalid script
        """
        script = "5 A 4 3 S MML"
        g1 = Game(script)
        result = g1.start()
        assert len(result) == 0 and not result

    def test_start_invalid_script_exception(self):
        """
            Used to test if the result is empty when an exception is encountered while a rover is moving
        """
        script = "5 5 4 3 S MMMM"
        expected_value = [""]
        g1 = Game(script)
        result = g1.start()
        assert len(result) == 1 and result == expected_value

    def test_start_multiple_result_exception(self):
        """
            Used to test if a result is obtained for each rover even if one of them has a problem while moving
        """
        script = "10 10 4 3 S MMRMMMMMMMMMM 2 2 W LM"
        expected_value = ["", "2 1 S"]
        g1 = Game(script)
        result = g1.start()
        assert len(result) == 2 and result == expected_value
