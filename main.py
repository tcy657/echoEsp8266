from machine import Pin
import time
import echoLib

SSID = ''
PASSWORD = ''

clientID = "******A"
serverIP = "mqtt.tlink.io"
username = ''
password = ''
topicName = b"your topic"
message = ''

def main_loop():
  try:
    echoLib.connectWifi(SSID,PASSWORD)  
    c = MQTTClient(CLIENT_ID, server,0,username,password)
    if ( 0 != c.connect() ):
      print("connect error.")   
      return
    while 1:
      c.publish(topicName, message, False) 
      time.sleep(1)
  except:
      pass
  finally:
    try:
        c.disconnect()
        print("Disconnected.")
    except Exception:
        print("disconnect error.")   
 
if __name__ == '__main__':
  main_loop() 
