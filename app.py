from flask import Flask, redirect, url_for, session, render_template
from authlib.integrations.flask_client import OAuth
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id='107589597057-nmigg8fd0611grc6cn5lkquegbtgbprl.apps.googleusercontent.com', # Google Cloud에서 받은 클라이언트 ID
    client_secret='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', # 클라이언트 비밀
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    userinfo_endpoint='https://www.googleapis.com/oauth2/v3/userinfo',
    client_kwargs={'scope': 'openid profile email'},
)
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('./index.html')

# 로그인 라우트
@app.route('/login')
def login():
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)

# Google 로그인 후 콜백 라우트
@app.route('/authorize')
def authorize():
    token = google.authorize_access_token()
    resp = google.get('userinfo')
    user_info = resp.json()
    # 사용자 정보를 화면에 표시하기 위해 간단히 처리합니다.
    return f'<h1>Welcome, {user_info["name"]}!</h1>'
