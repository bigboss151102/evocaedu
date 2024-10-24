from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Khởi tạo từ điển để lưu vị trí các phần tử đã xuất hiện trong mảng
        d = {}

        # Duyệt qua từng phần tử trong mảng cùng với chỉ số của nó
        for i, n in enumerate(nums):
            # Kiểm tra nếu phần tử đã xuất hiện trước đó và khoảng cách giữa hai chỉ số <= k
            if n in d and abs(i - d[n]) <= k:
                return True  # Nếu thỏa mãn điều kiện, trả về True
            else:
                # Nếu không thỏa điều kiện, cập nhật vị trí mới của phần tử trong từ điển
                d[n] = i
        
        # Nếu không tìm thấy phần tử nào thỏa điều kiện, trả về False
        return False

def main():
    solution = Solution()
    
    # Test 1: Có phần tử trùng lặp trong khoảng cách <= k
    nums = [1, 2, 3, 1]
    k = 3
    print(f"Test 1 - Input: {nums}, k={k}")
    print(f"Output: {solution.containsNearbyDuplicate(nums, k)}\n")  # Expected Output: True
    
    # Test 2: Không có phần tử trùng lặp trong khoảng cách <= k
    nums = [1, 2, 3, 4]
    k = 2
    print(f"Test 2 - Input: {nums}, k={k}")
    print(f"Output: {solution.containsNearbyDuplicate(nums, k)}\n")  # Expected Output: False
    
    # Test 3: Phần tử trùng lặp nhưng khoảng cách lớn hơn k
    nums = [1, 0, 1, 1]
    k = 1
    print(f"Test 3 - Input: {nums}, k={k}")
    print(f"Output: {solution.containsNearbyDuplicate(nums, k)}\n")  # Expected Output: True
    
    # Test 4: Tất cả các phần tử là duy nhất
    nums = [1, 2, 3, 4, 5]
    k = 3
    print(f"Test 4 - Input: {nums}, k={k}")
    print(f"Output: {solution.containsNearbyDuplicate(nums, k)}\n")  # Expected Output: False
    
    # Test 5: Kiểm tra với mảng chỉ có 1 phần tử
    nums = [1]
    k = 1
    print(f"Test 5 - Input: {nums}, k={k}")
    print(f"Output: {solution.containsNearbyDuplicate(nums, k)}\n")  # Expected Output: False

if __name__ == "__main__":
    main()  # Gọi hàm main để chạy các test
