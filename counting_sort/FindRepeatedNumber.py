# Given A = [1, 3, 6, 4, 1, 2], the function should return 1-2.
# Given A = [1, 2, 3, 2, 3], the function should return 2-2, 3-2.


def find_repeated_number(numbers):
    temp = [0 for _ in range(10)]

    for i in range(len(numbers)):
        if temp[numbers[i]] != 0:
            temp[numbers[i]] = temp[numbers[i]] + 1
        else:
            temp[numbers[i]] = 1

    print(temp)

    for i in range(len(temp)):
        if temp[i] > 1:
            print('number {} is repeated {} times'.format(i, temp[i]))


find_repeated_number([1, 3, 1, 2, 4, 3, 5, 6, 7])

