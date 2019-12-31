import time
from azure.iot.device import IoTHubModuleClient

module_client = IoTHubModuleClient.create_from_edge_environment()
module_client.connect()

if __name__ == '__main__':
  while True:
    module_client.send_message_to_output("This message is sent by module03", "output_module03")
    time.sleep(6)
