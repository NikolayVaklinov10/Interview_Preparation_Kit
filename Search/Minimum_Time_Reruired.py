def minTime(machines, goal):

    machines.sort()

    low_rate = machines[0]
    lower_bound = (goal // (len(machines) / low_rate))
    high_rate = machines[-1]
    upper_bound = (goal // (len(machines) / high_rate)) + 1

    while lower_bound < upper_bound:

        num_days = (lower_bound + upper_bound) // 2
        total = getNumItems(machines, goal, num_days)
        if total >= goal:
            upper_bound = num_days
        else:
            lower_bound = num_days + 1

    return int(lower_bound)


def getNumItems(machines, goal, num_days):

    total = 0

    for machine in machines:
        total += (num_days // machine)

    return total

# Note: lower_bound and upper_bound are the lowest
# and highest rates possible if using the slowest and
# faster machines, respectively.
