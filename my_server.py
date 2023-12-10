from flask import request
from flask import Flask
from flask_cors import CORS, cross_origin

# Khởi tạo Flask Server BE
app=Flask(__name__)
# Apply Flask - CORS
CORS(app)
app.config['CORS_HEADERS'] ='Content-Type'

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

#Start Back End

if __name__=='__main__':
    print("server is starting")
    app.run(ssl_context='adhoc',host='0.0.0.0',port='9999')
