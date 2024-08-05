#https://leetcode.com/problems/remove-element/
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Initialize the pointer for the position of the next non-val element
        k = 0

        # Iterate through each element in nums
        for i in range(len(nums)):
            if nums[i] != val:
                # If the element is not equal to val, place it at index k
                nums[k] = nums[i]
                # Increment k to point to the next position for the non-val element
                k += 1

        # Return the length of the array without val elements
        return k

        
