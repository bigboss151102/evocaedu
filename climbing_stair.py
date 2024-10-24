class Solution:
    def climbStairs(self, n: int) -> int:
        # Nếu n là 0 hoặc 1, trả về 1 (có một cách leo lên 0 hoặc 1 bậc)
        if n == 0 or n == 1:
            return 1
        # Công thức đệ quy: tổng số cách leo lên bậc n là tổng số cách leo lên bậc n-1 và n-2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

# Hàm main để thực thi chương trình
def main():
    # Nhập số bậc thang n để kiểm tra
    n = 5
    
    # Tạo đối tượng của class Solution
    solution = Solution()
    
    # Gọi hàm climbStairs để tính số cách leo lên bậc thang
    result = solution.climbStairs(n)
    
    # In ra kết quả
    print(f"Số cách leo lên {n} bậc thang là: {result}")

# Gọi hàm main
if __name__ == "__main__":
    main()