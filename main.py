from logging import exception

from flask import Flask
import redis

# step 2: define our connection information for Redis
# Replaces with your configuration information

app = Flask(__name__)

@app.route('/')
def index():
    r = redis.Redis(host='redis-server', port=639, db=1)
    r.set('hello', 'world')  # True

    value = r.get('hello saumit')

    return value



if __name__ == '__main__':
     app.run(debug=True, port=8081,host='0.0.0.0')