class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # Duyệt danh sách từ phần tử cuối đến phần tử đầu
        for i in range(len(digits) - 1, -1, -1):
            # Nếu chữ số hiện tại là 9, gán nó thành 0
            if digits[i] == 9:
                digits[i] = 0
            else:
                # Nếu chữ số hiện tại không phải là 9, tăng nó lên 1 và trả về danh sách
                digits[i] = digits[i] + 1
                return digits
        
        # Nếu tất cả các chữ số đều là 9, thêm 1 vào đầu danh sách
        return [1] + digits

def main():
    solution = Solution()

    # Test 1: Chuỗi có số không chứa 9
    digits = [1, 2, 3]
    print(f"Test 1 - Input: digits = {digits}")
    result = solution.plusOne(digits)
    print(f"Output: {result}\n")  # Expected Output: [1, 2, 4]

    # Test 2: Chuỗi có số kết thúc bằng 9
    digits = [1, 2, 9]
    print(f"Test 2 - Input: digits = {digits}")
    result = solution.plusOne(digits)
    print(f"Output: {result}\n")  # Expected Output: [1, 3, 0]

    # Test 3: Chuỗi chỉ chứa 9
    digits = [9, 9, 9]
    print(f"Test 3 - Input: digits = {digits}")
    result = solution.plusOne(digits)
    print(f"Output: {result}\n")  # Expected Output: [1, 0, 0, 0]

    # Test 4: Chuỗi chứa số không phải 9
    digits = [0]
    print(f"Test 4 - Input: digits = {digits}")
    result = solution.plusOne(digits)
    print(f"Output: {result}\n")  # Expected Output: [1]

    # Test 5: Chuỗi chứa số lớn hơn 9
    digits = [4, 5, 6]
    print(f"Test 5 - Input: digits = {digits}")
    result = solution.plusOne(digits)
    print(f"Output: {result}\n")  # Expected Output: [4, 5, 7]

if __name__ == "__main__":
    main()  # Gọi hàm main để chạy các test
