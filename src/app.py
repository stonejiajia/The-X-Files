# -*- coding: utf-8 -*-

from bottle import route, run, get, post, request


@route('/')
@route('/index.html')
def index():
    return '''<a href="/chart">书单排行表</a>
        <p> </p>
        <a href="/chart_week">本周排行表</a>
        <p> </p>
        <a href="/login">登陆</a>'''

@route('/chart')
def chart():
    return '总书单柱状图'

@route('/chart_week')
def chart_week():
    return '本周柱状图'


#@route('/login')
@get('/login')
def login_form():# p前面有没有“/”没区别吗？“/”是干嘛的？
    return '''<form method = "POST">
         <p>用户名：<p><input name="name" type="text" />
         <p>密码：</p><input name="password" type="password" />
         <p> </p>
         <input type="submit" value="Login" />
         </form>'''

#@route('/login', method = 'POST')
@post('/login')
def login():
    name = request.forms.get('name')
    password = request.forms.get('password')
    if check_login(name, password):#这里有个疑问，怎么将用户名写入？
        return '''<p>Hi,name???. Your login was correct</p>
                  <a href="/chart">书单排行表</a>
                  <p> </p>
                  <a href="/chart_week">本周排行表</a>'''
    else:
        return '<p>Login failed</p>'

def check_login(name, password):
    if name == "text" and password == "password":
        check_login = True
        print check_login
        return True
    else:
        check_login = False
        print check_login
        return False

run(host='localhost', port=8080)