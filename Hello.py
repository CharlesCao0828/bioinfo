from flask import Flask, render_template, request
from awsrequests import AwsRequester

APIGateway_URL = "https://c8r59wbfoc.execute-api.ap-southeast-1.amazonaws.com/test/dynamodbmanager"
app = Flask(__name__)
@app.route('/')
def main_page():
  return render_template('form.html')


@app.route('/hello', methods = ['GET', 'POST'])
def upload():
  if request.method == 'POST':
     req = AwsRequester("ap-southeast-1")
     s3_link = request.form.get('usr_name')
     req.post(APIGateway_URL, json = s3_link)
     return s3_link 

if __name__ == '__main__':
    app.run(debug = True, host="0.0.0.0", port=8081)
