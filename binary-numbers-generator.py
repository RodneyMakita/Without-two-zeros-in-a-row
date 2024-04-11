def zeros(n):
    if n == 1:
        return 2  # "0" and "1" are both valid

    # Initialize counts for n=1
    count_ending_with_0 = 1  # Only "1" is valid for n=1
    count_ending_with_1 = 1  # Only "0" is valid for n=1

    for _ in range(2, n):
        # Update counts for the current length
        new_count_ending_with_0 = count_ending_with_0 + count_ending_with_1
        new_count_ending_with_1 = count_ending_with_0

        # Update counts for the next iteration
        count_ending_with_0 = new_count_ending_with_0
        count_ending_with_1 = new_count_ending_with_1

    # Total valid numbers for length n
    return count_ending_with_0 + count_ending_with_1
