from flask import Flask
from flask_cors import CORS, cross_origin
import requests
import json
from flask import request
import os


def GetURL(VoteID):
    QuestionsURI = 'https://api.mentimeter.com/questions/'+VoteID
    ResultsURI = 'https://api.mentimeter.com/questions/'+VoteID+'/result'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'}
    GetQuestions = requests.get(QuestionsURI, headers=headers)
    Questions=GetQuestions.json()
    GetResults = requests.get(ResultsURI, headers=headers)
    Results=GetResults.json()
    resultDict = {
      "question": Questions['question'],
      "results": Results['results']
    }
    
    return json.dumps(resultDict)
    
app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))
CORS(app, support_credentials=True)

@app.route('/voting')
@cross_origin(supports_credentials=True)
def index():
   #print (request.args.get('questionid'))
   #return (request.args.get('questionid'))
   return (GetURL(request.args.get('questionid')))
   #return y

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=port)
    
#