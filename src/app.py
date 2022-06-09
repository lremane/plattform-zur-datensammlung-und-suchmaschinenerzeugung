from crawler.rdfaCrawler import rdfaCrawler
from QAclient.client import QAClient
from flask import Flask, render_template, request, jsonify
from src import config

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config.update(config.load_config_general().get('flask'))


@app.route("/")
def home():
    return render_template('login.html')


@app.route('/qaclient')
def index():
    return render_template('qaclient.html')


@app.route('/crawler-run', methods=['POST', 'GET'])
def crawler_run():
    if request.method == 'POST':
        url = request.get_json()[0]['url']
        filename = request.get_json()[1]['filename']
        crawler = rdfaCrawler()
        crawler.parseRdfa(url, filename)

    return jsonify('ok')


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
