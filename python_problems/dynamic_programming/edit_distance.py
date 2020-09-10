
"""
Edit Distance Problem.
Inputs, two strings, with lengths
Output: Minimum number of operations to do changes.
"""
def edit_distance(string1, string2, m, n):

    # If the cost of m is 0, this means that there is the only
    # option of inserting all elements of n.

    if m == 0:
        return n

    # If the second string has a cost 0, that means you can only
    # have the option of inserting all the elements of m

    if n == 0:
        return m

    # If the last characters of the currenct iteration between both
    # strings is equal, then you need to move forward with iteration
    if string1[m-1] == string2[n -1]:
        return edit_distance(string1, string2, m- 1, n - 1)

    # Recursive Call:
    # Always want to take the minimum cost of each of these iterations, which ends up being O(3^N)
    minimum_cost = min(edit_distance(string1, string2, m - 1, n),
                       edit_distance(string1, string2, m, n - 1),
                       edit_distance(string1, string2, m - 1, n - 1))

    return 1 + minimum_cost


def editDistanceDP(string1, string2, m, n):
    # Create Table to form values
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if m == 0:
                # If m = 0, we know that it will take take j operations to complete
                dp[i][j] = j

            if n == 0:
                # If n = 0, we know that it will take i operations to complete
                dp[i][j] = i

            if string1[m - 1] == string2[n - 1]:
                dp[i][j] = dp[i - 1][j - 1]

            else:
                dp[i][j] = 1 + min(
                    dp[i][j - 1],
                    dp[i - 1][j],
                    dp[i - 1][j - 1]
                )

    return dp[m][n]