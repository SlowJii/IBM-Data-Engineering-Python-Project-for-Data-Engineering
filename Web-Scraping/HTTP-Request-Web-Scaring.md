

Chúng ta sẽ thảo luận về giao thức HTTP sử dụng thư viện Requests, một phương pháp phổ biến để xử lý giao thức HTTP trong Python. Chúng ta sẽ xem xét:

- Tổng quan về thư viện Requests của Python để làm việc với giao thức HTTP.
- Giới thiệu về các yêu cầu GET và POST.

#### Thư viện Requests:
Requests là một thư viện Python cho phép bạn dễ dàng gửi các yêu cầu HTTP/1.1. Bạn có thể import thư viện như sau:
```python
import requests
```

#### Ví dụ về yêu cầu GET:
Bạn có thể thực hiện một yêu cầu GET đến `www.ibm.com` như sau:
```python
response = requests.get('https://www.ibm.com')
print(response.status_code)  # In ra mã trạng thái (200 cho OK)
```
- Sử dụng `response.headers` để xem tiêu đề phản hồi.
- Sử dụng `response.text` để hiển thị nội dung HTML trong thân phản hồi.

#### Yêu cầu POST:
Khác với GET, yêu cầu POST gửi dữ liệu trong phần thân yêu cầu (request body) thay vì trong URL. Để thực hiện yêu cầu POST, bạn thay đổi endpoint và sử dụng phương thức `post()` như sau:
```python
payload = {'name': 'Joseph', 'ID': '123'}
response = requests.post('https://httpbin.org/post', data=payload)
print(response.text)
```
- Kết quả của POST không chứa các cặp tên-giá trị trong URL, mà chúng được gửi trong phần thân yêu cầu.

---



Chúng ta sẽ tìm hiểu về Web Scraping. Sau khi xem xong, bạn sẽ có thể:

- Định nghĩa khái niệm web scraping;
- Hiểu vai trò của các đối tượng BeautifulSoup;
- Áp dụng phương thức `find_all`;
- Thực hiện web scraping trên một trang web.

#### Web Scraping là gì?
Web scraping là quá trình tự động trích xuất thông tin từ một trang web. Thay vì tốn hàng giờ để sao chép thủ công, bạn có thể hoàn thành công việc trong vài phút với một chút mã Python và sự trợ giúp từ hai module: Requests và BeautifulSoup.

#### Ví dụ:
Giả sử bạn cần tìm tên và lương của các cầu thủ trong Giải bóng rổ quốc gia từ một trang web.  
1. **Nhập BeautifulSoup**:  
   ```python
   from bs4 import BeautifulSoup
   ```
2. **Phân tích HTML**:  
   Lưu HTML của trang web dưới dạng chuỗi và sử dụng BeautifulSoup để phân tích:
   ```python
   soup = BeautifulSoup(HTML, 'html.parser')
   ```

#### Phân tích cấu trúc:
BeautifulSoup đại diện cho HTML dưới dạng các đối tượng cây (Tree-like objects).  
- Ví dụ: Để truy cập thẻ `<title>`, bạn có thể sử dụng:
  ```python
  title = soup.title
  ```

#### Áp dụng `find_all`:
Phương thức `find_all` lọc và trả về tất cả các thẻ phù hợp:
- Ví dụ: Lấy tất cả các hàng trong bảng HTML:
  ```python
  rows = soup.find_all('tr')
  for row in rows:
      cells = row.find_all('td')
      for cell in cells:
          print(cell.text)
  ```

#### Kết hợp với Requests:
Để lấy dữ liệu HTML từ một trang web:
```python
import requests
response = requests.get('https://example.com')
soup = BeautifulSoup(response.text, 'html.parser')
```
Sau đó, bạn có thể sử dụng BeautifulSoup để duyệt và trích xuất thông tin từ trang HTML đó. Hãy thử thực hành trong các bài lab.