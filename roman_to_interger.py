class Solution:
    def romanToInt(self, s: str) -> int:
        # Bảng giá trị của các ký tự La Mã
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        ans = 0  # Kết quả sẽ được lưu vào đây
        
        # Lặp qua từng ký tự trong chuỗi s
        for i in range(len(s)):
            # Nếu ký tự hiện tại có giá trị nhỏ hơn ký tự tiếp theo (trừ)
            if i < len(s) - 1 and m[s[i]] < m[s[i + 1]]:
                ans -= m[s[i]]
            else:
                ans += m[s[i]]  # Ngược lại cộng giá trị vào kết quả
        
        return ans  # Trả về kết quả chuyển đổi số nguyên

def main():
    solution = Solution()
    
    # Test 1: Chuyển đổi đơn giản
    s = "III"
    result = solution.romanToInt(s)
    print(f"Test 1 - Input: s = '{s}'")
    print(f"Output: {result}\n")  # Expected Output: 3

    # Test 2: Chuyển đổi với trường hợp trừ
    s = "IV"
    result = solution.romanToInt(s)
    print(f"Test 2 - Input: s = '{s}'")
    print(f"Output: {result}\n")  # Expected Output: 4

    # Test 3: Chuyển đổi lớn hơn với trường hợp trừ
    s = "IX"
    result = solution.romanToInt(s)
    print(f"Test 3 - Input: s = '{s}'")
    print(f"Output: {result}\n")  # Expected Output: 9

    # Test 4: Chuyển đổi phức tạp hơn
    s = "LVIII"
    result = solution.romanToInt(s)
    print(f"Test 4 - Input: s = '{s}'")
    print(f"Output: {result}\n")  # Expected Output: 58

    # Test 5: Số lớn hơn
    s = "MCMXCIV"
    result = solution.romanToInt(s)
    print(f"Test 5 - Input: s = '{s}'")
    print(f"Output: {result}\n")  # Expected Output: 1994

if __name__ == "__main__":
    main()
