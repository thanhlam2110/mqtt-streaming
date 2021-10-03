import paho.mqtt.client as mqtt
import time
import datetime
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("mqtt-topic")

def on_message(client, userdata, msg):
    print(" Topic : "+str(msg.topic)+"  and Message is : "+str(msg.payload))

def on_subscribe(client, userdata,mid, granted_qos):
    print ("userdata : " +str(userdata))

mqttc = mqtt.Client("Python-MQTT-Pub-Sub")
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.on_subscribe = on_subscribe
mqttc.connect("localhost",1883, 60)
i=0
text_file = open("start.txt", "w")
text_file.write("Start: %s" % datetime.datetime.now().time())
text_file.close()
while i<1000000:
    mqttc.publish("mqtt-topic",i)
    print ("publish message " + str(i))
    i+=1
text_file = open("stop.txt", "w")
text_file.write("Stop: %s" % datetime.datetime.now().time())
text_file.close()
mqttc.loop_forever()
