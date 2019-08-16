
import subprocess

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/memory')
def load_test_memory():
    sp = subprocess.Popen(['stress', '--vm','1','--vm-bytes','1000M','-t','3'], stdout=subprocess.PIPE)
    sp.stdout.read()
    return 'memory'

@app.route('/cpu')
def load_test_cpu():
    sp = subprocess.Popen(['stress', '-c','1','-t','3'], stdout=subprocess.PIPE)
    sp.stdout.read()
    return 'cpu'

@app.route('/io')
def load_test_io():
    sp = subprocess.Popen(['stress', '-c','1','-t','3'], stdout=subprocess.PIPE)
    sp.stdout.read()
    return 'io'

if __name__ == '__main__':
     app.run(host="0.0.0.0", port=int("8080"))
