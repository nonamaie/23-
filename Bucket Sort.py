def bucketsort(arr):
    numbuckets = len(arr)
    buckets = [[] for _ in range(numbuckets)]

    for x in arr:
        index = int(x * numbuckets)
        buckets[index].append(x)
    for bucket in buckets:
        bucket.sort()
    # 4. 合并桶
    sortedarray = []
    for bucket in buckets:
        sortedarray.extend(bucket)
    return sortedarray
# 测试桶排序
testarray = [0.42, 0.61, 0.05, 0.311, 0.10, 0.85, 0.30, 0.22]
sortedarray = bucketsort(testarray)
print("Sorted array is:", sortedarray)
