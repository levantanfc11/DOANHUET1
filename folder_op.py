#Các thư viện cần thiết
import os

#Hàm kiểm tra và tạo thư mục Web Crawler
def check_folder(path):
    os.chdir(path) #di chuyển đến vị trí thư mục
    #path ở đây là C:\\
    kiem_tra_thu_muc = os.listdir(path) #hiện ra các thư mục ở đường dẫn
    if 'Web Crawler' not in kiem_tra_thu_muc: #Nếu chưa có trong thư mục thì hãy tạo thư mục này
        os.mkdir('Web Crawler')

    #Tạo file txt lịch sử các đang đã tải về
    path = 'C:\\Web Crawler'
    os.chdir(path) #di chuyển đến vị trí thư mục
    kiem_tra_thu_muc = os.listdir(path) #hiện ra các thư mục ở đường dẫn
    if 'History.txt' not in kiem_tra_thu_muc: #Nếu chưa có trong thư mục thì tạo thư mục này
            line_1 = "Đây là file ghi lại lịch sử các url đã cào dữ liệu  |\n"
            line_2 = "Số thứ tự của đường link chính là số thứ tự của thư mục chứa nội dung đường dẫn đã cào\n"
            line_3 = "<Ví dụ đường dẫn có số thứ tự 1 thì thư mục chứ nội dung là Các trang web được cào>\n\n"
            content = [line_1, line_2, line_3]
            file = open("History.txt", "w", encoding="utf-8")
            for item in content:
                file.write(item)
            file.close()

#Các hàm
#Hàm này tạo tên file tự động bắt đầu bằng cụm filename tiếp theo là số các file kết thúc là .html
def tao_ten_file_tu_dong(path, url):
    path = "C:\\Web Crawler"
    os.chdir(path) #di chuyển đến vị trí thư mục
    const = "Trang_web_đã_cào_dữ_liệu_thứ_"
    count = len(os.listdir(path)) - 1  # Đếm số file và folder hiện có trong thư mục
    name_folder = const + str(count)  # Trang web đã cào dữ liệu thứ + số thứ tự
    os.mkdir(name_folder)  # Tạo thư mục
    return name_folder

#Hàm lưu nội dung vào file ở thư mục chỉ định
def luu_file(data, name_folder):
    path = "C:\\Web Crawler\\"
    os.chdir(path + str(name_folder))  # Di chuyển đến thư mục vừa được tạo tự động
    #Nội dung trang HTML cần đưa về
    line_noidung_1 = str(data[0])
    url = [line_noidung_1]
    file = open("HTML.HTML", "w+", encoding="utf-8")
    for item in url:
        file.write(item)
    file.close()
def luu_lich_su_cac_url(url):
    path = "C:\\Web Crawler\\"
    os.chdir(path)  #di chuyển đến vị trí thư mục
