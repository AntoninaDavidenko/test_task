import unittest
from test_task import Square, Circle, Rectangle, Triangle, define


class TestSquare(unittest.TestCase):
    def test_square_creation(self):
        data = ["Square", "TopRight", "1", "1", "Side", "5"]
        square = Square.create(data)
        self.assertEqual(square.side, 5)

    def test_square_area(self):
        data = ["Square", "TopRight", "1", "1", "Side", "5"]
        square = Square.create(data)
        self.assertEqual(square.area(), 25)

    def test_square_perimeter(self):
        data = ["Square", "TopRight", "1", "1", "Side", "5"]
        square = Square.create(data)
        self.assertEqual(square.perimeter(), 20)

    def test_square_missing_value(self):
        data = ["Square", "TopRight", "1", "Side", "5"]
        self.assertRaises(ValueError, Square.create, data)

    def test_square_wrong_value(self):
        data = ["Square", "TopRight", "1", "1", "Side", "0"]
        self.assertRaises(ValueError, Square.create, data)

    def test_square_mixed_order(self):
        data = ["Square", "Side", "2", "TopRight", "1", "1"]
        square = Square.create(data)
        self.assertEqual(square.perimeter(), 8)


class TestCircle(unittest.TestCase):
    def test_circle_creation(self):
        data = ["Circle", "Center", "1", "1", "Radius", "-1"]
        self.assertRaises(ValueError, Circle.create, data)

    def test_circle_area(self):
        data = ["Circle", "Center", "1", "1", "Radius", "3"]
        circle = Circle.create(data)
        self.assertEqual(circle.area(), 28.27)

    def test_circle_perimeter(self):
        data = ["Circle", "Center", "1", "1", "Radius", "3"]
        circle = Circle.create(data)
        self.assertEqual(circle.perimeter(), 18.85)

    def test_circle_missing_value(self):
        data = ["Circle", "Center", "1", "Radius", "2"]
        self.assertRaises(ValueError, Circle.create, data)

    def test_circle_mixed_order(self):
        data = ["Circle", "Radius", "2", "Center", "1", "1"]
        circle = Circle.create(data)
        self.assertEqual(circle.perimeter(), 12.57)


class TestRectangle(unittest.TestCase):
    def test_rectangle_creation(self):
        data = ["Rectangle", "TopRight", "2", "2", "BottomLeft", "1", "1"]
        rectangle = Rectangle.create(data)
        self.assertEqual(rectangle.first_x_position, 2)

    def test_rectangle_area(self):
        data = ["Rectangle", "TopRight", "3", "3", "BottomLeft", "1", "1"]
        rectangle = Rectangle.create(data)
        self.assertEqual(rectangle.area(), 4)

    def test_rectangle_perimeter(self):
        data = ["Rectangle", "TopRight", "3", "3", "BottomLeft", "1", "1"]
        rectangle = Rectangle.create(data)
        self.assertEqual(rectangle.perimeter(), 8)

    def test_rectangle_missing_value(self):
        data = ["Rectangle", "TopRight", "2", "BottomLeft", "1", "1"]
        self.assertRaises(ValueError, Rectangle.create, data)

    def test_rectangle_mixed_order(self):
        data = ["Rectangle", "BottomLeft", "1", "1", "TopRight", "2", "2"]
        rectangle = Rectangle.create(data)
        self.assertEqual(rectangle.first_x_position, 2)


class TestDefine(unittest.TestCase):
    def test_define_wrong_figure(self):
        data = "Triangle TopRight 1 1 Side 5"
        self.assertRaises(ValueError, define, data)

    def test_define_correct_figure(self):
        data = "Square TopRight 1 1 Side 5"
        figure = define(data)
        self.assertEqual(type(figure).__name__, "Square")

class TestTriangle(unittest.TestCase):
    def test_triangle_perimetr1(self):
        data = ["Triangle", "Point1", "5", "5", "Point2", "8", "8", "Point3", "10", "2"]
        triangle = Triangle.create(data)
        triangle_perimetr = triangle.perimeter()
        self.assertEqual(triangle_perimetr, 22)

    def test_triangle_perimetr2(self):
        data = ["Triangle", "Point1", "3", "5", "Point2", "8", "3", "Point3", "10", "2"]
        triangle = Triangle.create(data)
        triangle_perimetr = triangle.perimeter()
        self.assertEqual(triangle_perimetr, 12)

    def test_triangle_create(self):
        data = ["Triangle", "Point1", "5", "6", "Point2", "7", "8", "Point3", "9", "10"]
        triangle = Triangle.create(data)
        self.assertEqual(triangle.x1_position, 5)
        self.assertEqual(triangle.x2_position, 7)
        self.assertEqual(triangle.x3_position, 9)
        self.assertEqual(triangle.y1_position, 6)
        self.assertEqual(triangle.y2_position, 8)
        self.assertEqual(triangle.y3_position, 10)



if __name__ == '__main__':
    unittest.main()