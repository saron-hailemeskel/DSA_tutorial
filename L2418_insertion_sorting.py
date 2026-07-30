class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n= len(heights)
        for i in range(1,n):
            temp1=heights[i]
            temp2= names[i]

            j=i-1
            while j>=0 and temp1 >heights[j] :
                heights[j+1]=heights[j]
                names[j+1]=names[j]
                j-=1
            heights[j+1]= temp1
            names[j+1]=temp2
        return names

            
        
