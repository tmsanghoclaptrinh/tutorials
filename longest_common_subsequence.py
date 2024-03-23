# TÌM ĐỘ DÀI CHUỖI CON CHUNG DÀI NHẤT - THI HSG LỚP 11 CẤP TRƯỜNG - THPT NGỌC TẢO

# Ý TƯỞNG: ÁP DỤNG QUY HOẠCH ĐỘNG
"""
Bước 1: Xác định bài toán con:
- Lặp qua từng ký tự của s1 và s2 để so sánh 
- Xác định độ dài chuỗi con chung dài nhất tại mỗi vị trí

Bước 2: Xác định bài toán cơ sở:
- Nếu ký tự tại vị trí i của s1 và ký tự tại vị trí j của s2 giống nhau
-> Cập nhật độ dài của chuỗi con chung dài nhất tại vị trí i và j

Bước 3: Xác định đáp án bài toán:
- Trả về chuỗi con chung dài nhất

Bước 4: Xác định công thức truy hồi:
- L[i][j] = L[i - 1][j - 1] + 1
- Nghĩa là: Cập nhật độ dài chuỗi con chung tại vị trí [i][j] dựa trên các độ dài chuỗi con chung từ các vị trí trước đó [i-1][j-1]
"""

# Giả dụ fix cứng 2 chuỗi đầu vào s1 và s2 để kiểm tra kết quả cho nhanh
s1 = 'ACGTACGT'
s2 = 'TGACGTAC'

# Độ dài chuỗi con chung dài nhất, ban đầu có giá trị là 0
longest = 0

# Vị trí kết thúc chuỗi con chung dài nhất trong chuỗi s1
end = 0

"""
Tạo mảng 2 chiều (hình dung là 1 cái bảng có các hàng các cột cho dễ)
Dùng để lưu trữ độ dài của chuỗi con chung dài nhất tại mỗi vị trí của các chuỗi
Mặc định ban đầu khởi tạo tất cả các phần tử trong bảng có giá trị là 0
Bảng này có kích thước (số hàng x số cột), tức là (rows x columns) hoặc (len(s1) + 1) x (len(s2) + 1)
Lý do phải cộng thêm 1 vào độ dài 2 chuỗi là vì tý nữa ở phần công thức truy hồi
sẽ phải tính L[i][j] = L[i - 1][j - 1] + 1
Nên những trường hợp như L[1][1] = L[0][0] + 1
thì phải biết được L[0][0] có giá trị là mấy (thực ra L[0][0] sẽ luôn là 0 thôi)
Thực ra có 2 cách viết ngắn gọn hơn cho đoạn code này:
- Cách 1: L = [[0 for i in range(columns)] for j in range(rows)]
- Cách 2: L = [[0] * columns] * rows
"""
L = []
rows, columns = len(s1) + 1, len(s2) + 1
for i in range(rows):
    col = []
    for j in range(columns):
        col.append(0)
    L.append(col)

# Duyệt qua từng ký tự trong s1 và s2 để so sánh và cập nhật ma trận L
for i in range(1, rows):
    for j in range(1, columns):
        # Nếu ký tự tại vị trí [i - 1] của s1 và ký tự tại vị trí [j - 1] của s2 GIỐNG NHAU
        if s1[i - 1] == s2[j - 1]:
            # thì tăng giá trị của m[i][j] lên m[i - 1][j - 1] + 1
            # để cập nhật độ dài của chuỗi con chung
            L[i][j] = L[i - 1][j - 1] + 1

            # Nếu độ dài của chuỗi con chung vượt qua giá trị longest
            # thì cập nhật longest = L[i][j]
            # và end = i để lưu vị trí kết thúc chuỗi con chung dài nhất
            if L[i][j] > longest:
                longest = L[i][j]
                end = i

        # Còn nếu ký tự tại vị trí [i - 1] của s1 và ký tự tại vị trí [j - 1] của s2 KHÁC NHAU
        else:
            # thì gán giá trị L[i][j] = 0
            L[i][j] = 0

# In ra chuỗi con chung dài nhất
print(s1[end - longest:end])
