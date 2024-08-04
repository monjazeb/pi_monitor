import urllib
from datetime import datetime
from flask import Flask, render_template
from security import authenticate

app = Flask(__name__)
MagMon = "http://10.0.2.162:5000/data"

app_data = {'name':'MMM',
            'company': 'ARPA Medical co.',
            'version': 'v0.1 2024'}

@app.route('/')
def index():
    page={'now': datetime.now(),'title': 'Home', 'app': app_data}
    data={'percentage': '105 %','pressure':'3.25 PSI'}
    with urllib.request.urlopen(MagMon) as f:
        data['pressure'] = f.read()
    page['wifi_status'] = 'error'
    page['alarm_status'] = 'alarm'
    return render_template('index.html', page=page, data=data,)

@app.route('/data')
def data():
    page={'now': datetime.now(),'title': 'Home', 'app': app_data}
    return "data here"

@app.route('/alarm')
def alarm():
    page={'now': datetime.now(),'title': 'Home', 'app': app_data}
    return render_template('alarm.html', page=page)

@app.route('/log')
def viewlog():
    page={'now': datetime.now(),'title': 'Home', 'app': app_data}
    return render_template('log.html', page=page)

@app.route('/settings')
def settings():
    page={'now': datetime.now(),'title': 'Home', 'app': app_data}
    return render_template('settings.html', page=page)

@app.route('/r')
def r():
    page={'now': datetime.now(),'title': 'Home', 'app': app_data}
    return render_template('r.html', page=page)




if __name__ == '__main__':
    if authenticate.isOK():
        app.run(debug=True, host='0.0.0.0')

