from flask import Flask
from flask import request

app = Flask(__name__)

# ********************************************************************
# GET  http://Raspberry-Pi-IP:8080/
# ********************************************************************
@app.route("/")
def hello_world():
  return 'Flask Dockerized on Azure IoT Edge ( Version: 0.1 )'

if __name__ == '__main__':
  app.run(
      host='0.0.0.0',
      port = 8080
  )