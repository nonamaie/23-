def counting_sort_for_radix(arr, position):
    output_range = 10
    n = len(arr)
    output = [0] * n
    count = [0] * output_range

    for number in arr:
        index = number // position % 10
        count[index] += 1

    for i in range(1, output_range):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // position % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_number = max(arr)
    position = 1
    while max_number // position > 0:
        counting_sort_for_radix(arr, position)
        position *= 10
    return arr

# 测试基数排序
test_array = [170, 45, 75, 90, 802, 24, 2, 66]
sorted_array = radix_sort(test_array)
print("Sorted array is:", sorted_array)
