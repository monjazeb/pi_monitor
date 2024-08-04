from datetime import datetime
from flask import Flask, render_template
from security import authenticate

app = Flask(__name__)

app_data = {'name':'MMM',
            'company': 'ARPA Medical co.',
            'version': 'v0.1 2024'}

@app.route('/')
def index():
    page={'now': datetime.now(),'title': 'Home', 'app': app_data}
    data={'percentage': '105 %','pressure':'3.25 PSI'}
    page['status'] = 'alarm'
    return render_template('index.html', page=page, data=data,)

@app.route('/settings')
def settings():
    ...





if __name__ == '__main__':
    if authenticate.isOK():
        app.run(debug=True, host='0.0.0.0')

