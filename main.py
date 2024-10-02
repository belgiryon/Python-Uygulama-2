import math

#ilk aşama mesafeler listesi
points = [(1, 2), (3, 4), (6, 8), (2, 5), (9, 12)]

# Öklid uzaklık fonksiyonu
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

#Tüm noktalar arasındaki mesafeleri hesaplayın
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

# minimum mesafe sonuç
min_distance = min(distances)
print(f"\n Minimum Mesafe: {min_distance:.4f}")