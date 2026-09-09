text = "Python 123 Programming 456 "

dem_khoang_trang = 0

for char in text:
    if char.isspace():
        dem_khoang_trang += 1

print("So luuong khoang trang la: ", dem_khoang_trang)