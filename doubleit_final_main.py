def calculate_payout(test_cases):

    results = []

    

    for case in test_cases:

        N, choices = case

        current_offer = 1

        total_payout = 0

        

        for choice in choices:

            if choice == 'T':

                total_payout += current_offer

                current_offer = 1  

            elif choice == 'D':

                current_offer *= 2  

        

        results.append(total_payout)

    

    return results




T = int(input())

test_cases = []


for _ in range(T):

    N = int(input())

    choices = input().strip()

    test_cases.append((N, choices))




results = calculate_payout(test_cases)




for result in results:

    print(result)