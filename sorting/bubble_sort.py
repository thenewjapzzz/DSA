def bubble_sort(arr):
    n = len(arr)
    for _ in range(n):
        is_sorted = True
        print(arr)
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                is_sorted =  False
                arr[j], arr[j+1] = arr[j+1], arr[j]
        
        if is_sorted:
            return
                
bubble_sort([1, 2, 3, 4, 5])