class Solution:
    def subarray_target_sum_size_k(self, arr: List[int], k: int, target: int) -> int:
      curr_sum= sum(arr[:k])
      #curr_sum=0
      #for i in range(k):
      #  curr_sum+= arr[i]
      count= 0
      if curr_sum==target:
          count+=1
      for i in range(1,len(arr)-k+1):
        curr_sum-= arr[i-1]
        curr_sum+= arr[i+k-1]
        if curr_sum==target:
          count+=1
      return count
