class Solution:
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if target <= nums[i]:
                return i
        return len(nums)

def main():
    solution = Solution()

    # Test 1: Target nằm trong mảng
    nums = [1, 3, 5, 6]
    target = 5
    print(f"Test 1 - Input: nums = {nums}, target = {target}")
    result = solution.searchInsert(nums, target)
    print(f"Output: {result}\n")  # Expected Output: 2

    # Test 2: Target nhỏ hơn tất cả các phần tử trong mảng
    nums = [1, 3, 5, 6]
    target = 0
    print(f"Test 2 - Input: nums = {nums}, target = {target}")
    result = solution.searchInsert(nums, target)
    print(f"Output: {result}\n")  # Expected Output: 0

    # Test 3: Target lớn hơn tất cả các phần tử trong mảng
    nums = [1, 3, 5, 6]
    target = 7
    print(f"Test 3 - Input: nums = {nums}, target = {target}")
    result = solution.searchInsert(nums, target)
    print(f"Output: {result}\n")  # Expected Output: 4

    # Test 4: Target nằm giữa các phần tử trong mảng
    nums = [1, 3, 5, 6]
    target = 2
    print(f"Test 4 - Input: nums = {nums}, target = {target}")
    result = solution.searchInsert(nums, target)
    print(f"Output: {result}\n")  # Expected Output: 1

    # Test 5: Mảng rỗng
    nums = []
    target = 1
    print(f"Test 5 - Input: nums = {nums}, target = {target}")
    result = solution.searchInsert(nums, target)
    print(f"Output: {result}\n")  # Expected Output: 0

if __name__ == "__main__":
    main()
