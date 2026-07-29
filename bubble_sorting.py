###using else 
for i in range (len(arr)):
  for j in range ((len(arr))-i-1):
     if arr[j]<arr[j+1]:
        arr[j],arr[j+1]=  arr[j+1],arr[j]
  else break  
return arr
### using flag
for i in range (len(arr)):
  swapped=False
  for j in range ((len(arr))-i-1):
     if arr[j]<arr[j+1]:
        swapped=True
        arr[j],arr[j+1]=  arr[j+1],arr[j]
  if (!swapped): break
return arr

#here we used break for the best case O(N)
