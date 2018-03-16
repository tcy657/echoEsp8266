from machine import Pin
import time
import echoLib

pinTrig = 14
pinEcho = 13

SSID = 'zz'
PASSWORD = '521684zz'

clientID = "iot12345"
serverIP = 'test.mosquitto.org'
username = ''
password = ''
topicName = b"HkWlHbOHz"

compareValue = 200 #cm
lastMessage = 'error'
nowMessage = ''
nowValue = 0

def main_loop():
    try:
        io16 =Pin(16,Pin.OUT) #for check
        io16.value(0)
        time.sleep(1)
        io16.value(1)   
        time.sleep(1)
        
        print("s0")
        echoLib.connectWifi(SSID,PASSWORD)  
        c = MQTTClient(CLIENT_ID, server,0,username,password)
        print("s1")
        if ( 0 != c.connect() ):
            print("connect error.")   
            return
        print("s2")
        distance = []
        checkAgainFlag = False
        while 1:
            print("s3")
            for i in range(1,6): #1-5
                eachValue = echoLib.checkDist(pinTrig, pinEcho)
                distance.append(eachValue)
                time.sleep(0.5)
            nowValue = echoLib.sum2len(distance)
            print("s4")
            print(nowValue)
            if ( 0 == nowValue): #erro
                nowMessage = 'error'
            elif ( nowValue > compareValue): # empty
                nowMessage = 'empty'
            else: #full 
                nowMessage = 'full'
            print("s5")
            c.publish(topicName, nowMessage, False)
            #if ( nowMessage != lastMessage): #check again
            #  checkAgainFlag = True
            #  time.sleep(10) #after 10s
            #else:
            #  checkAgainFlag = False
            #   
            #if (False == checkAgainFlag) and (nowMessage != lastMessage):
            #  lastMessage = nowMessage

            print("s6")
            time.sleep(1)
            io16.value(0)
            time.sleep(1)
            io16.value(1)   
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
