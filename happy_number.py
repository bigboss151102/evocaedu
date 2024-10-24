class Solution:
    def isHappy(self, n: int) -> bool:
        # Hàm giúp tính tổng bình phương các chữ số của số n
        def get_next(n):
            return sum(int(digit) ** 2 for digit in str(n))
        
        seen = set()  # Tập hợp để lưu các số đã thấy
        # Tiếp tục cho đến khi n trở thành 1 hoặc đã thấy số này trước đó
        while n != 1 and n not in seen:
            seen.add(n)  # Thêm số hiện tại vào tập hợp
            n = get_next(n)  # Cập nhật n thành tổng bình phương các chữ số

        return n == 1  # Nếu n bằng 1, trả về True (n hạnh phúc), ngược lại trả về False

def main():
    solution = Solution()

    # Test 1: Kiểm tra với số hạnh phúc
    n = 19  # 1^2 + 9^2 = 82 -> 8^2 + 2^2 = 68 -> 6^2 + 8^2 = 100 -> 1^2 + 0^2 + 0^2 = 1
    print(f"Test 1 - Input: {n}")
    print(f"Output: {solution.isHappy(n)}\n")  # Expected Output: True

    # Test 2: Kiểm tra với số không hạnh phúc
    n = 2  # 2 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4 (bắt đầu lặp lại)
    print(f"Test 2 - Input: {n}")
    print(f"Output: {solution.isHappy(n)}\n")  # Expected Output: False

    # Test 3: Kiểm tra với số 1
    n = 1  # 1 đã là số hạnh phúc
    print(f"Test 3 - Input: {n}")
    print(f"Output: {solution.isHappy(n)}\n")  # Expected Output: True

    # Test 4: Kiểm tra với số 7
    n = 7  # 7 -> 49 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4 (bắt đầu lặp lại)
    print(f"Test 4 - Input: {n}")
    print(f"Output: {solution.isHappy(n)}\n")  # Expected Output: True

    # Test 5: Kiểm tra với số 0
    n = 0  # 0 -> 0 (không bao giờ trở thành 1)
    print(f"Test 5 - Input: {n}")
    print(f"Output: {solution.isHappy(n)}\n")  # Expected Output: False

if __name__ == "__main__":
    main()  # Gọi hàm main để chạy các test
