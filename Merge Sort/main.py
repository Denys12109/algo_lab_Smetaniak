class MergeSort:
    @staticmethod
    def sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            A = arr[:mid]
            B = arr[mid:]

            MergeSort.sort(A)
            MergeSort.sort(B)

            a = b = c = 0

            while a < len(A) and b < len(B):
                if A[a] < B[b]:
                    arr[c] = A[a]
                    a += 1
                else:
                    arr[c] = B[b]
                    b += 1
                c += 1

            while a < len(A):
                arr[c] = A[a]
                a += 1
                c += 1

            while b < len(B):
                arr[c] = B[b]
                b += 1
                c += 1
        return arr

if __name__ == "__main__":
    arr = [500, -4, 12, 48, 101]
    sorted_arr = MergeSort.sort(arr)
    print("Sorted array:", sorted_arr)

