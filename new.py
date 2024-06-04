
results = []

for i in range():
    n, d, costs = results[i]
    max_tickets = 0

    # Initialize the DP table outside the loop
    dp = [[0] * n for i in range(d + 1)]

    for i in range(n):
        for j in range(n):
            if i != j:
                dp[1][j] = costs[i][j]

    # Fill in the DP table
    for k in range(2, d + 1):
        for j in range(n):
            if i != j:
                for l in range(n):
                    if i != l and j != l:
                        dp[k][j] = max(dp[k][j], dp[k - 1][l] + costs[j][l])

    # Update max_tickets for the current test case
    max_tickets = max(max_tickets, max(dp[d]))

    results.append(max_tickets)

# Input
t = int(input())
test_cases = []
for _ in range(t):
    n, d = map(int, input().split())
    costs = []
for _ in range(n):
    row = list(map(int, input().split()))
    costs.append(row)
    test_cases.append((n, d, costs))

# Calculate and output the results
results = max_tickets(t, test_cases)
for result in results:
    print(result)
