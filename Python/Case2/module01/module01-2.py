from flask import Flask
from flask import request
from azure.iot.device import IoTHubModuleClient

app = Flask(__name__)

module_client = IoTHubModuleClient.create_from_edge_environment()
module_client.connect()

# ********************************************************************
# GET http://Raspberry-Pi-IP:8080/message/hello_world
# ********************************************************************
@app.route('/message/<content>')
def get_message(content):
  module_client.send_message_to_output(content, "output1")
  return "Message - {}!".format(content)

if __name__ == '__main__':
  app.run(
      host='0.0.0.0',
      port = 8080
  )