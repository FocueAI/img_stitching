from stitching import AffineStitcher
import cv2,flask

import numpy as np
import time
import base64

app = flask.Flask(__name__)
stitcher = AffineStitcher(crop=False,confidence_threshold=1)

def base64_to_image(base64_code):
    # base64解码
    img_data = base64.b64decode(base64_code)
    # 转换为np数组
    img_array = np.fromstring(img_data, np.uint8)
    # 转换成opencv可用格式
    img = cv2.imdecode(img_array, cv2.COLOR_RGB2BGR)
    return img

def image_to_base64(cv_img):
    _, buffer = cv2.imencode('.jpg',cv_img)
    base64_str = base64.b64encode(buffer).decode('utf-8')
    return base64_str

@app.route('/rfid/stitch',methods=["POST"])
def stitch():
     images_base64 = flask.request.json.get('images_base64',[])
     cv_img_l = [base64_to_image(i) for i in images_base64]
     panorama = stitcher.stitch(cv_img_l)
     # cv2.imwrite('./res__.jpg',panorama)
     cv_img_stitch = image_to_base64(panorama)
     return flask.jsonify({"res":cv_img_stitch})

if __name__ == "__main__":
    app.run(port=5000,debug=True)