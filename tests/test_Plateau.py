from src.Plateau import Plateau


class TestPlateau:
    """
        Test class regarding the Plateau class
    """

    def test_plateau(self):
        """
            Used to test that the object created is a Plateau and to check the dimensions of it
        """
        p1 = Plateau(5, 5)
        assert isinstance(p1, Plateau) and p1.edge_y == 5 and p1.edge_x == 5
