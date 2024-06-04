import math

# Function to calculate the area of a triangle formed by three points
def triangle_area(A, B, C):
    return 0.5 * abs(A[0] * (B[1] - C[1]) + B[0] * (C[1] - A[1]) + C[0] * (A[1] - B[1]))

# Function to check if two line segments intersect
def segments_intersect(A, B, C, D):
    def cross_product(p1, p2):
        return p1[0] * p2[1] - p1[1] * p2[0]
    
    def subtract_points(p1, p2):
        return p1[0] - p2[0], p1[1] - p2[1]
        
    def is_between(p1, p2, p3):
        cross = cross_product(subtract_points(p1, p2), subtract_points(p3, p2))
        if abs(cross) > 1e-9:
            return False
        dot_product = (p1[0] - p2[0]) * (p3[0] - p2[0]) + (p1[1] - p2[1]) * (p3[1] - p2[1])
        if dot_product < 0:
            return False
        squared_length_p2_p1 = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
        if dot_product > squared_length_p2_p1:
            return False
        return True

    p1 = subtract_points(A, B)
    p2 = subtract_points(C, B)
    p3 = subtract_points(D, B)
    
    cross1 = cross_product(p1, p2)
    cross2 = cross_product(p1, p3)
    
    if cross1 * cross2 >= 0:
        return False
    
    p1 = subtract_points(C, D)
    p2 = subtract_points(A, D)
    p3 = subtract_points(B, D)
    
    cross1 = cross_product(p1, p2)
    cross2 = cross_product(p1, p3)
    
    if cross1 * cross2 >= 0:
        return False
    
    return True

# Function to calculate the area of a polygon defined by a list of vertices
def polygon_area(polygon):
    area = 0.0
    for i in range(len(polygon)):
        j = (i + 1) % len(polygon)
        area += polygon[i][0] * polygon[j][1] - polygon[j][0] * polygon[i][1]
    return 0.5 * abs(area)

# Read input values
N, M = map(int, input().split())

vertices = []
for _ in range(N):
    x, y = map(float, input().split())
    vertices.append((x, y))

diagonals = []
for _ in range(M):
    u, v = map(int, input().split())
    diagonals.append((u - 1, v - 1))  # Adjust indices to 0-based

# Precompute intersection checks
intersects = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(i + 2, N):
        for k in range(N):
            if k != i and k != j:
                if segments_intersect(vertices[i], vertices[j], vertices[k], vertices[(k + 1) % N]):
                    intersects[i][j] = True
                    intersects[j][i] = True

# Initialize a table for dynamic programming
dp = [[0.0 for _ in range(M + 1)] for _ in range(N)]

# Use a dictionary to store computed polygon areas
polygon_areas = {}
for i in range(N):
    for j in range(N):
        if i != j and not intersects[i][j]:
            if (i, j) not in polygon_areas:
                polygon_areas[(i, j)] = polygon_area(vertices[i], vertices[j], vertices[(j + 1) % N])

# Dynamic Programming
for m in range(1, M + 1):
    for i in range(N):
        for j in range(m):
            max_area = dp[i][m]  # Store the current value in a separate variable
            max_area = max(max_area, polygon_areas.get((i, i), 0) + dp[i][j])
            for u, v in diagonals:
                if u == i:
                    max_area = max(max_area, polygon_areas.get((u, v), 0) + dp[v][m - 1])
            dp[i][m] = max_area  # Assign the updated value to dp[i][m]

# Find the maximum area by considering all starting vertices
max_total_area = max(dp[i][M] for i in range(N))

# Output the result
print(int(2 * max_total_area))
