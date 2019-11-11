import math


def poisonousPlants(plants):
    stack = []
    maxDays = -math.inf

    for plant in plants:
        days = 1

        while stack and stack[-1][0] >= plant:
            _, d = stack.pop()
            days = max(days, d + 1)

        if not stack:
            days = 0

        maxDays = max(maxDays, days)
        stack.append((plant, days))

    return maxDays












