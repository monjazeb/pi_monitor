from monitor import app
from monitor import security

if __name__ == '__main__':
    if security.authenticate.isOK():
        app.run(debug=False, host='0.0.0.0')
