import itertools

def can_connect(a, b):
    return abs( a//3 - b//3) < 2 and abs(a %3 - b%3) < 2

def is_cross(c1, n1, c2, n2):
    if frozenset([abs(c1-n1), abs(c2-n2)]) == frozenset([2,4]):
        if c1 + n1 == c2 + n2:
            return True
    return False

points = list(range(9))
paths = []
# a path is (centre, node1, node2) with node1 < node2
# a path pair is two paths with centre1 < centre2 
for p in itertools.permutations(points, 6):
    if p[0] > p[3]: # throw out bad centres
        continue
    if p[1] > p[2] or p[4] > p[5]: # throw out bad node pairs
        continue
    if not(can_connect(p[0], p[1])) or not(can_connect(p[0], p[2])):
        continue # bin disconnected first pair
    if not (can_connect(p[3], p[4])) or not (can_connect(p[3],p[5])):
        continue # bin disconnected second pair
    cross = False
    for n1 in [1,2]:
        for n2 in [4,5]:
            if is_cross( p[0], p[n1], p[3], p[n2]):
                cross = True
    if cross:
        continue
    paths.append(p)

def print_path(p):
    out = ""
    connections = [(p[0], p[1]), (p[0],p[2]),
                   (p[3], p[4]), (p[3],p[5])]
    grid = [[ " " if i%2 == 1 or j%2 == 1 else "." for i in range(5)] for j in range(5)]
    for i, pi in enumerate(p):
        x = pi % 3
        y = pi // 3
        if i < 3:
            grid[2*x][2*y] = "*"
        else:
            grid[2*x][2*y] = "o"
    for c1, c2 in connections:
        x = c1%3 + c2%3
        y = c1//3 + c2//3
        if abs(c1-c2) == 1:
            char = "|"
        elif abs(c1-c2) == 2:
            char = "/"
        elif abs(c1-c2) == 3:
            char = "-"
        elif abs(c1-c2) == 4:
            char = "\\"
        grid[x][y] = char
    for g in grid:
        out += ( "".join(g)) + "\n"
    return out

for i, p in enumerate(paths):
    print(i)
    print(print_path(p))

WIDTH = 500
HEIGHT = 500

def xy(n, k ):
    xx = k % 24
    yy = k // 24
    return (n %3 + 1) * WIDTH/4 + xx* WIDTH, (n // 3 + 1) * HEIGHT / 4 + yy * HEIGHT


def generate_svg(path, k):
    out = ""
    # circles and rects, let's not overcomplicate
    for p in range(9):
        x, y = xy(p, k)
        if p in path:
            out += f'<circle fill = "black" cx="{x}" cy="{y}" r="{WIDTH/20}"/>\n'
        else:
            # out += f'<circle fill = "black" cx="{x}" cy="{y}" r="{WIDTH/50}"/>\n'
            pass
    for i in {0,3}:
        pts = ""
        for j in [1+i, 2+i]:
            x,y = xy(path[j], k)
            X,Y = xy(path[i], k)
            pts = f" {x},{y} {X},{Y}"
            out += f'<polyline stroke="black" points = "{pts}" stroke-width="{WIDTH/50}"/>\n'
    return out

def full_svg(paths):
    out = '<svg xmlns="http://www.w3.org/2000/svg" width="12000" height="12000" viewBox="0 0 12000 12000" fill="none">\n'
    for k,p in enumerate(paths):
        out += generate_svg(p, k)
    out += "</svg>"
    return out

# with open("glyphs.svg", "w") as f:
#     f.write(full_svg(paths))

print(generate_svg((0,1,4,5,7,8),0))
print(generate_svg((1,3,4,7,5,8),0))
