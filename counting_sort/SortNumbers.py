# Given A = [1, 3, 6, 4, 1, 2], the function should return [1, 1, 2, 3, 4, 6].
# Given A = [1, 2, 3, 2, 3], the function should return [1, 2, 2, 3, 3]



def sort_array(numbers) :
    arr = [0 for _ in range(10)]

    for i in range(len(numbers)):
        if arr[i] != 0:
            arr[numbers[i]] = arr[numbers[i]] + 1
        else:
            arr[numbers[i]] = 1

    for i in range(len(arr)):
        if arr[i] == 1:
            print(i)
        elif arr[i] > 1:
            for j in range(arr[i]):
                print(i)




sort_array([1, 3, 6, 4, 1, 2, 3])
# [1, 3, 6, 4, 1, 2]
#0 2, 1, 1, 0, 1,