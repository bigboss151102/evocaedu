class Solution:
    def toLowerCase(self, s: str) -> str:
        # Khởi tạo chuỗi rỗng để lưu các ký tự sau khi chuyển thành chữ thường
        lower_case_str = ""
        
        # Duyệt qua từng ký tự trong chuỗi đầu vào
        for char in s:
            # Lấy giá trị ASCII của ký tự
            ascii_val = ord(char)
            
            # Nếu ký tự là chữ hoa (A-Z trong bảng ASCII), chuyển nó thành chữ thường
            if 65 <= ascii_val <= 90:  # A-Z trong bảng mã ASCII
                lower_case_str += chr(ascii_val + 32)  # Chuyển thành chữ thường bằng cách cộng thêm 32
            else:
                # Nếu không phải là chữ hoa, giữ nguyên ký tự
                lower_case_str += char
        
        # Trả về chuỗi đã chuyển thành chữ thường
        return lower_case_str

def main():
    solution = Solution()
    
    # Test 1: Kiểm tra với chuỗi có cả chữ hoa và chữ thường
    s = "HelloWorld"
    print(f"Test 1 - Input: {s}")
    print(f"Output: {solution.toLowerCase(s)}\n")  # Expected Output: "helloworld"
    
    # Test 2: Kiểm tra với chuỗi chỉ có chữ hoa
    s = "PYTHON"
    print(f"Test 2 - Input: {s}")
    print(f"Output: {solution.toLowerCase(s)}\n")  # Expected Output: "python"
    
    # Test 3: Kiểm tra với chuỗi chỉ có chữ thường
    s = "java"
    print(f"Test 3 - Input: {s}")
    print(f"Output: {solution.toLowerCase(s)}\n")  # Expected Output: "java"
    
    # Test 4: Kiểm tra với chuỗi chứa cả chữ, số và ký tự đặc biệt
    s = "C++123@HELLO"
    print(f"Test 4 - Input: {s}")
    print(f"Output: {solution.toLowerCase(s)}\n")  # Expected Output: "c++123@hello"
    
    # Test 5: Kiểm tra với chuỗi rỗng
    s = ""
    print(f"Test 5 - Input: {s}")
    print(f"Output: {solution.toLowerCase(s)}\n")  # Expected Output: ""

if __name__ == "__main__":
    main()  # Gọi hàm main để chạy các test
