class ShellSort:
    @staticmethod
    def sort(arr):
        a = len(arr)
        num = a // 2
        while num > 0:
            for i in range(num, a):
                temp = arr[i]
                j = i
                while j >= num and arr[j - num] > temp:
                    arr[j] = arr[j - num]
                    j -= num
                arr[j] = temp
            num //= 2
        return arr

if __name__ == "__main__":
    arr = [199, 47, 512, -1, 30]
    sorted_arr = ShellSort.sort(arr)
    print("Sorted array:", sorted_arr)

