def pickup_even(items):
    result = []
    for item in items:
        if item % 2 == 0:
            result.append(item)
    return result
