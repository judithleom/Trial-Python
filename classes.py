class Rectangle:
    def __init__(self, width = 1, height = 1):
        self.__width = width
        self.__height = height
    def getArea(self):
        return self.__width * self.__height    
    def getPerimeter(self):
        return 2 * (self.__width + self.__height)
def main():
    r1 = Rectangle(2, 4)
    print("The area is", r1.getArea())
    print("The perimeter is", r1.getPerimeter())    
    r2 = Rectangle(6, 10)
    print("The area is", r2.getArea())
    print("The perimeter is", r2.getPerimeter())
main() # Call the main function
