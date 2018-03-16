from machine import Pin
import time
import echoLib

pinTrig = 14
pinEcho = 13

SSID = ''
PASSWORD = ''

clientID = "******A"
serverIP = "mqtt.tlink.io"
username = ''
password = ''
topicName = b"your topic"
message = ''

threshold = 20 #cm
lastValue = 0
nowValue = 0

def main_loop():
  try:
    echoLib.connectWifi(SSID,PASSWORD)  
    c = MQTTClient(CLIENT_ID, server,0,username,password)
    if ( 0 != c.connect() ):
      print("connect error.")   
      return
    
    distance = []
    while 1:
      for i in range(1,6): #1-5
          eachValue = echoLib.checkDist(pinTrig, pinEcho)
          distance.append(eachValue)
          time.sleep(0.5)
      nowValue = echoLib.sum2len(distance)
      compareValue = lastValue +threshold
      if ( 0 == nowValue): #erro
        message = 'error'
      elif ( nowValue > compareValue): # empty
        message = 'empty'
      elif ( nowValue > compareValue):  
         message = 'null'
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
