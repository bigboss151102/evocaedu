class Solution(object):
    def isValid(self, s):
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if not stack or \
                    (c == ')' and stack[-1] != '(') or \
                    (c == '}' and stack[-1] != '{') or \
                    (c == ']' and stack[-1] != '['):
                    return False
                stack.pop()
        return not stack

def main():
    solution = Solution()
    
    # Test 1: Chuỗi hợp lệ với ngoặc tròn
    s = "()"
    result = solution.isValid(s)
    print(f"Test 1 - Input: s = '{s}'")
    print(f"Output: {result}\n")  # Expected Output: True

    # Test 2: Chuỗi hợp lệ với nhiều loại ngoặc
    s = "()[]{}"
    result = solution.isValid(s)
    print(f"Test 2 - Input: s = '{s}'")
    print(f"Output: {result}\n")  # Expected Output: True

    # Test 3: Chuỗi không hợp lệ
    s = "(]"
    result = solution.isValid(s)
    print(f"Test 3 - Input: s = '{s}'")
    print(f"Output: {result}\n")  # Expected Output: False

    # Test 4: Chuỗi phức tạp
    s = "([{}])"
    result = solution.isValid(s)
    print(f"Test 4 - Input: s = '{s}'")
    print(f"Output: {result}\n")  # Expected Output: True

    # Test 5: Chuỗi không cân bằng
    s = "([)]"
    result = solution.isValid(s)
    print(f"Test 5 - Input: s = '{s}'")
    print(f"Output: {result}\n")  # Expected Output: False

if __name__ == "__main__":
    main()
