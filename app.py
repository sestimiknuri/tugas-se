from flask import Flask, g, url_for, request
import pymysql
from flask import Flask, session, render_template,redirect
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager, current_user,login_required
from datetime import timedelta,datetime
from functools import wraps
from os import environ
import redis
from flask_session import Session

app = Flask('app')
app.config['SECRET_KEY'] = 'mebeditpa234#'
app.debug = True
PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)


login = LoginManager(app)
login.init_app(app)
login.login_view = 'login'



@app.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=30)
    g.user = current_user

@app.errorhandler(404)
def page_not_found(e):
    return render_template("/404.html")

# def limit_menu():
#     getMenu = limitMenu("1")
#     if not getMenu:
#         return render_template("/404.html")


from controllers import home,pylogin,logout, queryUpTup,queryRkakl,queryBelanja,queryHal3Dipa,queryKontrak,setQuery_b,setQuery_a,setQuery_b,pengguna,proyeksi,searching_satker,proyeksi,queryOutputStrategis, confirmPnbp, alokasiPnbp

if __name__ == "__main__":
     app.run('0.0.0.0', port=80)
     
    
