# Các thư viện cần thiết
import folder_op, web_op

def start():
    url =str(input("Nhập url cần tải :")) #Chứa các đường link chưa duyệt
    n = int(input("Nhập giới hạn trang cần tải về :"))
    url_list = [] #Danh sách các đường link hàng chờ
    history=[]  #Chứa các đường link đã duyệt
    max_page= n    #Quy định số lượng trang web được tải về
    folder_op.check_folder("C:\\") #Kiểm tra và tạo thư mục Web Crawler
    data_folder = 'C:\\Web Crawler' #Lưu dữ liệu vào bên trong thư mục Web Crawler
    count=0     #Đếm số lượng trang web đã tải
    url_list.append(str(url)) #Thêm đường dẫn vào danh sách hàng chờ




    #kịch bản các trang web
    while (count < max_page) and (len(url_list) > 0):
        url = str(url_list.pop(0))
        page = web_op.doc_noi_dung(url)
        links = web_op.lay_cac_duong_link(page)
        url_new = [] #Danh sách chứa các đường link mới được tìm thấy
        url_new_max = 1000 #Số lượng tối đa mà danh sách mới tìm thấy có thể chứa
        for item in links:  #Duyệt từng đường link thu được để kiểm tra tính hợp lệ
            if web_op.kiem_tra_link(item) == False: #Kiểm tra tính hợp lệ
                item = web_op.chinh_sua_link(url, item)
            url_new.append(item)    #Lưu lại cái file url hợp lệ
            url_list = url_list + url_new
        count += 1 #Đếm số đường dẫn đã duyệt
        history.append(url) #Lưu lại đường dẫn vừa mới nhận được vào lịch sử
        data1 = [page, url, url_new, url_new_max]
        name_folder = folder_op.tao_ten_file_tu_dong(data_folder,url)
        folder_op.luu_file(data1, name_folder)
        folder_op.luu_lai_lich_su_url(url)
if __name__ == '__main__':
    start()