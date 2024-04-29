class SelectionSort:
    @staticmethod
    def sort(arr):
        a = len(arr)
        for i in range(a):
            min = i
            for j in range(i + 1, a):
                if arr[j] < arr[min]:
                    min = j
            arr[i], arr[min] = arr[min], arr[i]
        return arr

if __name__ == "__main__":
    arr = [1090, 57, -89, 3, 0]
    sorted_arr = SelectionSort.sort(arr)
    print("Sorted array:", sorted_arr)

