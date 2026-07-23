if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr=set(arr)
    largest = max(arr)
    arr.remove(largest)
    largest = max (arr)
    print(largest)
# MISTAKE -- STILL HAVING DUPLICATE VALUES (CORRECTED USING SET())
#         --TRYING TO DO ALL THE MATH (USING MAX())
# converting map to list
# FIRST CODE
#if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     for i in range (n):
#         if arr[i]>=arr[i+1]:
#             largest=arr[i]
#             arr.remove(arr[i])
#     for i in range (n-1):
#         if arr[i]>=arr[i+1]:
#             largest=arr[i]
            
#     print(largest)
