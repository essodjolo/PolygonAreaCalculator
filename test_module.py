import unittest
import shape_calculator


class MyTestCase(unittest.TestCase):
    def test_get_area(self):  # also testing the setters here.
        # Rectangle
        rect = shape_calculator.Rectangle(0, 0)
        rect.set_height(2)
        rect.set_width(5)
        expected_area = 10
        self.assertEqual(expected_area, rect.get_area())

        # Square
        sq = shape_calculator.Square(0)
        sq.set_side(4)
        expected_area = 16
        self.assertEqual(expected_area, sq.get_area())

    def test_get_perimeter(self):
        # Rectangle
        rect = shape_calculator.Rectangle(3, 7)
        expected_perimeter = 20
        self.assertEqual(expected_perimeter, rect.get_perimeter())

        # Square
        sq = shape_calculator.Square(3)
        expected_perimeter = 12
        self.assertEqual(expected_perimeter, sq.get_perimeter())

    def test_get_diagonal(self):
        # Rectangle
        rect = shape_calculator.Rectangle(2, 4)
        expected_diagonal = 20 ** .5  # √20
        self.assertEqual(expected_diagonal, rect.get_diagonal())

        # Square
        sq = shape_calculator.Square(2)
        expected_diagonal = 8 ** .5  # √8
        self.assertEqual(expected_diagonal, sq.get_diagonal())

    def test__repr__(self):
        # Rectangle
        rect = shape_calculator.Rectangle(5, 10)
        expected_output = "Rectangle(width=5, height=10)"
        self.assertEqual(expected_output, str(rect))

        # Square
        sq = shape_calculator.Square(9)
        expected_output = "Square(side=9)"
        self.assertEqual(expected_output, str(sq))

    def test_get_picture(self):
        # Rectangle
        rect = shape_calculator.Rectangle(20, 5)
        expected_picture = """********************
********************
********************
********************
********************"""
        self.assertEqual(expected_picture, rect.get_picture())

        # Square
        sq = shape_calculator.Square(5)
        expected_picture = """*****
*****
*****
*****
*****"""
        self.assertEqual(expected_picture, str(sq))

        # When width or height is larger than 50
        rect = shape_calculator.Rectangle(52, 45)
        self.assertEqual("Too big for picture.", rect.get_picture())
        rect = shape_calculator.Rectangle(23, 85)
        self.assertEqual("Too big for picture.", rect.get_picture())

    def test_get_amount_inside(self):
        rect = shape_calculator.Rectangle(4, 8)
        sq = shape_calculator.Square(4)
        self.assertEqual(2, rect.get_amount_inside(sq))
        rect_2 = shape_calculator.Rectangle(4, 6)
        self.assertEqual(1, rect.get_amount_inside(rect_2))
        rect_3 = shape_calculator.Rectangle(8, 4)
        self.assertEqual(0, rect.get_amount_inside(rect_3))


if __name__ == '__main__':
    unittest.main()
