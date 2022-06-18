import os
import config

from QAclient.client import QAClient
from flask import Flask, render_template, request, jsonify
from pyRdfa import pyRdfa
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config.update(config.load_config_general().get('flask'))


qaclient = QAClient()
crawler = pyRdfa()


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/crawler-run', methods=['POST'])
def crawler_run():
    url = request.get_json()[0]['url']
    filename = request.get_json()[1]['filename']
    result = crawler.rdf_from_source(url, outputFormat='nt')
    if result:
        if not os.path.exists("./rdfData"):
            os.mkdir("./rdfData")
        with open(f"./rdfData/{filename}.nt", "wb") as f:
            f.write(result.encode('utf-8'))
        return jsonify('ok')
    else:
        return jsonify('Error!')


@app.route('/upload-data', methods=['POST'])
def upload_data():
    url = request.get_json()[0]['url']
    set_name = request.get_json()[1]['filename']
    data_set = crawler.rdf_from_source(url, outputFormat='nt')

    response = qaclient.new_dataset(set_name, data_set)

    if response == 200:
        return jsonify('ok')
    else:
        return jsonify('Error!')


@app.route('/check_login_data', methods=['POST'])
def check_login_data():
    qaclient.login(request.get_json()[0]['username'],
                   request.get_json()[1]['password'])

    if qaclient.token:
        return jsonify({'res': '1'})
    else:
        return jsonify({'res': '0'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
