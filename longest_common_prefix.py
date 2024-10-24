from typing import List

class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        ans = ""  # Chuỗi kết quả để lưu tiền tố chung dài nhất
        v = sorted(v)  # Sắp xếp danh sách các chuỗi

        first = v[0]  # Chuỗi đầu tiên sau khi sắp xếp
        last = v[-1]  # Chuỗi cuối cùng sau khi sắp xếp

        # So sánh từng ký tự của chuỗi đầu tiên và chuỗi cuối cùng
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:  # Nếu ký tự khác nhau, trả về kết quả hiện tại
                return ans
            ans += first[i]  # Thêm ký tự chung vào chuỗi kết quả

        return ans  # Trả về tiền tố chung dài nhất

def main():
    solution = Solution()
    
    # Test 1: Chuỗi có tiền tố chung đơn giản
    v = ["flower", "flow", "flight"]
    result = solution.longestCommonPrefix(v)
    print(f"Test 1 - Input: v = {v}")
    print(f"Output: '{result}'\n")  # Expected Output: "fl"

    # Test 2: Không có tiền tố chung
    v = ["dog", "racecar", "car"]
    result = solution.longestCommonPrefix(v)
    print(f"Test 2 - Input: v = {v}")
    print(f"Output: '{result}'\n")  # Expected Output: ""

    # Test 3: Các chuỗi giống nhau
    v = ["interstellar", "interstate", "internet"]
    result = solution.longestCommonPrefix(v)
    print(f"Test 3 - Input: v = {v}")
    print(f"Output: '{result}'\n")  # Expected Output: "inter"

    # Test 4: Chuỗi rỗng
    v = []
    result = solution.longestCommonPrefix(v)
    print(f"Test 4 - Input: v = {v}")
    print(f"Output: '{result}'\n")  # Expected Output: ""

    # Test 5: Chỉ có một chuỗi
    v = ["single"]
    result = solution.longestCommonPrefix(v)
    print(f"Test 5 - Input: v = {v}")
    print(f"Output: '{result}'\n")  # Expected Output: "single"

if __name__ == "__main__":
    main()
