def maximumHappinessSum(happiness, k):
    happiness.sort(reverse=True)

    total_happiness_sum = 0
    turns = 0
    # Calculate the maximum happiness sum
    for i in range(k):
        # Adjust happiness and ensure it's not negative
        total_happiness_sum += max(happiness[i] - turns, 0)
        # Increment turns for the next iteration
        turns += 1
    return total_happiness_sum
maximumHappinessSum([1,2,3],2)