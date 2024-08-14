import urllib, json, random
from datetime import datetime
from flask import render_template, flash, jsonify, redirect, url_for, request
from monitor import app
from monitor import config

page={
    'now': datetime.now(),
    'title': '',
    'app': config.app_data,
    'status':{
        'wifi':'normal',
        'alarm':'normal'
        }
    }

def get_data():
    d={}
    try:
        # read sensors room temp, water temp, input power,
        # Magnet Monitor data, wifi, internet, shield cooler status,...
        # fill data in d and status in stat
        with urllib.request.urlopen(config.MagMon) as f:
            d = json.load(f)
            #TODO add recieved data to csv logger
        stat = {'wifi':'normal', 'alarm':'normal'}
    except urllib.error.URLError:
        d['recieved']='No Data!'
        stat = {'wifi':'error','alarm':'alarm'}
    except json.JSONDecodeError:
        d['recieved']='Bad Data!'
        stat = {'wifi':'alarm','alarm':'error'}
    # if error in notify_list: notify(error)
    # notify_levels =['siren', 'notification', 'sms']
    page['status']=stat
    return d

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
    page['now']= datetime.now()
    page['title']= 'Home'
    page['app']['refresh']=config.app_data['refresh']
    
    data = get_data()
    return render_template('index.html', page=page, data=data)

@app.route('/log')
def viewlog():
    page['now']= datetime.now()
    page['title']= 'Log Charts'
    page['app']['refresh']='600'

    #TODO: get dataset from recorded weekly data csv 
    dataset ={ 
        'hepp': [
            {'label': 'Pressure',
            'data': [random.uniform(-1,1) for _ in range(7)],
            'backgroundColor': config.chart_colors[0],
            },
            {'label': '%He',
            'data': [random.uniform(-1,1) for _ in range(7)],
            'backgroundColor': config.chart_colors[1],
            },
        ],
        'cryo': [
            {'label': 'ColdHead',
            'data': [random.uniform(-1,1) for _ in range(7)],
            'backgroundColor': config.chart_colors[2],
            },
            {'label': 'Sleave',
            'data': [random.uniform(-1,1) for _ in range(7)],
            'backgroundColor': config.chart_colors[3],
            },
        ]
    }
    return render_template('log.html', page=page, dataset=dataset)

@app.route('/settings/<p>', methods=['GET','POST'])
@app.route('/settings', defaults={'p':None})
def settings(p):
    page['now']= datetime.now()
    page['title']= 'Settings'
    page['app']['refresh']='600'
    if request.method == 'POST':
        print(request.form)
        flash('Done.')        
        return redirect(url_for('index'))
    if p: return render_template(f'settings-{p}.html', page=page)
    else: return render_template(f'settings.html', page=page)

@app.route('/wifi')
def wifi():
    page={'now': datetime.now(),'title': 'Wifi', 'app': config.app_data, 'status':{}}
    #TODO: verify wifi and show errors
    return render_template('wifi.html', page=page)

@app.route('/alarm')
def alarm():
    page={'now': datetime.now(),'title': 'Alarm', 'app': config.app_data, 'status':{}}
    #TODO: show alarms recorded...
    return render_template('alarm.html', page=page)

@app.route('/r')
def r():
    page={'now': datetime.now(),'title': 'r', 'app': config.app_data, 'status':{}}
    return render_template('r.html', page=page)

