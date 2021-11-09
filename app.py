from flask import Flask, render_template, request
from keras.preprocessing.image import img_to_array
from keras.models import load_model
from PIL import Image
import io
import boto3

AWS_ACCESS_KEY = ""
AWS_SECRET_KEY = ""
BUCKET_NAME = ""

s3 = boto3.client('s3',
        aws_access_key_id = AWS_ACCESS_KEY,
        aws_secret_access_key = AWS_SECRET_KEY)

app = Flask(__name__)
# export model
model = load_model('data/h5/model.h5')

@app.errorhandler(404)
def page_not_found(error):

	return render_template('404.html'), 404

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        
        return render_template('index.html')

    if request.method == 'POST':
        try:
            if request.form.get('gender'):
                # female predict
                img = request.files["file"]
                pred_img = img.read()
                upload_img(img)
                pred_img = Image.open(io.BytesIO(pred_img)).convert("RGB")
                pred_img = pred_img.resize((256, 256))
                pred_img = img_to_array(pred_img)
                pred_img = pred_img.reshape((1, 256, 256, 3))
                pred = model.predict(pred_img)
                label = pred.argmax()
                label = 'f' + str(label)
                print(label)
            
                return render_template("index.html", label=label)    
        
            else:
                # male predict
                img = request.files["file"]
                pred_img = img.read()
                upload_img(img)
                pred_img = Image.open(io.BytesIO(pred_img)).convert("RGB")
                pred_img = pred_img.resize((256, 256))
                pred_img = img_to_array(pred_img)
                pred_img = pred_img.reshape((1, 256, 256, 3))
                pred = model.predict(pred_img)
                label = pred.argmax()
                label = 'm' + str(label)
                
                return render_template("index.html", label=label)    
        except:

            return render_template('404.html'), 404

def upload_img(image):
    image.seek(0) # s3 저장에 필요
    s3.put_object(
        Bucket = BUCKET_NAME, # 버킷 이름
        Body = image, # 업로드 파일
        Key = 'image/{}'.format(image.filename), # 저장 위치 및 이름 지정
        ContentType = image.content_type) # 이미지 타입
    

if __name__ == "__main__":
    app.run(debug=True)
