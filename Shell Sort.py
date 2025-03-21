def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:

        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

    return arr

# 测试函数
test_array = [64, 34, 25, 12, 22, 11, 90]
sorted_array = shell_sort(test_array)
print(sorted_array)


