from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Tạo một từ điển để lưu vị trí của các phần tử đã thấy
        hset = {}
        
        # Duyệt qua tất cả các phần tử trong danh sách
        for idx in range(len(nums)):
            # Nếu phần tử đã tồn tại trong hset và khoảng cách giữa vị trí hiện tại và vị trí đã thấy <= k, trả về True
            if nums[idx] in hset and abs(idx - hset[nums[idx]]) <= k:
                return True
            
            # Cập nhật vị trí của phần tử trong hset
            hset[nums[idx]] = idx
        
        # Nếu không tìm thấy phần tử trùng lặp nào thỏa mãn điều kiện, trả về False
        return False

def main():
    solution = Solution()

    # Test 1: Kiểm tra với một danh sách có phần tử trùng lặp gần nhau
    nums = [1, 2, 3, 1]
    k = 3
    print(f"Test 1 - Input: {nums}, k: {k}")
    print(f"Output: {solution.containsNearbyDuplicate(nums, k)}\n")  # Expected Output: True

    # Test 2: Kiểm tra với một danh sách không có phần tử trùng lặp gần nhau
    nums = [1, 0, 1, 1]
    k = 1
    print(f"Test 2 - Input: {nums}, k: {k}")
    print(f"Output: {solution.containsNearbyDuplicate(nums, k)}\n")  # Expected Output: True

    # Test 3: Kiểm tra với một danh sách không có phần tử trùng lặp
    nums = [1, 2, 3, 4, 5]
    k = 2
    print(f"Test 3 - Input: {nums}, k: {k}")
    print(f"Output: {solution.containsNearbyDuplicate(nums, k)}\n")  # Expected Output: False

    # Test 4: Kiểm tra với danh sách có nhiều trùng lặp
    nums = [1, 2, 3, 1, 2, 3]
    k = 2
    print(f"Test 4 - Input: {nums}, k: {k}")
    print(f"Output: {solution.containsNearbyDuplicate(nums, k)}\n")  # Expected Output: False

    # Test 5: Kiểm tra với danh sách có trùng lặp ngay kế tiếp
    nums = [1, 2, 3, 1, 2, 1]
    k = 2
    print(f"Test 5 - Input: {nums}, k: {k}")
    print(f"Output: {solution.containsNearbyDuplicate(nums, k)}\n")  # Expected Output: True

if __name__ == "__main__":
    main()  # Gọi hàm main để chạy các test
