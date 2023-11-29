import math
from config import SCREEN_HEIGHT, SCREEN_WIDTH

# Precalculated starting points for cube
points = [
(342.5, 257.5),
(342.5, 222.5),
(377.5, 222.5),
(377.5, 257.5),
(325, 275),
(325, 205),
(395, 205),
(395, 275)
]

original_points = [
[-1, 1, 1],
[-1, -1, 1],
[1, -1, 1],
[1, 1, 1],
[-1, 1, -1],
[-1, -1, -1],
[1, -1, -1],
[1, 1, -1]
]

rotated_3d_points = [list(point) for point in original_points]
# angle_deg = 60.0
z_offset = -4.0
cube_size = 300.0

def Calculate_Cube(angle_deg):
    for i in range(len(original_points)):
        # Create a new list for each iteration
        rotated_3d_point = [0, 0, 0]

        # Apply rotation
        rotated_3d_point[0] = original_points[i][0] * math.cos(math.radians(angle_deg)) - original_points[i][2] * math.sin(math.radians(angle_deg))
        rotated_3d_point[1] = original_points[i][1]
        rotated_3d_point[2] = original_points[i][0] * math.sin(math.radians(angle_deg)) + original_points[i][2] * math.cos(math.radians(angle_deg)) + z_offset

        # Update rotated_3d_points with the new list
        rotated_3d_points[i] = rotated_3d_point

    for i in range(len(rotated_3d_points)):
        # 3d positions => 2d projection
        point_x = (SCREEN_WIDTH / 2) + rotated_3d_points[i][0] / rotated_3d_points[i][2] * cube_size
        point_y = (SCREEN_HEIGHT / 2) + rotated_3d_points[i][1] / rotated_3d_points[i][2] * cube_size
        points[i] = (point_x, point_y)

def Draw_Cube(line_color, screen, pygame, line_width = 3):
    pygame.draw.line(screen, line_color, points[0], points[1], width=line_width)
    pygame.draw.line(screen, line_color, points[1], points[2], width=line_width)
    pygame.draw.line(screen, line_color, points[2], points[3], width=line_width)
    pygame.draw.line(screen, line_color, points[3], points[0], width=line_width)
    
    pygame.draw.line(screen, line_color, points[4], points[5], width=line_width)
    pygame.draw.line(screen, line_color, points[5], points[6], width=line_width)
    pygame.draw.line(screen, line_color, points[6], points[7], width=line_width)
    pygame.draw.line(screen, line_color, points[7], points[4], width=line_width)
    
    pygame.draw.line(screen, line_color, points[4], points[0], width=line_width)
    pygame.draw.line(screen, line_color, points[5], points[1], width=line_width)
    pygame.draw.line(screen, line_color, points[6], points[2], width=line_width)
    pygame.draw.line(screen, line_color, points[7], points[3], width=line_width)
    
Calculate_Cube(0)