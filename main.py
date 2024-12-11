def calculate_average(*grades):
    if not grades:
        return 0
    total = sum(grades)
    count = len(grades)
    average = total / count

    return average