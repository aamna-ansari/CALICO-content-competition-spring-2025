import math
def cross(o, a, b):
    return (a[0] - o[0])*(b[1] - o[1]) - (a[1] - o[1])*(b[0] - o[0])
def convex_hull(points):
    points = sorted(points)
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]
def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])
def dot(a, b):
    return a[0]*b[0] + a[1]*b[1]
def min_area_rect(hull):
    n = len(hull)
    if n == 1:
        return 0.0
    if n == 2:
        return dist(hull[0], hull[1]) * 0.0
    

    ans = float('inf')
    k = 1
    for i in range(n):
        j = (i + 1) % n
        edge = (hull[j][0] - hull[i][0], hull[j][1] - hull[i][1])
        edge_len = math.hypot(edge[0], edge[1])
        edge = (edge[0]/edge_len, edge[1]/edge_len) 
        


        while True:
            k_next = (k+1)%n
            if abs(cross(hull[i], hull[j], hull[k_next])) > abs(cross(hull[i], hull[j], hull[k])):
                k = k_next
            else:
                break
        max_proj = -float('inf')
        min_proj = float('inf')

        max_width = 0
        for p in hull:
            proj = dot((p[0] - hull[i][0], p[1] - hull[i][1]), edge)
            max_proj = max(max_proj, proj)
            min_proj = min(min_proj, proj)
            width = abs(cross(hull[i], hull[j], p)) / edge_len
            max_width = max(max_width, width)
        area = (max_proj - min_proj) * max_width
        ans = min(ans, area)
    return ans


def circle():
    T = int(input())
    for _ in range(T):
        N = int(input())
        points = []
        for _ in range(N):
            x, y = map(float, input().split())
            points.append((x, y))
        hull = convex_hull(points)
        area = min_area_rect(hull)
        print(f"{area:.10f}")
circle()