if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    result=[
        [i,j,k]
     for i in range (x+1)
     for j in range(y+1)
     for k in range(z+1)
     if i+j+k!=n
    ]
    print (result)

#list comprehension [expression for loop if condition]
   # using multiple loops 
result =[]
for i in range (x+1):
  for j in range(y+1):
    for k in range(z+1):
       if i+j+k!=n:
         result.append([i,j,k])
  print (result)
      
    
  
    
