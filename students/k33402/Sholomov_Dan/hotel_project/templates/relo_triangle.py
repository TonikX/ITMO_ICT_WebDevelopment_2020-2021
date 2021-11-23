from math import pi


help_str = '1 - create\n' \
       '2 - print\n' \
       '3 - change color\n' \
       '4 - change visibility\n' \
       '5 - change center\n' \
       '6 - change side'


class Location:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Geometry:
    def __init__(self):
        self.pi = pi


class Primitive(Geometry):
    def __init__(self, color='black', visibility=True):
        Geometry.__init__(self)
        self.color = color
        self.visibility = visibility


class Point(Primitive, Location):
    def __init__(self, x=0, y=0, color="black", visibility=True):
        Primitive.__init__(self, color, visibility)
        Location.__init__(self, x, y)

    def __str__(self):
        return '({};{})'.format(self.x, self.y)


class ReloTriangle(Point):
    def __init__(self, center_x=0, center_y=0, side=0, color='black', visibility=True):
        self.point1 = Point(center_x - side / 2, center_y - (3 ** 0.5 * side / 6))
        self.point2 = Point(center_x, center_y + (3 ** 0.5 * side / 3))
        self.point3 = Point(center_x + side / 2, center_y - (3 ** 0.5 * side / 6))
        self.side = side
        Point.__init__(self, center_x, center_y, color, visibility)
        min_x = self.point1.x
        min_y = self.point2.y - side
        max_x = self.point3.x
        max_y = self.point2.y
        min_point = Point(min_x, min_y)
        max_point = Point(max_x, max_y)
        self.clip = Clip(min_point, max_point)

    def calculate_square(self):
        return (self.pi - 3 ** 0.5) * self.side ** 2 / 2

    def calculate_perimeter(self):
        return self.side * self.pi

    def change_center(self, new_x, new_y):
        self.__init__(new_x, new_y, self.side, self.color, self.visibility)

    def __str__(self):
        return f"""Свойства фигуры:
Центр = {Point.__str__(self)}
Вершины = {self.point1}, {self.point2}, {self.point3}, 
Сторона = {self.side}
Площадь = {self.calculate_square()}
Периметр = {self.calculate_perimeter()}
Видимость = {self.visibility}
Цвет = {self.color}
Область = {self.clip.min_point} -- {self.clip.max_point}
Размер = {self.clip.calculate_size()}"""

    def change_side(self, side):
        self.__init__(self.x, self.y, side, self.color, self.visibility)


class Clip:
    def __init__(self, min_point=Point(-100, -100), max_point=Point(100, 100)):
        self.min_point = min_point
        self.max_point = max_point

    def calculate_size(self):
        return '[{}x{}]'.format(self.max_point.x - self.min_point.x, self.max_point.y - self.min_point.y)


def main():
    print(help_str)
    relo = None
    while True:
        command = input()
        if command != '':
            command = int(command)
        else:
            break

        if command == 1:
            print("center_x center_y side color visibility")
            info = input().split()
            relo = ReloTriangle(float(info[0]), float(info[1]), float(info[2]), info[3], bool(info[4]))
        elif command == 2:
            print(relo)
        elif command == 3:
            print("color")
            relo.color = input()
        elif command == 4:
            print("visibility")
            relo.visibility = bool(input())
        elif command == 5:
            print("center_x center_y")
            center_x, center_y = map(float, input().split())
            relo.change_center(center_x, center_y)
        elif command == 6:
            print("side")
            relo.change_side(float(input()))


if __name__ == "__main__":
    main()
