class Solution:
    def maxProfit(self, prices):
        # Khởi tạo giá mua ban đầu là giá đầu tiên trong danh sách
        buy = prices[0]
        # Khởi tạo lợi nhuận tối đa ban đầu là 0
        profit = 0
        
        # Duyệt qua từng giá trong danh sách bắt đầu từ chỉ số 1
        for i in range(1, len(prices)):
            # Nếu giá hiện tại thấp hơn giá mua đã lưu
            if prices[i] < buy:
                # Cập nhật giá mua mới
                buy = prices[i]
            # Nếu lợi nhuận từ việc bán hiện tại lớn hơn lợi nhuận tối đa đã lưu
            elif prices[i] - buy > profit:
                # Cập nhật lợi nhuận tối đa
                profit = prices[i] - buy
        
        return profit  # Trả về lợi nhuận tối đa

def main():
    solution = Solution()

    # Test 1: Trường hợp bình thường
    prices = [7, 1, 5, 3, 6, 4]  # Giá cổ phiếu trong các ngày
    print(f"Test 1 - Input: {prices}")
    print(f"Output: {solution.maxProfit(prices)}\n")  # Expected Output: 5

    # Test 2: Trường hợp không có lợi nhuận
    prices = [7, 6, 4, 3, 1]  # Không thể tạo lợi nhuận
    print(f"Test 2 - Input: {prices}")
    print(f"Output: {solution.maxProfit(prices)}\n")  # Expected Output: 0

    # Test 3: Trường hợp có lợi nhuận ngay từ đầu
    prices = [1, 2, 3, 4, 5]  # Lợi nhuận tối đa là 4
    print(f"Test 3 - Input: {prices}")
    print(f"Output: {solution.maxProfit(prices)}\n")  # Expected Output: 4

    # Test 4: Trường hợp giá cổ phiếu không thay đổi
    prices = [5, 5, 5, 5]  # Không thể tạo lợi nhuận
    print(f"Test 4 - Input: {prices}")
    print(f"Output: {solution.maxProfit(prices)}\n")  # Expected Output: 0

    # Test 5: Trường hợp có nhiều thay đổi giá
    prices = [3, 2, 6, 5, 0, 3]  # Lợi nhuận tối đa là 4
    print(f"Test 5 - Input: {prices}")
    print(f"Output: {solution.maxProfit(prices)}\n")  # Expected Output: 4

if __name__ == "__main__":
    main()  # Gọi hàm main để chạy các test
