def calculate_area(shape):
    """
    Calculate the area of a shape.
    
    Args:
        shape (str): The type of shape ('rectangle', 'circle', 'triangle').
        
    Returns:
        float: The area of the shape.
    """
    if shape == "rectangle":
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        return length * width
    elif shape == "circle":
        radius = float(input("Enter the radius: "))
        return 3.141592653589793 * (radius ** 2)
    elif shape == "triangle":
        base = float(input("Enter the base: "))
        height = float(input("Enter the height: "))
        return 0.5 * base * height
