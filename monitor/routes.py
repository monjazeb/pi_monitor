import urllib, json
from datetime import datetime
from flask import render_template, flash, jsonify
from monitor import app
from monitor import config


@app.route('/')
def index():
    page={'now': datetime.now(),'title': 'Home', 'app': config.app_data}
    data={}
    try:
        with urllib.request.urlopen(config.MagMon) as f:
            data=json.load(f)
        print(data)
        page['wifi_status'] = 'normal'
        page['alarm_status'] = 'normal'
    except urllib.error.URLError:
        data['pressure']='No Data'
        page['wifi_status'] = 'error'
        page['alarm_status'] = 'alarm'
    return render_template('index.html', page=page, data=data,)

@app.route('/api')
def api():
    # page={'now': datetime.now(),'title': 'Home', 'app': config.app_data}
    data = {
        'pressure': '2.35 PSI',
        'percent': '98.2 %',
        'coldhead': '42.6 K',
        'waterflow': '5.3 lpm'
    }
    return data

@app.route('/alarm')
def alarm():
    page={'now': datetime.now(),'title': 'Home', 'app': config.app_data}
    return render_template('alarm.html', page=page)

@app.route('/log')
def viewlog():
    page={'now': datetime.now(),'title': 'Home', 'app': config.app_data}
    return render_template('log.html', page=page)

@app.route('/settings')
def settings():
    page={'now': datetime.now(),'title': 'Home', 'app': config.app_data}
    return render_template('settings.html', page=page)

@app.route('/wifi')
def wifi():
    page={'now': datetime.now(),'title': 'Home', 'app': config.app_data}
    return render_template('wifi.html', page=page)

@app.route('/r')
def r():
    page={'now': datetime.now(),'title': 'Home', 'app': config.app_data}
    return render_template('r.html', page=page)

