def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for a in arr:
        count[a] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    output = [0] * len(arr)
    for a in reversed(arr):
        output[count[a] - 1] = a
        count[a] -= 1
    for i in range(len(arr)):
        arr[i] = output[i]
# 测试计数排序
test_array = [4, 2, 2, 8, 3, 3, 1]
counting_sort(test_array)
print("Sorted array is:", test_array)
