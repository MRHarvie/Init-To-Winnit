print("Rectangle Calculator")

class Rectangle():
        def __init__(self, width, height):
            self.height = height
            self.width = width
            self.perimiter = (height + width) * 2
            self.area = height * width


height = int(input("Height: "))
width = int(input("Width: "))
rectangle = Rectangle(width, height)
print(f"Perimeter: {rectangle.perimiter}")
print(f"Area: {rectangle.area}")
