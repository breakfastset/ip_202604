import math

def calculate_circle_area(radius):
    area = math.pi * (radius ** 2)   # pi r square
    return area

def calculate_circle_perimeter(radius):
    perimeter = 2 * math.pi * radius  # 2 pi r
    return perimeter

def calculate_sphere_volume(radius):
    volume = 4 * math.pi * (radius ** 3) / 3
    return volume

def calculate_sphere_surface_area(radius):
    surface_area = 4 * math.pi * (radius ** 2)
    return surface_area

def calculate_hemisphere_surface_area(radius):
    hemisphere_surface_area = (0.5 * calculate_sphere_surface_area(radius) +
                               calculate_circle_area(radius))
    return hemisphere_surface_area