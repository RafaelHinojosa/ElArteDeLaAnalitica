"""
    Author: Rafael Hinojosa López
    Matrícula: A01705777
    Fecha: 14 - Enero - 2022
"""

from random import randint
import math

# 1. Generate random amount of points
noPoints = randint(5, 8)
print('No. Points: ' + str(noPoints))

# 2. Generate random k value of centers
kCenters = randint(2, 3)
print('No. Centers: ' + str(kCenters))

# 3. Create list and push 'noPoints' random values with x and y coordinates
points = []
for point in range(0, noPoints): 
    x = randint(0, 5)
    y = randint(0, 5)
    points.append([x, y])

print('Puntos: ' + str(points))

# 4. Generate the centers and append them to a list
centers = []
for center in range(0, kCenters):
    x = randint(0, 6)
    y = randint(0, 6)
    centers.append([x, y])

print('Centros: ' + str(centers))


# Helper function to calculate euclidean distance between 2 points
def getDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# 5. For each point, assign them their closest center
groups = []

def getEmptyGroups():
    _emptyGroups = []

    for index in range(0, len(centers)):
        _emptyGroups.append([])
    
    return _emptyGroups

emptyGroups = getEmptyGroups()

def generateGroups(points):
    newGroups = emptyGroups

    for point in points:
        minDistance = 1e10
        minCenter = 0

        for centerIndex in range(0, len(centers)):
            center = centers[centerIndex]
            distance = getDistance(point, center)
            if distance < minDistance:
                minDistance = distance
                minCenter = centerIndex
        
        newGroups[minCenter].append(point)

    return newGroups

groups = generateGroups(points)
print('Grupos Iniciales: ' + str(groups))

# 6. Change centers location until the avg distance to all their points is the minimum
def getNewCenter(points):
    sumX = 0
    sumY = 0
    noPoints = len(points)

    if noPoints == 0:
        return [0, 0]
    
    for point in points:
        sumX += point[0]
        sumY += point[1]

    newX = sumX / noPoints
    newY = sumY / noPoints

    return [newX, newY]

maxIterations = 500
def relocateCenters(_groups):
    aCenterChanged = False

    for centerIndex in range(0, len(centers)):
        newCenter = getNewCenter(_groups[centerIndex])
        
        if newCenter != centers[centerIndex]:
            aCenterChanged = True
            centers[centerIndex] = newCenter
    
    return aCenterChanged

def kMeans(iterationNo):
    # 1. Classify variables into groups
    newGroups = generateGroups(points)

    # 2. Relocate Centers 
    aCenterChanged = relocateCenters(newGroups)
    
    # 3. Repeat process until centers don't move
    if iterationNo >= maxIterations or aCenterChanged == False:
        return newGroups
    else:
        return kMeans(iterationNo + 1)

groups = kMeans(1)
print('Los grupos quedan así: ' + str(groups))