from flask import Flask, redirect, url_for, session, render_template
from authlib.integrations.flask_client import OAuth
import os
from flask_session import Session

app = Flask(__name__)
app.secret_key = os.urandom(24)


# Flask-Session 설정
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id=os.getenv('107589597057-nmigg8fd0611grc6cn5lkquegbtgbprl.apps.googleusercontent.com'),
    client_secret=os.getenv('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'),
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    userinfo_endpoint='https://www.googleapis.com/oauth2/v3/userinfo',
    client_kwargs={'scope': 'openid profile email'},
)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)

@app.route('/authorize')
def authorize():
    token = google.authorize_access_token()
    resp = google.get('userinfo')
    user_info = resp.json()
    # 사용자 정보를 세션에 저장
    session['user_info'] = user_info
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)