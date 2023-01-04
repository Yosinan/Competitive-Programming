class Solution: 
    def select(self, arr, i):
        # code here 
        mini = i
        for j in range(i+1,len(arr)):
            if arr[mini] > arr[j]:
                mini = j
        return mini
        
    def selectionSort(self, arr,n):
        
        #code here
        for j in range(n):
            k = 0
            mini = arr[j]
            for i in range(j+1, n):
                if arr[i] < mini:
                    mini = arr[i]
                    a = i
                    k = 1
            if k ==1:
                temp = arr[j]
                arr[j] = mini
                arr[a] = temp