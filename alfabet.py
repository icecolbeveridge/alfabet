import itertools

def is_valid(a,b,c):
    # exclude if two are on one margin and one opposite
    xs = set({a.x, b.x, c.x})
    ys = set({a.y, b.y, c.y})
    if len(xs) == 2 and 1 not in xs:
        return False 
    if len(ys) == 2 and 1 not in ys:
        return False
    return True

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
    def __hash__(self):
        return hash(f"{self.x},{self.y}")
    def __repr__(self):
        return f"({self.x},{self.y})"

def no_intersection(p1, p2):
    s1 = set(p1)
    s2 = set(p2)
    return len(s1.union(s2)) == 6
 
points = [Point(x,y) for x in range(3) for y in range(3)]
validgroups = []
validpairs = []
for p in itertools.combinations(points, 3):
    if is_valid(p[0],p[1],p[2]):
        validgroups.append(p)

for p in itertools.combinations(validgroups, 2):
    if no_intersection(p[0], p[1]):
        validpairs.append(p)

for (p,q) in validpairs:
    out = [["." for i in range(3)] for j in range(3)]
    for pi in p:
        out[pi.x][pi.y] = "*"
    for qi in q:
        out[qi.x][qi.y] = "%"
    for l in out:
        print( "".join(l))
    print()
                    
