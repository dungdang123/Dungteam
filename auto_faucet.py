import requests

# Địa chỉ ví TRON của bạn (cần thay thế)
address = "TAuGq11BHvnqTw3mDDhhtA7zWQtnvdBuhm"  # Đặt địa chỉ ví TRON của bạn vào đây

# URL faucet Shasta
faucet_url = "https://www.trongrid.io/shasta/faucet"

# Dữ liệu request
data = {
    "address": address
}

# Gửi request
response = requests.post(faucet_url, data=data)

# Kiểm tra kết quả
if response.status_code == 200:
    print("Đã xin TRX thành công!")
    print(response.text)
else:
    print("Có lỗi xảy ra:", response.status_code)#