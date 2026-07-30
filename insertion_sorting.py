n=len(arr)
for i in range(1,n): ##for the unsorted forwarding loop
  temp= arr[i]
  j=i-1
  # for the sorted backward loop
  while j>=0 and temp < arr[j] :
    arr[j+1]=arr[j] #right shifting
    j-=1
  arr[j+1]= temp
  return arr
