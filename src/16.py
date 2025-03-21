import math

def calculate_area_rectangle(length, width):
    area = length * width
    return area

def calculate_circumference_circle(radius):
    circumference = 2 * math.pi * radius
    return circumference

def main():
    print("Rectangle Area:", calculate_area_rectangle(5, 3))
    print("Circle Circumference:", calculate_circumference_circle(7))

if __name__ == "__main__":
    main()
