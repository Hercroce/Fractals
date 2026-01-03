import math

def add_turned_point(coords, command="right"):
    if len(coords) < 2:
        raise ValueError("Need at least two coordinates to determine direction")
    
    if command == "right":
        degress = 90
    
    else:
        degress = 270

    x_prev, y_prev = coords[-2]
    x_curr, y_curr = coords[-1]

    # Calculate current direction (angle in radians)
    dx = x_curr - x_prev
    dy = y_curr - y_prev
    angle = math.atan2(dy, dx)

    # Turn by the specified angle (convert to radians)
    angle += math.radians(degress)

    # New point 1 unit away in that direction
    new_x = x_curr + math.cos(angle)
    new_y = y_curr + math.sin(angle)

    coords.append((new_x, new_y))
    return coords

initial_coordinates = [[0,0],[1,0]]
curve = add_turned_point(initial_coordinates)
curve = add_turned_point(curve, "left")
print(curve)