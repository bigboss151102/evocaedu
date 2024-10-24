class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0  # Khởi tạo biến left để xác định giới hạn dưới
        right = x  # Khởi tạo biến right để xác định giới hạn trên
        
        # Duyệt trong khoảng từ left đến right
        while left <= right:
            mid = (left + right) // 2  # Tính giá trị trung bình của left và right
            
            # Kiểm tra nếu mid bình phương nhỏ hơn x
            if mid * mid < x:
                left = mid + 1  # Nếu nhỏ hơn, thì tăng left để tìm giá trị lớn hơn
            # Kiểm tra nếu mid bình phương lớn hơn x
            elif mid * mid > x:
                right = mid - 1  # Nếu lớn hơn, thì giảm right để tìm giá trị nhỏ hơn
            else:
                return mid  # Nếu mid bình phương bằng x, trả về mid
            
        return right  # Nếu không tìm thấy, trả về right, là giá trị căn bậc hai lớn nhất của x

def main():
    solution = Solution()

    # Test 1: Số nhỏ hơn 4
    x = 8
    print(f"Test 1 - Input: x = {x}")
    result = solution.mySqrt(x)
    print(f"Output: {result}\n")  # Expected Output: 2

    # Test 2: Số bằng 4
    x = 4
    print(f"Test 2 - Input: x = {x}")
    result = solution.mySqrt(x)
    print(f"Output: {result}\n")  # Expected Output: 2

    # Test 3: Số lớn hơn 4
    x = 16
    print(f"Test 3 - Input: x = {x}")
    result = solution.mySqrt(x)
    print(f"Output: {result}\n")  # Expected Output: 4

    # Test 4: Số bằng 0
    x = 0
    print(f"Test 4 - Input: x = {x}")
    result = solution.mySqrt(x)
    print(f"Output: {result}\n")  # Expected Output: 0

    # Test 5: Số bằng 1
    x = 1
    print(f"Test 5 - Input: x = {x}")
    result = solution.mySqrt(x)
    print(f"Output: {result}\n")  # Expected Output: 1

if __name__ == "__main__":
    main()  # Gọi hàm main để chạy các test
