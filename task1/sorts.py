def fast_sort(arr, low, high):
    if low < high:
        p = divide_and_rule(arr, low, high)
        fast_sort(arr, low, p - 1)          # fix 3: pivot already in place
        fast_sort(arr, p + 1, high)

def divide_and_rule(arr, low, high):
    p = arr[high]
    i = low - 1
    for j in range(low, high):              # fix 1: stop before the pivot
        if arr[j] <= p:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]   # fix 2: pivot goes to i+1
    return i + 1                                     # fix 2

def slow_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = slow_sort(arr[:mid])
    right = slow_sort(arr[mid:])
    return add_and_rule(left, right)

def add_and_rule(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])         # fix 4: use j, not i
            j += 1
    result += left[i:]
    result += right[j:]
    return result

if __name__ == "__main__":
    import random
    a = [3, 1, 2]
    fast_sort(a, 0, 2)
    print("fast_sort [3,1,2] ->", a)
    print("slow_sort [3,4,1,2] ->", slow_sort([3, 4, 1, 2]))
    for _ in range(1000):
        x = [random.randint(-50, 50) for _ in range(random.randint(0, 20))]
        y = x[:]
        fast_sort(y, 0, len(y) - 1)
        assert y == sorted(x), ("fast_sort failed", x, y)
        assert slow_sort(x) == sorted(x), ("slow_sort failed", x)
    print("All 1000 random tests passed")
