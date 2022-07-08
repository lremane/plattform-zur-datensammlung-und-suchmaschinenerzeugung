import os
import config
import urllib3
from pyRdfa import pyRdfa
from qaclient.models import IndexConfig, LoginRequest
from qaclient import ApiException, Configuration, ApiClient
from qaclient.apis import UserControllerApi, DatasetControllerKgApi

from flask import Flask, render_template, request, jsonify, send_file

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config.update(config.load_config_general().get('flask'))

crawler = pyRdfa()
client_config = Configuration(api_key_prefix={'Authorization': 'Bearer'})


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/version")
def version():
    return render_template('index2.html')


@app.route('/process_run', methods=['POST'])
def process_run():
    url = request.get_json()[0]['url']
    dataset = request.get_json()[1]['filename']
    result = crawler.rdf_from_source(url, outputFormat='nt')

    if result:
        if not os.path.exists("./rdfData"):
            os.mkdir("./rdfData")
        with open(f"./rdfData/{dataset}.nt", "wb") as f:
            f.write(result.encode('utf-8'))

    with ApiClient(client_config) as api_client:
        api_instance = DatasetControllerKgApi(api_client)
        file = f'rdfData/{dataset}.nt'
        index_config = IndexConfig(dataset=dataset)

        try:
            api_instance.upload_using_post(dataset, file)
            api_instance.index_using_post(index_config)
            return jsonify('ok')
        except ApiException:
            return jsonify('Error while processing')


def upload_dataset():
    pass


@app.route('/check_login_data', methods=['POST'])
def check_login_data():
    with ApiClient(client_config) as api_client:
        api_instance = UserControllerApi(api_client)
        login_request = LoginRequest(username_or_email=request.get_json()[0]['username'],
                                     password=request.get_json()[1]['password'])

        try:
            auth = api_instance.signin_using_post(login_request)
            client_config.api_key = {'Authorization': auth.access_token}

            return jsonify({'res': '1'})
        except ApiException:
            return jsonify({'res': '0'})


@app.route('/crawl-your-data', methods=['POST'])
def check_login_data_2():
    with ApiClient(client_config) as api_client:
        api_instance = UserControllerApi(api_client)
        login_request = LoginRequest(username_or_email=request.form.get('username'),
                                     password=request.form.get('password'))

        try:
            auth = api_instance.signin_using_post(login_request)
            client_config.api_key = {'Authorization': auth.access_token}

            return render_template('index3.html')
        except ApiException:
            return render_template('error.html')


@app.route('/data_downloader/<filename>', methods=['POST', 'GET'])
def data_downloader(filename):
    return send_file('rdfData/' + filename + '.nt', as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
