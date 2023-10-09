def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def main(arr, target):
    if sorted(arr) != arr:
        arr.sort()
        print(f"Массив не отсортирован. Отсортированный массив: {arr}")
    
    result = binary_search(arr, target)
    if result != -1:
        print(f"Элемент {target} найден по индексу {result}.")
    else:
        print(f"Элемент {target} не найден в массиве.")

main([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
main([10, 32, 3, 1, 8, 64, 2, 58, 1, 32], 3)