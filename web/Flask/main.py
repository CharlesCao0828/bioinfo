from flask import Flask, render_template, request
from awsrequests import AwsRequester
import json

APIGateway_URL = "https://c8r59wbfoc.execute-api.ap-southeast-1.amazonaws.com/test/dynamodbmanager"
app = Flask(__name__)
@app.route('/')
def main_page():
  return render_template('form.html')


@app.route('/upload', methods = ['GET', 'POST'])
def upload():
  if request.method == 'POST':
     req = AwsRequester("ap-southeast-1")
     submit_info_dict = {"lambda_sfn_input" : 
             {
                 "ProjectNo" : request.form.get('ProjectNo'),
                 "INPUT_BUCKET" : request.form.get('INPUT_BUCKET'),
                 "INPUT_KEY" : request.form.get('INPUT_KEY'),
                 "OUTPUT_BUCKET" : request.form.get('OUTPUT_BUCKET')
                 }
             }
     req.post(APIGateway_URL, json = submit_info_dict)
     print type(submit_info_dict)
     return submit_info_dict

if __name__ == '__main__':
    app.run(debug = True, host="0.0.0.0", port=8081)
