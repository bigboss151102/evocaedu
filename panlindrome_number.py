class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:  # Số âm không thể là số Palindrome
            return False

        reversed_num = 0  # Biến để lưu trữ số đã đảo ngược
        temp = x  # Sao chép giá trị của x để thực hiện việc đảo ngược

        # Đảo ngược số x
        while temp != 0:
            digit = temp % 10  # Lấy chữ số cuối của temp
            reversed_num = reversed_num * 10 + digit  # Thêm chữ số vào số đảo ngược
            temp //= 10  # Loại bỏ chữ số cuối cùng

        # Kiểm tra xem số đảo ngược có bằng với số gốc không
        return reversed_num == x

def main():
    solution = Solution()
    
    # Test 1: Số Palindrome dương
    x = 121
    result = solution.isPalindrome(x)
    print(f"Test 1 - Input: x = {x}")
    print(f"Output: {result}\n")  # Expected Output: True

    # Test 2: Số không phải là Palindrome
    x = -121
    result = solution.isPalindrome(x)
    print(f"Test 2 - Input: x = {x}")
    print(f"Output: {result}\n")  # Expected Output: False

    # Test 3: Số có giá trị âm
    x = 10
    result = solution.isPalindrome(x)
    print(f"Test 3 - Input: x = {x}")
    print(f"Output: {result}\n")  # Expected Output: False

    # Test 4: Số Palindrome lớn
    x = 12321
    result = solution.isPalindrome(x)
    print(f"Test 4 - Input: x = {x}")
    print(f"Output: {result}\n")  # Expected Output: True

if __name__ == "__main__":
    main()
