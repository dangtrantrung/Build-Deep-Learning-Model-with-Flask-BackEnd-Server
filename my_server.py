from flask import request
from flask import Flask
from flask_cors import CORS, cross_origin

import numpy as np
import cv2
import base64


# Khởi tạo Flask Server BE
app=Flask(__name__)
# Apply Flask - CORS
CORS(app)
app.config['CORS_HEADERS'] ='Content-Type'

# hàm chuyển đổi từ base64 to image
def from_base64_to_image(staff_pix):
    try:
        staff_pix=np.fromstring(base64.b64decode(staff_pix),dtype=np.uint8)
        staff_pix=cv2.imdecode(staff_pix,cv2.IMREAD_ANYCOLOR)
    except:
        return None
    return staff_pix

# hàm đếm số mặt trong ảnh
def dem_so_mat(face):

     # Khởi tạo bộ phát hiện khuôn mặt
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    # Chuyen gray
    gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
    # Phát hiện khuôn mặt trong ảnh
    faces = face_cascade.detectMultiScale(gray, 1.2, 10)

    so_mat = len(faces)
    return so_mat



# define App routes
@app.route("/")
def hello():
    return "Hello World!"

@app.route('/add',methods=['POST','GET'])
@cross_origin(origin='*')
def add_process():
    return 'hàm cộng'

@app.route('/minus',methods=['POST','GET'])
@cross_origin(origin='*')
def minus_process():
    a=(int)(request.args.get('sothunhat'))
    b=(int)(request.args.get('sothuhai'))
    return 'Kết quả là: ' +str(a-b)

@app.route('/multiply',methods=['POST','GET'])
@cross_origin(origin='*')
def multiply_process():
    return 'hàm nhân'

@app.route('/divide',methods=['POST','GET'])
@cross_origin(origin='*')
def divide_process():
    return 'hàm chia'

@app.route('/viethoa',methods=['GET'])
@cross_origin(origin='*')
def upper_process():
    chuoiinput=request.args.get('chuoi')
    return 'Kết quả là: ' +str.upper(chuoiinput)

@app.route('/viethoapost',methods=['POST'])
@cross_origin(origin='*')
def upper_post_process():
    s=request.form.get('inputchuoi')
    return s.upper()

@app.route('/nhandienkhuonmat',methods=['POST'])
@cross_origin(origin='*')
def nhandienkhuonmat_process():
    face_number=0

    # đọc ảnh từ client gửi lên
    facebase64= request.form.get('facebase64')

    # chuyển base64 về OpenCV format
    face=from_base64_to_image(facebase64)

    # đếm số mặt trong ảnh
    face_number=dem_so_mat(face)

    # trả về

    return "Số mặt trong ảnh là: " +str(face_number)


#Start Back End

if __name__=='__main__':
    print("server is starting")
    app.run(ssl_context='adhoc',host='0.0.0.0',port='9999')
