# TODO: Complete the following functions that compute the area of the shapes below

def area_square(side:int)->int:
    
    """
    Calculate the area of a square(l*l) given the length of its side.
    
    Parameters:
        side (int): The length of one side of the square. Must be a positive integer.
        
    Returns:
        int: The area of the square.
    """
    return side ** 2


def area_triangle(base:int, height:int)->float:
    
    """
    Calculate the area of a triangle(1/2 * b * h) given the base length and height.
    
    Parameters:
        base (int): The length of the base of the triangle. Must be a positive integer.
        height (int): The height of the triangle. Must be a positive integer.
        
    Returns:
        float: The area of the triangle.
    """
    area = 0.5 * base * height
    return area



def area_circle(radius:int)->float:
    
    """
    Calculate the area of a circle (pi * r^2) given its radius.
    
    Parameters:
        radius (int): The radius of the circle. Must be a positive integer.
        
    Returns:
        float: The area of the circle.
    """
    
    return 0.0

def area_rectangle(length:int, width:int)->int:
    
    """
    Calculate the area of a rectangle(l*w) given its length and width.
    
    Parameters:
        length (int): The length of the rectangle. Must be a positive integer.
        width (int): The width of the rectangle. Must be a positive integer.
        
    Returns:
        int: The area of the rectangle.
    """
    
    return 0


# TODO: Complete the required shapes below
#       with reference to the unittests
def draw_square(height:int)->None:
    
    """
    Draws a square pattern of asterisks (*) with the given height and width.
    
    Parameters:
        height (int): The height and width of the square. Must be a positive integer.
        
    Returns:
        None: Prints the square pattern directly to console.
        
    """
    for _ in range(height):
        print("*" * height)



def draw_pyramid(height:int)->None:
    
    """
    Draws a centered pyramid pattern of asterisks (*) with the given height.
    
    Parameters:
        height (int): The height of the pyramid. Must be a positive integer.
        
    Returns:
        None: Prints the pyramid pattern directly to console.
        
    """
    
    pass

def draw_triangle(height:int)->None:
    
    """
    Draws a number triangle where each row contains sequential numbers from 1 to the row number.
    
    Parameters:
        height (int): The height of the triangle. Must be a positive integer.
        
    Returns:
        None: Prints the triangle pattern directly to console.
    
        
    """
    
    pass

def draw_triangle_reversed(height:int)->None:
    
    """
    Draw an inverted number triangle where each row begins with its position number, 
    with the top row having the most repeated numbers and each row below having one fewer repetition.
    
    Parameters:
        height (int): The height of the triangle. Must be a positive integer.
        
    Returns:
        None: Prints the inverted triangle pattern directly to console.
        

    """
    
    pass



         
                
# TODO: add support for other shapes
def draw(shape:str, height:int)->None:
    
    """
    Main drawing function that calls the appropriate shape-specific drawing function
    based on the requested shape type.
    
    Parameters:
        shape (str): The type of shape to draw. Must be one of:
            - "square": A square of asterisks
            - "triangle_reversed": Inverted triangle of repeated row numbers
            - "triangle": Triangle of sequential numbers
            - "pyramid": Centered pyramid of asterisks
        height (int): The height of the shape. Must be a positive integer.
        
    Returns:
        None: Prints the requested shape pattern directly to console.
    """
    
    if shape == "pyramid":
        draw_pyramid(height)

