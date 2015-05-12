# -*- coding: utf-8 -*-

from bottle import route,run

@route('/')
@route('/index.html')
def index():
    return '''<a href="/chart">书单排行表</a>
        
        <a href="/chart_week">本周排行表</a>'''

@route('/chart')
def chart():
    return '总书单柱状图'

@route('/chart_week')
def chart_week():
    return '本周柱状图'

run(host='localhost', port=8080)