import math

def triangle_area(base, height):
    return 0.5 * base * height

def rectangle_area(length, width):
    return length * width

def square_area(side):
    return side ** 2

def parallelogram_area(base, height):
    return base * height

def circle_area(radius):
    return math.pi * radius ** 2

def main():
    print("Polygon Area Calculator")
    print("1. Triangle")
    print("2. Rectangle")
    print("3. Square")
    print("4. Parallelogram")
    print("5. Circle")
    
    choice = int(input("Enter the number of the shape you want to calculate the area for: "))
    
    if choice == 1:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        print(f"The area of the triangle is {triangle_area(base, height):.2f}")
    elif choice == 2:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        print(f"The area of the rectangle is {rectangle_area(length, width):.2f}")
    elif choice == 3:
        side = float(input("Enter the side of the square: "))
        print(f"The area of the square is {square_area(side):.2f}")
    elif choice == 4:
        base = float(input("Enter the base of the parallelogram: "))
        height = float(input("Enter the height of the parallelogram: "))
        print(f"The area of the parallelogram is {parallelogram_area(base, height):.2f}")
    elif choice == 5:
        radius = float(input("Enter the radius of the circle: "))
        print(f"The area of the circle is {circle_area(radius):.2f}")
    else:
        print("Invalid choice! Please enter a valid number.")

if __name__ == "__main__":
    main()
