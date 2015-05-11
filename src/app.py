# -*- coding: utf-8 -*-

from bottle import route,run

@route('/')
@route('/index.html')
def index():
    return '<a href="/hello">书单排行表</a>'
#return '<a href="/hello">本周排行表</a>'

@route('/hello')
def hello():
    return '柱状图'

run(host='localhost', port=8080)