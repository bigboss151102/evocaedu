class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # Chép các phần tử từ nums2 vào nums1 bắt đầu từ vị trí m
        for j in range(n):
            nums1[m + j] = nums2[j]
        
        # Sắp xếp nums1 để đảm bảo các phần tử được hợp nhất đúng thứ tự
        nums1.sort()

def main():
    solution = Solution()

    # Test 1: Trường hợp bình thường
    nums1 = [1, 2, 3, 0, 0, 0]  # Danh sách đầu vào chứa các phần tử đã sắp xếp và không gian trống
    m = 3  # Số lượng phần tử đã sắp xếp trong nums1
    nums2 = [2, 5, 6]  # Danh sách nums2 cần hợp nhất
    n = 3  # Số lượng phần tử trong nums2
    solution.merge(nums1, m, nums2, n)
    print(f"Test 1 - Input: nums1 = {nums1}, nums2 = {nums2}")
    print(f"Output: {nums1}\n")  # Expected Output: [1, 2, 2, 3, 5, 6]

    # Test 2: Trường hợp nums2 rỗng
    nums1 = [1]  # Danh sách chỉ chứa một phần tử
    m = 1
    nums2 = []  # Danh sách nums2 rỗng
    n = 0
    solution.merge(nums1, m, nums2, n)
    print(f"Test 2 - Input: nums1 = {nums1}, nums2 = {nums2}")
    print(f"Output: {nums1}\n")  # Expected Output: [1]

    # Test 3: Trường hợp nums1 rỗng
    nums1 = [0] * 3  # Danh sách nums1 chỉ chứa không gian trống
    m = 0
    nums2 = [1, 2, 3]  # Danh sách nums2 chứa các phần tử
    n = 3
    solution.merge(nums1, m, nums2, n)
    print(f"Test 3 - Input: nums1 = {nums1}, nums2 = {nums2}")
    print(f"Output: {nums1}\n")  # Expected Output: [1, 2, 3]

    # Test 4: Trường hợp nums1 đã chứa tất cả các phần tử của nums2
    nums1 = [1, 2, 3, 4, 5]  # Danh sách đã sắp xếp
    m = 5
    nums2 = []  # Danh sách nums2 rỗng
    n = 0
    solution.merge(nums1, m, nums2, n)
    print(f"Test 4 - Input: nums1 = {nums1}, nums2 = {nums2}")
    print(f"Output: {nums1}\n")  # Expected Output: [1, 2, 3, 4, 5]

    # Test 5: Trường hợp có các số trùng lặp
    nums1 = [1, 2, 3, 0, 0, 0]  
    m = 3
    nums2 = [2, 3, 4]  
    n = 3
    solution.merge(nums1, m, nums2, n)
    print(f"Test 5 - Input: nums1 = {nums1}, nums2 = {nums2}")
    print(f"Output: {nums1}\n")  # Expected Output: [1, 2, 2, 3, 3, 4]

if __name__ == "__main__":
    main()  # Gọi hàm main để chạy các test
