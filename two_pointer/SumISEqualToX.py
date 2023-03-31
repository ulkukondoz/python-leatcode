# Given a sorted array A (sorted in ascending order),
# find if there exists any pair of elements
# (A[i], A[j]) such that their sum is equal to X.

# numbers = {10, 20, 35, 50, 75, 80}
# total = 85
def find_sum_of_two_num_(numbers, total):
    i = 0
    j = len(numbers) - 1

    while i < j:
        if numbers[i] + numbers[j] == total:
            print('number[{}] + number[{}] = {}'.format(i, j, total))
            i += 1
            j -= 1
        elif numbers[i] + numbers[j] > total:
            j -= 1
        elif numbers[i] + numbers[j] < total:
            i += 1


find_sum_of_two_num_([10, 20, 35, 50, 75, 80], 85)
