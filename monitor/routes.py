import urllib, json
from datetime import datetime
from flask import render_template, flash, jsonify
from monitor import app
from monitor import config


def get_data():
    d={}
    try:
        with urllib.request.urlopen(config.MagMon) as f:
            d = json.load(f)
        stat = {'wifi':'normal', 'alarm':'normal'}
    except urllib.error.URLError:
        d['recieved']='No Data!'
        stat = {'wifi':'error','alarm':'alarm'}
    except json.JSONDecodeError:
        d['recieved']='Bad Data!'
        stat = {'wifi':'alarm','alarm':'error'}
    return d, stat

@app.route('/api')
def api():
    data = {
        'pressure': '2.35 PSI',
        'percent': '98.2 %',
        'coldhead': '42.6 K',
        'waterflow': '5.3 lpm'
    }
    return data

@app.route('/')
def index():
    page={'now': datetime.now(),'title': 'Home', 'app': config.app_data, 'status':{}}
    data, status = get_data()
    page['status'] = status
    return render_template('index.html', page=page, data=data)

@app.route('/alarm')
def alarm():
    page={'now': datetime.now(),'title': 'Alarm', 'app': config.app_data, 'status':{}}
    return render_template('alarm.html', page=page)

@app.route('/log')
def viewlog():
    page={'now': datetime.now(),'title': 'Log', 'app': config.app_data, 'status':{}}
    return render_template('log.html', page=page)

@app.route('/settings')
def settings():
    page={'now': datetime.now(),'title': 'Settings', 'app': config.app_data, 'status':{}}
    return render_template('settings.html', page=page)

@app.route('/wifi')
def wifi():
    page={'now': datetime.now(),'title': 'Wifi', 'app': config.app_data, 'status':{}}
    return render_template('wifi.html', page=page)

@app.route('/r')
def r():
    page={'now': datetime.now(),'title': 'r', 'app': config.app_data, 'status':{}}
    return render_template('r.html', page=page)

