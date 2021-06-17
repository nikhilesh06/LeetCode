class Solution:
    #Initialising counters for local and global inversions
    counterlocal=counterglobal=0
    def isIdealPermutation(self, nums: List[int]) -> bool:

        #LOCAL INVERSION
        #Time Complexity for calculating local inversion will be O(n)
        for i in range(len(nums)-1):
            if(nums[i]>nums[i+1]):
                self.counterlocal+=1                
        
        #GLOBAL INVERSION
        #Calculating global inversion by leveraging on merge sort
        #Time Complexity for local inversion will be O(nlogn)
        def mergeSort(nums):   
            if len(nums)>1:
                mid=len(nums)//2
                l = nums[:mid]
                r= nums[mid:]
                mergeSort(l)
                mergeSort(r)
                
                i=j=k=0

                
                while(i<len(l) and j<len(r)):
                    if (l[i]<r[j]):
                        nums[k]=l[i]
                        i+=1
                    else:
                        nums[k]=r[j]
                        j+=1
                        #Counting the inversion wherever the left array element is greater than right array element
                        #Counting will also include all the elements in the left sorted array (after the element being compared)
                        self.counterglobal+= len(l)-i
                    k+=1
                while (i<len(l)):
                        nums[k]=l[i]
                        i+=1
                        k+=1
                while (j<len(r)):
                        nums[k]=r[j]
                        j+=1
                        k+=1        
        mergeSort(nums)
        
        return self.counterglobal==self.counterlocal
        