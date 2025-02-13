def binary_search(nums, k, lo, hi):    
    while lo <= hi:
        mid = int((lo+hi) / 2)
        
        if nums[mid] == k:
            return mid
        elif nums[mid] < k:
            lo = mid + 1
        else:
            hi = mid - 1
    
    return -1
            
            
def exponencial_search(arr, target):
    if arr[0] == target:
        return 0
    n = len(arr)
    i = 1
    
    while i < n and arr[i] < target:
        i *= 2
    
    return binary_search(arr, target, i//2, min(i, n-1))

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 10
result = exponencial_search(arr, target)
print(result)