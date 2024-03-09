# Thư viện này dùng để send request tới đường dẫn: https://sjc.com.vn/giavang/textContent.php
import requests
# Thư viện này dùng để parse HTML sang một cấu trúc dữ liệu có thể quản lý được trong Python
from bs4 import BeautifulSoup

# Send request tới đường dẫn: https://sjc.com.vn/giavang/textContent.php
page_url = "https://sjc.com.vn/giavang/textContent.php"
page = requests.get(page_url)

# Parse HTML sang một cấu trúc dữ liệu có thể quản lý được trong Python
beautifulSoup = BeautifulSoup(page.content, 'html.parser')

# Lấy thời gian cập nhật giá vàng
updated_date = beautifulSoup.find_all(class_ ="w350 m5l float_left red_text bg_white")[0].text

# Trích xuất thẻ <tr> của loại "VÀNG NHẪN SJC 99,99 1 CHỈ, 2 CHỈ, 5 CHỈ"
row = beautifulSoup.table.find_all("tr", limit = 5)[4]

# Lấy tên loại vàng
species = row.find_all("td")[0].text

# Lấy giá mua
raw_buy_into = row.find_all("td")[1].text
buy_into = raw_buy_into.replace(',', '.') + ' VNĐ'

# Lấy giá bán
raw_sold_out = row.find_all("td")[2].text
sold_out = raw_sold_out.replace(',', '.') + ' VNĐ'

# In ra màn hình
print(f'CẬP NHẬT LÚC: {updated_date}')
print(f'GIÁ VÀNG "{species}"')
print(f'GIÁ MUA: {buy_into}')
print(f'GIÁ BÁN: {sold_out}')
