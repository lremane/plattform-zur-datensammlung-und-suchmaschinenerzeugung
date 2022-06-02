from QAclient.client import QAClient
from flask import Flask, render_template, request, jsonify
from crawler.crawler import Crawler

app = Flask(__name__, template_folder='templates', static_folder='css')
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/qaclient')
def index():
  return render_template('qaclient.html')

@app.route('/sendQAClient', methods=['POST', 'GET'])
def sendQAClient():
  qaclient     = QAClient()
  access_token = ''
  if request.method == 'POST':
    username     = request.get_json()[0]['username']
    password     = request.get_json()[1]['password']
    access_token = qaclient.login(username, password)['accessToken']

  results = {'fetchedData': access_token}

  return jsonify(results)

@app.route('/crawler-run', methods=['POST', 'GET'])
def crawler_run():
  if request.method == 'POST':
    Crawler(request.get_json(), 'test666')

  return jsonify('ok')

if __name__ == '__main__':
	app.run(debug = True, host = '0.0.0.0', port = 5000)
