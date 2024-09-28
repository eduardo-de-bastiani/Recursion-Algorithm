def rec(path, pos=0, last_jump_was_three=False):
    # Base case: if we're exactly at the last 'm', return 1
    if pos == len(path) - 1:
        return 1
    
    # If we're out of bounds or on a "0" (gap), return 0
    if pos >= len(path) or path[pos] == '0':
        return 0
    
    # Try to make 1, 2, or 3 meter jumps from this rock
    ways = 0
    
    # 1-meter jump (always allowed)
    ways += rec(path, pos + 1, False)
    
    # 2-meter jump (always allowed)
    ways += rec(path, pos + 2, False)
    
    # 3-meter jump (only allowed if the last jump wasn't 3 meters)
    if not last_jump_was_three:
        ways += rec(path, pos + 3, True)
    
    return ways


def rec_memo(path, pos=0, last_jump_was_three=False, memo=None):
    # Initialize memoization dictionary if not already done
    if memo is None:
        memo = {}
    
    # Memoization key: the current position and whether the last jump was 3 meters
    key = (pos, last_jump_was_three)
    
    # If the result for this state is already computed, return it
    if key in memo:
        return memo[key]
    
    # Base case: if we're exactly at the last 'm', return 1 (we've crossed the river)
    if pos == len(path) - 1:
        return 1
    
    # If we're out of bounds or on a "0" (gap), return 0 (invalid path)
    if pos >= len(path) or path[pos] == '0':
        return 0
    
    # Try to make 1, 2, or 3 meter jumps from this rock
    ways = 0
    
    # 1-meter jump (always allowed)
    ways += rec_memo(path, pos + 1, False, memo)
    
    # 2-meter jump (always allowed)
    ways += rec_memo(path, pos + 2, False, memo)
    
    # 3-meter jump (only allowed if the last jump wasn't 3 meters)
    if not last_jump_was_three:
        ways += rec_memo(path, pos + 3, True, memo)
    
    # Store the result in the memo dictionary before returning
    memo[key] = ways
    
    return ways


def non_recursive(path):
    n = len(path)
    # Edge case: If the path is too short or only contains "m" and "0"s
    if n == 0 or path[0] != 'm' or path[-1] != 'm':
        return 0
    # Initialize the dp array with 0's
    # dp[i][j] represents ways to reach position i, where j is 0 if last jump wasn't 3, 1 if it was
    dp = [[0, 0] for _ in range(n)]
    dp[0][0] = 1  # There's one way to start from the first "m"

    # Loop through each position and calculate ways to reach it
    for i in range(1, n):
        if path[i] == '0':  # Skip if the current position is a gap
            continue
        # Check 1-meter back
        if i - 1 >= 0:
            dp[i][0] += dp[i-1][0] + dp[i-1][1]
        # Check 2-meters back
        if i - 2 >= 0:
            dp[i][0] += dp[i-2][0] + dp[i-2][1]
        # Check 3-meters back
        if i - 3 >= 0:
            dp[i][1] += dp[i-3][0]  # Only if last jump wasn't 3 meters

    # The result will be the sum of ways to reach the last position (the final 'm')
    return dp[-1][0] + dp[-1][1]




# Example usage
path = "m10101100111m"
print("recursivo: ", rec(path))  # Expected output: 5


# Example usage
path = "m10101100111m"
print("memorizada: ", rec_memo(path))  # Expected output: 5

# Example usage
path = "m10101100111m"
print("sem recursão: ", non_recursive(path))  # Expected output: 5
