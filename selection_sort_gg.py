class Solution: 
    def selectionSort(self, arr):
        n = len(arr)
        for i in range(n - 1):
            min_pos = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_pos]:
                    min_pos = j 
            if min_pos != i:
                arr[i], arr[min_pos] = arr[min_pos], arr[i]
        return arr

      
