import math
class Shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Shape):
    def __init__(self, length):
        super().__init__(length, length)
    
    def area(self):
        return self.length ** 2
    
    def perimeter(self):
        return self.length * 4
    

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length, width)
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return (self.length * 2) + (self.width * 2)

class Circle(Shape):
    def __init__(self, radius):
        super().__init__(0, 0)
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)
    
    def circumference(self):
        return 2 * math.pi * self.radius



def get_int(x):
    while True:
        try:
            user_input = int(input(x))
        except ValueError:
            print("Error: Please enter a valid number.")
        else:
            return user_input


def main():
    print("""Shapes
          Circle - 1
          Rectangle - 2
          Square - 3""")
    
    choices = get_int("Enter shape (1/2/3): ")
    while choices not in (1,2,3):
        print("Invalid input.")
        choices = get_int("Enter shape (1/2/3): ")   

    if choices == 1:
        radius = get_int("Enter radius: ")
        circle = Circle(radius)
        area = circle.area()
        circumference = circle.circumference()
        print(f"""Area = {round(area, 2)}
Circumference = {round(circumference, 2)}""")
    
    elif choices == 2:
        length = get_int("Enter length: ")
        width = get_int("Enter width: ")
        rectangle = Rectangle(length, width)
        area = rectangle.area()
        perimeter = rectangle.perimeter()
        print(f"Area = {area}")
        print(f"perimeter = {perimeter}")

    elif choices == 3:
        length = get_int("Enter length: ")
        square = Square(length)
        area = square.area()
        perimeter = square.perimeter()
        print(f"Area = {area}")
        print(f"perimeter = {perimeter}")

if __name__ == "__main__":
    main()