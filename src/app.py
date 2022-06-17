import os
import config

from QAclient.client import QAClient
from crawler.RdfaCrawler import RdfaCrawler
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config.update(config.load_config_general().get('flask'))


qaclient = QAClient()
crawler = RdfaCrawler()


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/version")
def version():
    return render_template('index2.html')


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


@app.route('/check_login_data', methods=['POST'])
def check_login_data():
    qaclient.login(request.get_json()[0]['username'],
                   request.get_json()[1]['password'])

    if qaclient.token:
        return jsonify({'res': '1'})
    else:
        return jsonify({'res': '0'})


@app.route('/crawl-your-data', methods=['POST'])
def check_login_data_2():

    qaclient.login(request.form.get('username'), request.form.get('password'))

    if qaclient.token:
        return render_template('index3.html')
    else:
        return render_template('error.html')
    
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
