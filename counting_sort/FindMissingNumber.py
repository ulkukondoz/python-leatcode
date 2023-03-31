# Write a function:
# class Solution { public int solution(int[] A); }
#
# that, given an array A of N integers, returns the smallest positive integer
# (greater than 0) that does not occur in A.
#
# For example,
# Given A = [1, 3, 6, 4, 1, 2], the function should return 5.
# Given A = [1, 2, 3], the function should return 4.
# Given A = [−1, −3], the function should return 1.
#
# Write an efficient algorithm for the following assumptions:
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].

def find_missing_num(numbers):
    arr = [0 for _ in range(10)]

    for i in range(len(numbers)):
        if numbers[i] < 0:
            continue
        else:
            arr[numbers[i]] = numbers[i]

    print(arr)

    for i in range(len(arr)):
        if i != 0 and arr[i] == 0:
            return arr[i - 1] + 1


missingNum = find_missing_num([1, 3, 6, 4, 1, 2])
print(f"Missing num in [1, 3, 6, 4, 1, 2] is", missingNum)

missingNum = find_missing_num([1, 2, 3])
print(f"Missing num in [1, 2, 3] is", missingNum)

missingNum = find_missing_num([-1, -3])
print(f"Missing num in [-1, -3] is", missingNum)
