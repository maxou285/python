#Se rendre dans le bon répertoire sinon le ficheir ne sera pas trouvé
# On prend les 6 coordonnées des 3 points d'un triangle et on regarde si l'origine est à l'intérieur du triangle 
triangles= [list(map(int, line.split(","))) for line in open("p102triangles.txt")]
print(sum((ax * by > ay * bx and bx * cy > by * cx and cx * ay > cy * ax) or (ax * by < ay * bx and bx * cy < by * cx and cx * ay < cy * ax)for ax, ay, bx, by, cx, cy in triangles))

"""
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
f = open('triangles.txt','r+')
ans = 0
for line in f:
    c = line.split(',')
    p1,p2,p3 = (int(c[0]),int(c[1])),(int(c[2]),int(c[3])),(int(c[4]),int(c[5]))
    point = Point(0,0)
    polygon = Polygon([p1,p2,p3])
    if polygon.contains(point): ans += 1
print(ans)"""