from azure.iot.device import IoTHubModuleClient
 
module_client = IoTHubModuleClient.create_from_edge_environment()
module_client.connect()
 
if __name__ == '__main__':
  while True:
    message = module_client.receive_message_on_input("input1") # block till message arrives
    print("Received - {}!".format(message))