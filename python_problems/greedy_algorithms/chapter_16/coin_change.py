"""
Coin Change Pseudo code
We want to define the minimum number of coins
# Naive recursive python program

if V == 0, then 0 coins required.
If V > 0, mincoins(coins[0..m-1], v) = min{1 + minCoins(v-coin[i])} where i is valuues from 0
to m-1 and coin[i] <= v
"""

import sys


# V is the value of the number of cents
# m is the size of the coins array(number of different coins)
# coins is the list of the values of coins [25,10,5,1]
def minCoins(coins, m, V):
    if V == 0: return 0

    # Initialize result
    res = sys.maxsize

    # Try every coin that has a smaller value of V
    for i in range(0, m):
        if (coins[i] <= V):
            sub_res = minCoins(coins, m, V - coins[i])

            if (sub_res != sys.maxsize and sub_res + 1 < res):
                res = sub_res + 1

    return res


coins = [9, 6, 5, 1]
m = len(coins)
V = 11
print("Minimum coins required is", minCoins(coins, m, V))
