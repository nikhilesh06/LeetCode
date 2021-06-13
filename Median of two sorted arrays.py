class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #Finding the index of the middle element/median of the combined array
 
        #Assigning the longer and shorter arrays
        #num1 is shorter array and num2 is larger array - if not flip and send the arguments again
        if (len(nums1) > len(nums2)):
            return self.findMedianSortedArrays(nums2,nums1)
        
        med= (len(nums1) + len(nums2)+ 1)//2
        start=0
        end = len(nums1)
         # We traverse the the shorter array using divide and conquer
           
        while(start<=end):           
            shrter_array_partition = (start+end)//2 
            # The partition of the longer array is adjusted relative to the partition of shorter array
            longer_array_partition = med -  shrter_array_partition
            
            #Adding Boundary cases to the shorter and longer array
            if shrter_array_partition==0 : 
                shorter_left = -float('inf') 
            else: 
                shorter_left =  nums1[shrter_array_partition-1]                    
            if shrter_array_partition==len(nums1): 
                shorter_right = float('inf') 
            else: 
                shorter_right =  nums1[shrter_array_partition]                
            if longer_array_partition==0 : 
                longer_left = -float('inf') 
            else: 
                longer_left =  nums2[longer_array_partition-1]                    
            if longer_array_partition==len(nums2): 
                longer_right = float('inf') 
            else: 
                longer_right =  nums2[longer_array_partition]
                

            #If the partition is at the median
            if (shorter_left<=longer_right and longer_left<=shorter_right):
                if (len(nums1) + len(nums2))%2==0:
                    return(float((max(shorter_left,longer_left)+ min(shorter_right,longer_right))/2))      
                else:
                    return (float(max(shorter_left,longer_left)))
                break
            #If the partition is towards the right - then we move to the left i.e the new shorter array will be the left half
            elif (shorter_left>longer_right):                              
                end = shrter_array_partition-1
            #If the parition is towards the left - move to right i.e New shrter arry is righ half
            else:
                start = shrter_array_partition+1