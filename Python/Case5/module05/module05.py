import time
from azure.iot.device import IoTHubDeviceClient

from dotenv import load_dotenv
load_dotenv()
import os
CONNECTION_STRING = os.getenv("CONNECTION_STRING")
device_client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

if __name__ == '__main__':
  while True:
    message = device_client.receive_message()
    print( "Data: {}".format(message) )
