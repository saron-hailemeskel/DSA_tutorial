n=len(arr)
for i in range(n):
  min_pos=i
  for j in range(i+1, n):
    if (arr[j]<arr[min_pos]):
      min_pos=j #finding the minimum
  if (min_pos!= i):# inorder to not change if the index and min postion value are in the same index
    arr[i],arr[min_pos]=arr[min_pos],arr[i]
 return arr
##best and worst case both O(N^2)
      
