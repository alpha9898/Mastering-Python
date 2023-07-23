class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create an empty dictionary to store elements from 'nums' and their corresponding indices
        num_dict = {}
        
        # Iterate through the 'nums' list using 'enumerate' to access both elements and their indices
        for i, num in enumerate(nums):
            # Calculate the complement, i.e., the value we need to find in 'nums' to achieve the target sum
            complement = target - num
            
            # Check if the complement exists in the 'num_dict'
            if complement in num_dict:
                #! If the complement exists, it means we have found the pair of elements that sum up to the target.
                #! Return the indices of these two elements as a list.
                #! The first index is the value associated with the 'complement' in the dictionary,
                #! and the second index is the current index 'i'.
                return [num_dict[complement], i]
            
            # If the complement is not in the 'num_dict', add the current element 'num' to the dictionary with its index 'i'.
            # This is done to keep track of the indices of the elements as the loop progresses.
            num_dict[num] = i
        
        # If the loop completes without finding a pair that sums up to the target, return an empty list.
        return []
