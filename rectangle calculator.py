def title():
    """
    Print the title of the program.

    This function doesn't take any parameters.
    """
    print("Rectangle Calculator")

class Rectangle():
        def __init__(self, width, height):
            """
            Initialize a Rectangle object with the given width and height.

            Parameters:
            - width (int): The width of the rectangle.
            - height (int): The height of the rectangle.
            """
            self.height = height
            self.width = width
            self.perimiter = (height + width) * 2
            self.area = height * width

def calculations():
    """
    Perform calculations for a rectangle.

    This function takes user input for height and width, creates a Rectangle object,
    calculates perimeter and area, and then prints the results.

    Returns:
    - tuple: A tuple containing width and height.
    """
    height = int(input("Height: "))
    width = int(input("Width: "))
    rectangle = Rectangle(width, height)
    print(f"Perimeter: {rectangle.perimiter}")
    print(f"Area: {rectangle.area}")
    return width, height

def draw_rectangle(width, height):
    """
    Draw a rectangle using asterisks.

    Parameters:
    - width (int): The width of the rectangle.
    - height (int): The height of the rectangle.
    """
    for i in range(height):
        for j in range(width):
            if i==0 or i== height-1 or j==0 or j ==width- 1:
                print("*", end=" ")
            else:
                print(" ",end=" ")
        print()

def main():
    """
    Main function to run the rectangle calculator program.

    This function runs a loop to continuously take user input, perform calculations,
    and draw rectangles. The user can choose to continue or exit the program.
    """
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
