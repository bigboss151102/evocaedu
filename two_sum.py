from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}  # Dictionary để lưu trữ giá trị của số và vị trí (index) của nó
        n = len(nums)  # Số lượng phần tử trong mảng nums

        for i in range(n):  # Lặp qua từng phần tử của mảng
            complement = target - nums[i]  # Tìm phần bù (complement) của giá trị hiện tại
            if complement in numMap:  # Nếu phần bù đã có trong numMap (nghĩa là đã có một cặp phù hợp)
                return [numMap[complement], i]  # Trả về vị trí của phần bù và vị trí hiện tại
            numMap[nums[i]] = i  # Thêm giá trị hiện tại và vị trí của nó vào dictionary

        return []  # Trả về mảng rỗng nếu không tìm thấy giải pháp

def main():
    solution = Solution()
    
    # Test 1
    nums = [2, 7, 11, 15]
    target = 9
    result = solution.twoSum(nums, target)
    print(f"Test 1 - Input: nums = {nums}, target = {target}")
    print(f"Output: {result}\n")  # Expected Output: [0, 1]

    # Test 2
    nums = [3, 2, 4]
    target = 6
    result = solution.twoSum(nums, target)
    print(f"Test 2 - Input: nums = {nums}, target = {target}")
    print(f"Output: {result}\n")  # Expected Output: [1, 2]

    # Test 3
    nums = [3, 3]
    target = 6
    result = solution.twoSum(nums, target)
    print(f"Test 3 - Input: nums = {nums}, target = {target}")
    print(f"Output: {result}\n")  # Expected Output: [0, 1]

if __name__ == "__main__":
    main()
