import shape_functions

def main():
    radius = float(input("Enter radius: "))
    circle_area = shape_functions.calculate_circle_area(radius)
    circle_perimeter = shape_functions.calculate_circle_perimeter(radius)
    sphere_volume = shape_functions.calculate_sphere_volume(radius)
    sphere_surface_area = shape_functions.calculate_sphere_surface_area(radius)
    hemisphere_surface_area = shape_functions.calculate_hemisphere_surface_area(radius)

    print(f"Area of circle: {circle_area:.2f}")
    print(f"Perimeter of circle: {circle_perimeter:.2f}")
    print(f"Volume of sphere: {sphere_volume:.2f}")
    print(f"Surface area of sphere: {sphere_surface_area:.2f}")
    print(f"Surface area of hemisphere: {hemisphere_surface_area:.2f}")

main() # call main

