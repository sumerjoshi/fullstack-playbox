
"""
Activity Selection is essentially a dynamic programming problem.
However, for activity selection, we can select the greedy choice, which is:
1. Being able to select increasing start time
2. Being able to select increasing finish time.

This is better because being greedy allows you to make the optimal choice for a solution.
Part 1. Non-conflicting
Part 2. conflicting

For this, let's assume that activities are tuples

Sample Input:
(1,4), (3,5), (0,6) (5,7) (3,8), (5,9) (6,10) (8,11) (8,12) (2,13) (2,14)

Sample Output:
(1,4) (5,7) (8,11) (12,14)

Let's call sample input as activities

Pseudocode:
    GAFS(activities)
    n = activities.length
    k = 0 (Last Selected Activity)
    output_activities = {}
    for i from 1 to len(activities):
        if activities[i][0] >= activities[k][1]
            output_activities.add(k)
            k = i
    return output_activities

"""


def greedy_activity_selector_iterative(activities):
    n = len(activities)
    k = 0
    output_activities = set()
    output_activities.add(0)
    for i in range(1, n):
        if activities[i][0] >= activities[k][1]:
            output_activities.add(i)
            k = i
    return output_activities


