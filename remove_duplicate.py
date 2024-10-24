from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j

def main():
    solution = Solution()
    
    # Test 1: Mảng chứa các số lặp lại
    nums = [1, 1, 2]
    print(f"Test 1 - Input: nums = {nums}")
    length = solution.removeDuplicates(nums)
    print(f"Output Length: {length}")
    print(f"Modified Array: {nums[:length]}\n")  # Expected Output: [1, 2]

    # Test 2: Mảng với các số liên tiếp không lặp lại
    nums = [0, 1, 2, 3, 4, 5]
    print(f"Test 2 - Input: nums = {nums}")
    length = solution.removeDuplicates(nums)
    print(f"Output Length: {length}")
    print(f"Modified Array: {nums[:length]}\n")  # Expected Output: [0, 1, 2, 3, 4, 5]

    # Test 3: Mảng với tất cả phần tử giống nhau
    nums = [2, 2, 2, 2]
    print(f"Test 3 - Input: nums = {nums}")
    length = solution.removeDuplicates(nums)
    print(f"Output Length: {length}")
    print(f"Modified Array: {nums[:length]}\n")  # Expected Output: [2]

    # Test 4: Mảng rỗng
    nums = []
    print(f"Test 4 - Input: nums = {nums}")
    length = solution.removeDuplicates(nums)
    print(f"Output Length: {length}")
    print(f"Modified Array: {nums[:length]}\n")  # Expected Output: []

    # Test 5: Mảng với 1 phần tử
    nums = [5]
    print(f"Test 5 - Input: nums = {nums}")
    length = solution.removeDuplicates(nums)
    print(f"Output Length: {length}")
    print(f"Modified Array: {nums[:length]}\n")  # Expected Output: [5]

if __name__ == "__main__":
    main()
