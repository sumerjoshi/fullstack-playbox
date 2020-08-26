

"""
LCS

1. Declare variables that are listed
2. Create table for bottom up remembering of data
3. Complete optimal substructure in terms of notes

"""
def lcs(item_x, item_y):
    m = len(item_x)
    n = len(item_y)
    table = [[0]*(n+1) for i in range(m+1)]

    """
    We are building from X[0...i-1] and Y[0...j-1]
    """
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif item_x[i-1] == item_y[j-1]:
                table[i][j] = table[i-1][j-1]+1
            else:
                table[i][j] = max(table[i][j-1], table[i-1][j])
    return table[m][n]


answer = lcs("AGGTAB", "GXTXAYB")
print("LCS IS {}".format(answer))

