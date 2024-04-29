class InsertionSort:
    @staticmethod
    def sort(arr):
        for i in range(1, len(arr)):
            abc = arr[i]
            j = i - 1
            while j >= 0 and abc < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = abc
        return arr

# Приклад використання
if __name__ == "__main__":
    arr = [100, 138, 1, -2, 99]
    sorted_arr = InsertionSort.sort(arr)
    print("Sorted array:", sorted_arr)

