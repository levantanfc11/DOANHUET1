#Các thư viện cần thiết
import requests
from bs4 import BeautifulSoup
import re

#Các hàm cần thiết

#Hàm đọc nội dung trang web
#Kết quả trả về là 1 văn bản dạng chuỗi
def doc_noi_dung(url):

    # Gửi yêu cầu truy cập url
    raw_page = requests.get(url)
    # Lấy code html của trang web được trả về theo url
    content = BeautifulSoup(raw_page.content, "html.parser")
    return content

#Hàm lấy các đường link web trong nội dung đọc về
#Kết quả trả về là 1 list chứa các đường link
def lay_cac_duong_link(content):
    list_url = []
    result = []
    a_tags = content.find_all('a')  # Lọc thẻ <a>
    for item in a_tags:
        link = item.get("href") #lấy các đường dẫn trong href
        list_url.append(link)
    for item in list_url:
        item =str(item)
        if (item.find("http", 0,4)):
            if (item.find("java", 0, 4)):
                if item.find("html", (len(item)-4), len(item)):
                    if item.find("#", 0, 4):
                        if item.find("None", 0 ,4):
                            if len(item) > 2:
                                print(item)
        if not(item.find("http"), 0, 4):
                print(item)
    return result



#Hàm kiểm tra tính hợp lệ của 1 đường link
#Kết quả trả về : True nếu hợp lệ, False nếu không hợp lệ
def kiem_tra_link(link):
    check = re.search("http", link)
    try:
        if link == check.string:
            return True
    except:
        return False



#Hàm chỉnh sửa đường link nếu không đầy đủ
#Kết quả trả về là 1 đường link đầy đủ
def chinh_sua_link(link):
    url_new = str(url) + item     #Thêm phần còn thiếu là https://... vào
    return url_new