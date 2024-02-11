def title():
    print("Rectangle Calculator")

class Rectangle():
        def __init__(self, width, height):
            self.height = height
            self.width = width
            self.perimiter = (height + width) * 2
            self.area = height * width

def calculations():
    height = int(input("Height: "))
    width = int(input("Width: "))
    rectangle = Rectangle(width, height)
    print(f"Perimeter: {rectangle.perimiter}")
    print(f"Area: {rectangle.area}")
    return width, height

def draw_rectangle(width, height):
    for i in range(height):
        for j in range(width):
            if i==0 or i== height-1 or j==0 or j ==width- 1:
                print("*", end=" ")
            else:
                print(" ",end=" ")
        print()

def main():
    while True:
        width,height =calculations()
        draw_rectangle(width,height)
        print("")
        again = input("Continue? (y/n): ")
        if again.lower()!="y":
            print("")
            print("Bye!")
            break

if __name__ == '__main__':
    title()
    main()
