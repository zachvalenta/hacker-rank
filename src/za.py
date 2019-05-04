def container_ship(cons, stamps):
    """
    consumption = [3, 5, 2, 1]
    timestamps = [0, 3, 5, 8]

    0 to 3 = 3 hours * 3 = 9 tons consumed
    3 to 5 = 2 hours * 6 = 10 tons consumed
    5 to 8 = 3 hours * 2 = 6 tons consumed

    25 tons total
    """
    total_cost = 0
    for x, y in zip(cons, stamps):
        next_i = stamps.index(y) + 1
        if next_i <= len(stamps) - 1:
            next_val = stamps[next_i]
            elapsed_time = next_val - y
            current_cost = elapsed_time * x
            total_cost += current_cost
    return total_cost
