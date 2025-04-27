def min_actions_to_visit_buttons(T, test_cases):
    results = []
    for case in test_cases:
        N, M, grid = case
        pos = {}
        for r in range(N):
            for c in range(M):
                pos[grid[r][c]] = (r, c)
        
        actions = 0
        currentR, currentC = 0, 0
        
        for num in range(1, N*M + 1):
            targetR, targetC = pos[num]
            vertiMove = min(abs(currentR - targetR), N - abs(currentR - targetR))
            horiMove = min(abs(currentC - targetC), M - abs(currentC - targetC))
            actions += vertiMove + horiMove
            currentR, currentC = targetR, targetC
        
        results.append(actions)
    return results

T = int(input())
test_cases = []
for _ in range(T):
    N, M = map(int, input().split())
    grid = []
    for _ in range(N):
        row = list(map(int, input().split()))
        grid.append(row)
    test_cases.append((N, M, grid))


answers = min_actions_to_visit_buttons(T, test_cases)

for ans in answers:
    print(ans)