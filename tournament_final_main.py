def tournament_champion(T, test_cases):
    results = []
    for case in test_cases:
        N, names, powers = case
        competitors = list(zip(names, powers))
        
        while len(competitors) > 1:
            next_round = []
            for i in range(0, len(competitors), 2):
                name1, power1 = competitors[i]
                name2, power2 = competitors[i+1]
                
                if power1 > power2:
                    next_round.append((name1, power1 + power2))
                elif power2 > power1:
                    next_round.append((name2, power1 + power2))
                else:  
                    next_round.append((name1 + name2, power1 + power2))
            competitors = next_round
        
        champion_name = competitors[0][0]
        results.append(champion_name)
    return results


T = int(input())
test_cases = []

for _ in range(T):
    N = int(input())
    names = input().split()
    powers = list(map(int, input().split()))
    test_cases.append((N, names, powers))

champions = tournament_champion(T, test_cases)
for champ in champions:
    print(champ)