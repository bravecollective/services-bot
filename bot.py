# Command Bot (c) 2015
# Matthew Glinski
# MIT Licensed
# Since: v0.0.1
#

from flask import Flask

app = Flask(__name__)

# Root URI
@app.route('/')
def hello_world():
    return 'Hello World!'

# App startup if running file directly
if __name__ == '__main__':
    app.run()
