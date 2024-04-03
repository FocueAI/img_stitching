import requests
import base64
import os

# 测试图片所在的文件夹
image_dir = r'./test_data/layer-01'

images_base64 = []
for i in os.listdir(image_dir):
    if i.endswith('.jpg'):
        image_path = os.path.join(image_dir,i)
        with open(image_path, "rb") as image:
            encoded_string = base64.b64encode(image.read()).decode('utf-8')
            images_base64.append(encoded_string)

data = {
    'images_base64': images_base64
}

# 设置后端服务器的URL
url = 'http://localhost:5000/rfid/stitch'
response = requests.post(url, json=data)
print(response.text)