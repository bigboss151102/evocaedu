def decimalNumber(s):
    i = 0
    sum = 0
    # Duyệt chuỗi từ phải sang trái (như cách tính nhị phân)
    for x in range(len(s) - 1, -1, -1):
        # Chuyển đổi vị trí số nhị phân sang giá trị thập phân
        twoNumber = 1 << i  # 1<<i nghĩa là 2^i (dùng phép dịch bit)
        sum += twoNumber * int(s[x])  # Nhân giá trị nhị phân tại vị trí với 2^i
        i += 1
    return sum

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Nếu cả a và b đều là "0", trả về "0"
        if a == "0" and b == "0":
            return a

        # Chuyển đổi cả hai chuỗi nhị phân thành số thập phân, sau đó cộng lại
        result = decimalNumber(a) + decimalNumber(b)
        s = ""
        # Chuyển đổi từ số thập phân sang chuỗi nhị phân
        while result > 0:
            s += str(result % 2)  # Lấy phần dư của phép chia cho 2 (0 hoặc 1)
            result = result // 2  # Chia số thập phân cho 2 để tiếp tục tính
        return s[::-1]  # Đảo ngược chuỗi để có kết quả đúng

# Hàm main để thực thi chương trình
def main():
    # Ví dụ chuỗi nhị phân để kiểm tra
    a = "1010"
    b = "1011"
    
    # Tạo đối tượng của class Solution
    solution = Solution()
    
    # Gọi hàm addBinary để cộng hai chuỗi nhị phân
    result = solution.addBinary(a, b)
    
    # In ra kết quả
    print(f"Kết quả của phép cộng nhị phân giữa {a} và {b} là: {result}")

# Gọi hàm main
if __name__ == "__main__":
    main()