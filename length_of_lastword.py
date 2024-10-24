class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0  # Khởi tạo biến length để đếm số ký tự của từ cuối cùng
        i = len(s) - 1  # Bắt đầu từ chỉ số cuối cùng của chuỗi s

        # Bỏ qua các khoảng trắng ở cuối chuỗi
        while i >= 0 and s[i] == ' ':
            i -= 1  # Giảm chỉ số i để kiểm tra ký tự trước đó

        # Đếm số ký tự của từ cuối cùng
        while i >= 0 and s[i] != ' ':
            length += 1  # Tăng biến length cho mỗi ký tự không phải khoảng trắng
            i -= 1  # Giảm chỉ số i để kiểm tra ký tự trước đó

        return length  # Trả về độ dài của từ cuối cùng

def main():
    solution = Solution()

    # Test 1: Chuỗi có nhiều từ
    s = "Hello World"
    print(f"Test 1 - Input: s = '{s}'")
    result = solution.lengthOfLastWord(s)
    print(f"Output: {result}\n")  # Expected Output: 5 (từ "World")

    # Test 2: Chuỗi chỉ có một từ
    s = "Python"
    print(f"Test 2 - Input: s = '{s}'")
    result = solution.lengthOfLastWord(s)
    print(f"Output: {result}\n")  # Expected Output: 6 (từ "Python")

    # Test 3: Chuỗi có khoảng trắng ở đầu và cuối
    s = "   Hello   "
    print(f"Test 3 - Input: s = '{s}'")
    result = solution.lengthOfLastWord(s)
    print(f"Output: {result}\n")  # Expected Output: 5 (từ "Hello")

    # Test 4: Chuỗi có nhiều khoảng trắng giữa các từ
    s = "   Fly me   to   the moon  "
    print(f"Test 4 - Input: s = '{s}'")
    result = solution.lengthOfLastWord(s)
    print(f"Output: {result}\n")  # Expected Output: 4 (từ "moon")

    # Test 5: Chuỗi rỗng
    s = ""
    print(f"Test 5 - Input: s = '{s}'")
    result = solution.lengthOfLastWord(s)
    print(f"Output: {result}\n")  # Expected Output: 0 (không có từ nào)

if __name__ == "__main__":
    main()  # Gọi hàm main để chạy các test
