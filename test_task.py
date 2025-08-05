from abc import ABC, abstractmethod
from math import pi, pow


class Shape(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @classmethod
    @abstractmethod
    def create(cls, data_string):
        pass


class Square(Shape):
    def __init__(self, x, y, side):
        self.x_position = x
        self.y_position = y
        self.side = side

    @classmethod
    def create(cls, data_string):
        x_position = None
        y_position = None
        side = None
        j = 1
        try:
            while j < len(data_string):
                if data_string[j] == 'TopRight':
                    x_position = int(data_string[j+1])
                    y_position = int(data_string[j+2])
                    j += 3
                elif data_string[j] == 'Side':
                    side = int(data_string[j+1])
                    if side <= 0:
                        raise ValueError
                    j += 2
                else:
                    raise ValueError
            return cls(x_position, y_position, side)
        except ValueError:
            raise ValueError('Invalid data string')

    def perimeter(self):
        return self.side * 4

    def area(self):
        return self.side * self.side

class Circle(Shape):
    def __init__(self, x, y, radius):
        self.x_position = x
        self.y_position = y
        self.radius = radius

    @classmethod
    def create(cls, data_string):
        x_position = None
        y_position = None
        radius = None
        j = 1
        try:
            while j < len(data_string):
                if data_string[j] == 'Center':
                    x_position = int(data_string[j+1])
                    y_position = int(data_string[j+2])
                    j += 3
                elif data_string[j] == 'Radius':
                    radius = int(data_string[j+1])
                    if radius <= 0:
                        raise ValueError
                    j += 2
                else:
                    raise ValueError
            return cls(x_position, y_position, radius)
        except ValueError:
            raise ValueError('Invalid data string')

    def perimeter(self):
        return round(self.radius * 2 * pi, 2)

    def area(self):
        return round(pi * pow(self.radius, 2), 2)

class  Rectangle(Shape):
    def __init__(self, x, y, x2, y2):
        self.first_x_position = x
        self.first_y_position = y
        self.second_x_position = x2
        self.second_y_position = y2
        self.width = abs(x - x2)
        self.height = abs(y - y2)

    @classmethod
    def create(cls, data_string):
        first_x_position = None
        first_y_position = None
        second_x_position = None
        second_y_position = None
        j = 1
        try:
            while j < len(data_string):
                if data_string[j] == 'TopRight':
                    first_x_position = int(data_string[j+1])
                    first_y_position = int(data_string[j+2])
                    j += 3
                elif data_string[j] == 'BottomLeft':
                    second_x_position = int(data_string[j+1])
                    second_y_position = int(data_string[j+2])
                    j += 3
                else:
                    raise ValueError
            return cls(first_x_position, first_y_position, second_x_position, second_y_position)
        except ValueError:
            raise ValueError('Invalid data string')

    def perimeter(self):
        return (self.width + self.height) * 2

    def area(self):
        return self.width * self.height

def define (line):
    shape_classes = {
        "Square": Square,
        "Circle": Circle,
        "Rectangle": Rectangle
    }

    elements = line.split(" ")
    if elements[0] in shape_classes:
        return shape_classes[elements[0]].create(elements)
    else:
        raise ValueError('Invalid figure type')

def main():
    with open("text.txt") as f:
        for i in f:
            try:
                figure = define(i)
                print(type(figure).__name__, "Perimeter", figure.perimeter(), "Area", figure.area())
            except ValueError as e:
                print(e)
                continue

if __name__ == "__main__":
    main()