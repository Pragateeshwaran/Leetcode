stages = [20, 30, 40, 20]

def frogs(stage):
    if stage == len(stages) - 1:
        return 0  # Base case: last stage
    if stage == len(stages) - 2:
        return abs(stages[stage] - stages[stage + 1])  # Second-to-last stage
    
    # Recursive case
    return min(
        frogs(stage + 1) + abs(stages[stage] - stages[stage + 1]),
        frogs(stage + 2) + abs(stages[stage] - stages[stage + 2]) if stage + 2 < len(stages) else float('inf')
    )

val = frogs(0)
print(val)

# =============================================================================================================================

stages = [20, 30, 40, 20]
diction = {len(stages) - 1: 0, len(stages) - 2: abs(stages[-2] - stages[-1])}
def frogs(stage):
    if stage in diction:
        return diction[stage]
    
    # Recursive case
    diction[stage] =  min(
        frogs(stage + 1) + abs(stages[stage] - stages[stage + 1]),
        frogs(stage + 2) + abs(stages[stage] - stages[stage + 2]) if stage + 2 < len(stages) else float('inf')
    )
    return diction[stage]
# =============================================================================================================================
val = frogs(0)
print(val)

stages = [20, 30, 40, 20]

def frogs():
    n = len(stages)
    dp = [0] * n  # DP table to store minimum costs

    dp[0] = 0  # Cost at the first stage
    dp[1] = abs(stages[1] - stages[0])  # Cost at the second stage

    for i in range(2, n):
        dp[i] = min(
            dp[i - 1] + abs(stages[i] - stages[i - 1]),
            dp[i - 2] + abs(stages[i] - stages[i - 2])
        )
    
    return dp[n - 1]  # Minimum cost to reach the last stage

val = frogs()
print(val)
