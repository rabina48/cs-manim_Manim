def find_nearest_points():
    """Find and print the nearest pair of points from user input."""
    n = int(input("Enter the number of points: "))
    points = []

    for _ in range(n):
        x, y = map(int, input("Enter the coordinates of a point (x y): ").split())
        points.append((x, y))

    min_dist = float('inf')
    nearest_pair = None

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = ((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)**0.5
            if dist < min_dist:
                min_dist = dist
                nearest_pair = (points[i], points[j])

    print("The nearest pair of points is:", nearest_pair)

# Call the function
find_nearest_points()
