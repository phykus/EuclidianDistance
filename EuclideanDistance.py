#EuclideanDistance

import math

# Function to calculate Euclidean distance between two points
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# Two points needed to calculate Euclidean distance"
n = 2

# List to store the user-provided points
points = []

# Asking the user to input the points
for i in range(n):
    x = float(input("Nokta " + str(i+1) + " için x değerini girin: "))
    y = float(input("Nokta " + str(i+1) + " için y değerini girin: "))
    points.append((x, y))

# List to store distances between each pair of points
distances = []

# Calculate the distance between each pair of points and append it to the distances list
for i in range(len(points)):
    for j in range(i+1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# The distances are stored in a list
print ("Mesafeler : " , distances)
# Find and print the minimum distance
min_distance = min(distances)

print("Noktalar arasındaki minimum mesafe: " , min_distance)
