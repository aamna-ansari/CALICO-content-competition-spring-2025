import sys
import threading
def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        blocks = []
        for _ in range(N):
            x0, y0, x1, y1 = map(int, sys.stdin.readline().split())
            mass = (x1 - x0) * (y1 - y0)
            cx = (x0 + x1) / 2
            cy = (y0 + y1) / 2
            blocks.append({'x0': x0, 'y0': y0, 'x1': x1, 'y1': y1, 'mass': mass, 'cx': cx, 'cy': cy})
        parent = [-1] * N
        children = [[] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                if blocks[i]['y0'] == blocks[j]['y1']: 

                    
                    if not (blocks[i]['x1'] <= blocks[j]['x0'] or blocks[i]['x0'] >= blocks[j]['x1']):
                        parent[i] = j
                        children[j].append(i)
                        break
        stable = True
        
        def dfs(u):
            nonlocal stable
            total_mass = blocks[u]['mass']
            total_cx = blocks[u]['mass'] * blocks[u]['cx']
            total_cy = blocks[u]['mass'] * blocks[u]['cy']
            for v in children[u]:
                m, cx, cy = dfs(v)
                total_mass += m
                total_cx += m * cx
                total_cy += m * cy
            if parent[u] != -1:
                p = parent[u]
                center_x = total_cx / total_mass
                if not (blocks[p]['x0'] <= center_x <= blocks[p]['x1']):
                    stable = False
            return total_mass, total_cx / total_mass, total_cy / total_mass
        for i in range(N):
            if parent[i] == -1 and blocks[i]['y0'] == 0:
                dfs(i)
        print("Stable" if stable else "Unstable")
threading.Thread(target=main).start()