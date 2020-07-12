# Amazon series Easy Question 1.
# Problem : Find if given four points form a square.
# Input : Four Points (Each has 2 coordinates).
# Output : True/ False.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# return distance in (^2) ie square
def getDistInSquare(p1, p2):
    return (p1.x - p2.x)**2 + (p1.y - p2.y)**2

# returns if points form a square

# Else return false.
def isSquare(p1, p2, p3, p4):
    # d1 = d2 and d3 = √2 * d2 and d(P2,P4) = √2 * d(P2, P3). If so return true.
    # d1 = d3 and d2 = √2 * d3 and d(P2, P3) = √2 * d(P2, P4). If so return true.
    # d2 = d3 and d1 = √2 * d3 and d(P3, P4) = √2 * d(P2, P3).. If so return true.
    d1 = getDistInSquare(p1, p2)
    d2 = getDistInSquare(p1, p4)
    d3 = getDistInSquare(p1, p3)

    if d1==0 or d2==0 or d3==0:
        return False

    if d1==d2 and d3==2*d2 and getDistInSquare(p2,p4)==2*getDistInSquare(p2, p3):
        return True
    elif d1==d3 and d2==2*d3 and getDistInSquare(p2, p3)==2*getDistInSquare(p2, p4):
        return True
    elif d2==d3 and d1==2 * d3 and getDistInSquare(p3, p4)== 2 * getDistInSquare(p2, p3):
        return True
    else:
        return False

if __name__ == "__main__":
    p1 = Point(0, 0)
    p2 = Point(0, 10)
    p3 = Point(10, 0)
    p4 = Point(10, 10)
    if isSquare(p1, p2, p3, p4):
        print("The given points form a square")
    else:
        print("THe given points dose not form a square")
