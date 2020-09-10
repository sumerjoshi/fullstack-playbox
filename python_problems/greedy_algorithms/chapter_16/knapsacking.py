
"""
Dynamic programming problem of 0-1 knapsack

Inputs are n number of items, and W is the maximum weight that you can put in the knapsack
We need to compare the number of items to the weights, and be able to subtract from the weight
    Assume that W-wj where the weight remaning is of n-1 items

Form the formula (or recurrence)



Knapsack(n, W):
   Initialize table K to be [[0 for x to n+1] for x to W+1]
   from i to range(W+1)
      from j to range(n+1)
"""




"""
Fractional Knapsack 0-1
Here we have weights w, values v, with value to weight ratio
"""


class ItemValue(object):

    def __init__(self):
        pass
