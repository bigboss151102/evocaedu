class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Nếu num là 0, trả về 0
        if num == 0: 
            return 0
        # Nếu num chia hết cho 9, trả về 9 (đây là trường hợp đặc biệt của quy tắc chia 9)
        if num % 9 == 0: 
            return 9
        else:
            # Nếu không chia hết cho 9, trả về phần dư của num khi chia cho 9
            return (num % 9)

def main():
    solution = Solution()
    
    # Test 1: Input là số chia hết cho 9
    num = 18
    print(f"Test 1 - Input: {num}")
    print(f"Output: {solution.addDigits(num)}\n")  # Expected Output: 9
    
    # Test 2: Input là số không chia hết cho 9
    num = 38
    print(f"Test 2 - Input: {num}")
    print(f"Output: {solution.addDigits(num)}\n")  # Expected Output: 2 (38 % 9 = 2)
    
    # Test 3: Input là 0
    num = 0
    print(f"Test 3 - Input: {num}")
    print(f"Output: {solution.addDigits(num)}\n")  # Expected Output: 0
    
    # Test 4: Input là số rất lớn
    num = 987654321
    print(f"Test 4 - Input: {num}")
    print(f"Output: {solution.addDigits(num)}\n")  # Expected Output: 9
    
    # Test 5: Input là số nhỏ
    num = 7
    print(f"Test 5 - Input: {num}")
    print(f"Output: {solution.addDigits(num)}\n")  # Expected Output: 7

if __name__ == "__main__":
    main()  # Gọi hàm main để chạy các test
