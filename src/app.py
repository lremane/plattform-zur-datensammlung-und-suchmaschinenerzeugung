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
client_config = Configuration(api_key_prefix={'JWT': 'Bearer'})


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/version")
def version():
    return render_template('index2.html')


@app.route('/process_run', methods=['POST'])
def process_run():
    url = request.get_json()[0]['url']
    filename = request.get_json()[1]['filename']
    result = crawler.rdf_from_source(url, outputFormat='nt')

    # Stores crawled file in rdfData/
    if result:
        if not os.path.exists("./rdfData"):
            os.mkdir("./rdfData")
        with open(f"./rdfData/{filename}.nt", "w") as file:
            file.write(result)

    # Uploads crawled .nt file to QAnswer and indexes the filename
    with ApiClient(client_config) as api_client:
        api_instance = DatasetControllerKgApi(api_client)
        with open(f'rdfData/{filename}.nt', 'rb') as file:
            try:
                api_instance.upload_using_post(filename, file)
                api_instance.index_using_post(IndexConfig(dataset=filename))
                return jsonify('ok')
            except ApiException:
                return jsonify('Error while processing')



@app.route('/check_login_data', methods=['POST'])
def check_login_data():
    # Checks validates user credentials and stores authentication token in config
    with ApiClient(client_config) as api_client:
        login_request = LoginRequest(username_or_email=request.get_json()[0]['username'],
                                     password=request.get_json()[1]['password'])

        try:
            auth = UserControllerApi(api_client).signin_using_post(login_request)
            client_config.api_key = {'JWT': auth.access_token}
            return jsonify({'res': '1'})
        except ApiException:
            return jsonify({'res': '0'})


@app.route('/crawl-your-data', methods=['POST'])
def check_login_data_2():
    # Checks validates user credentials and stores authentication token in config
    with ApiClient(client_config) as api_client:
        login_request = LoginRequest(username_or_email=request.form.get('username'),
                                     password=request.form.get('password'))

        try:
            auth = UserControllerApi(api_client).signin_using_post(login_request)
            client_config.api_key = {'JWT': auth.access_token}

            return render_template('index3.html')
        except ApiException:
            return render_template('error.html')


@app.route('/data_downloader/<filename>', methods=['POST', 'GET'])
def data_downloader(filename):
    return send_file('rdfData/' + filename + '.nt', as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
