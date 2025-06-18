def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Find two numbers in the array that add up to the target sum.
    
    Args:
        nums: List of integers
        target: Target sum to find
    
    Returns:
        List containing indices of the two numbers that add up to the target
    """
    # Create a hash map to store number:index pairs
    num_map = {}
    
    # Iterate through the array
    for i, num in enumerate(nums):
        # Calculate the complement needed to reach target
        complement = target - num
        
        # If complement exists in hash map, we found our pair
        if complement in num_map:
            return [num_map[complement], i]
            
        # Add current number and its index to hash map
        num_map[num] = i
    
    # If no solution is found
    return []

# Example usage
if __name__ == "__main__":
    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = two_sum(nums1, target1)
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {result1}")  # Should print [0, 1]
    
    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = two_sum(nums2, target2)
    print(f"\nInput: nums = {nums2}, target = {target2}")
    print(f"Output: {result2}")  # Should print [1, 2]

