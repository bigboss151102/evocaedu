from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index

def main():
    solution = Solution()

    # Test 1: Xóa phần tử xuất hiện nhiều lần
    nums = [3, 2, 2, 3]
    val = 3
    print(f"Test 1 - Input: nums = {nums}, val = {val}")
    length = solution.removeElement(nums, val)
    print(f"Output Length: {length}")
    print(f"Modified Array: {nums[:length]}\n")  # Expected Output: [2, 2]

    # Test 2: Xóa phần tử không xuất hiện
    nums = [0, 1, 2, 3, 4, 5]
    val = 6
    print(f"Test 2 - Input: nums = {nums}, val = {val}")
    length = solution.removeElement(nums, val)
    print(f"Output Length: {length}")
    print(f"Modified Array: {nums[:length]}\n")  # Expected Output: [0, 1, 2, 3, 4, 5]

    # Test 3: Xóa tất cả phần tử
    nums = [1, 1, 1, 1]
    val = 1
    print(f"Test 3 - Input: nums = {nums}, val = {val}")
    length = solution.removeElement(nums, val)
    print(f"Output Length: {length}")
    print(f"Modified Array: {nums[:length]}\n")  # Expected Output: []

    # Test 4: Mảng rỗng
    nums = []
    val = 0
    print(f"Test 4 - Input: nums = {nums}, val = {val}")
    length = solution.removeElement(nums, val)
    print(f"Output Length: {length}")
    print(f"Modified Array: {nums[:length]}\n")  # Expected Output: []

    # Test 5: Mảng có 1 phần tử, phần tử đó cần bị xóa
    nums = [5]
    val = 5
    print(f"Test 5 - Input: nums = {nums}, val = {val}")
    length = solution.removeElement(nums, val)
    print(f"Output Length: {length}")
    print(f"Modified Array: {nums[:length]}\n")  # Expected Output: []

if __name__ == "__main__":
    main()
