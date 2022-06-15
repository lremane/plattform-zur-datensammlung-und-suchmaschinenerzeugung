import os

from QAclient.client import QAClient
from flask import Flask, render_template, request, jsonify
import config
from crawler.RdfaCrawler import RdfaCrawler

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config.update(config.load_config_general().get('flask'))


qaclient = QAClient()
crawler = RdfaCrawler()

@app.route("/")
def home():
    return render_template('login.html')


@app.route('/qaclient')
def index():
    return render_template('qaclient.html')



@app.route('/crawler-run', methods=['POST'])
def crawler_run():
    url = request.get_json()[0]['url']
    filename = request.get_json()[1]['filename']
    result = crawler.get_rdfa(url)
    if result:
        if not os.path.exists("./rdfData"):
            os.mkdir("./rdfData")
        with open(f"./rdfData/{filename}.nt", "w") as f:
            f.write(result)
        return jsonify('ok')
    else:
        return jsonify('Error!')



@app.route('/upload-data', methods=['POST'])
def upload_data():
    url = request.get_json()[0]['url']
    set_name = request.get_json()[1]['filename']
    data_set = crawler.get_rdfa(url)

    response = qaclient.new_dataset(set_name, data_set)

    if response == 200:
        return jsonify('ok')
    else:
        pass


@app.route('/tonys-page', methods=['POST'])
def check_login_data():
    qaclient.login(request.form.get('username'), request.form.get('password'))

    if qaclient.token:
        return render_template('index.html')
    else:
        return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

