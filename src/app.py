import os

from crawler.RdfaCrawler import RdfaCrawler
from QAclient.client import QAClient
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['TEMPLATES_AUTO_RELOAD'] = True


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
    crawler = RdfaCrawler()
    result = crawler.get_rdfa(url)
    if result:
        if not os.path.exists("./rdfData"):
            os.mkdir("./rdfData")
        with open(f"./rdfData/{filename}.nt", "w") as f:
            f.write(result)
        return jsonify('ok')
    else:
        return jsonify('Error!')


@app.route('/tonys-page', methods=['POST'])
def check_login_data():
    qaclient = QAClient()
    has_account = ''

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        has_account = qaclient.login(username, password)

        if has_account == '0':
            return render_template('error.html')
        else:
            return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
