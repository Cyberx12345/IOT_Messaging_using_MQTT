import paho.mqtt.client as mqtt

def on_connect(client , userdata , flasgs , rc):
    print("Connected with Result code " , str(rc))
    ## User can subscribe to any topic he or she likes

    client.subscribe('communication')

def on_message(client, userdata, msg):
    print(msg.topic + " \n " + msg.payload.decode("utf-8") + " \n ")

# Next, we instantiate the MQTT client object and set up the callbacks
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message


## Connecting to another raspberry Pi
client.connect('broker.emqx.io', 1883, 60)

## Allowing the progrqam forerver 
client.loop_forever()

# #Sending messages 

# def on_connect(client, userdata, flags, rc):
#     if rc == 0:
#         print("Connected to broker")
#         global Connected  # Use global variable
#         Connected = True  # Signal connection

#     else:
#         print("Connection failed")

# # Then we initialize Connected to False
# Connected = False  # global variable for the state of the connection

# ## Function to run when paho connects to the correct server
# client = mqtt.Client()
# client.on_connect = on_connect
# client.connect("156.38.119.93", 1883, 60)
# client.loop_start()  # start the loop



# ## Waiting for the server to start a connection 
# while Connected != True:  # Wait for connection
#     time.sleep(0.1)


# ## Disconnect when it gets interuppted 


# try:
#     while True:
#         message = input('Your message: ')
#         client.publish("glblcd/sam", message)

# except KeyboardInterrupt:
#     client.disconnect()
#     client.loop_stop()
