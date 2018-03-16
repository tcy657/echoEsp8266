from simple import MQTTClient
import network
import time

#for log file
#return ok-True, bad-False
def writeLogTime(fileNameStr, logStr):
  try:
    import time
    if os.path.exists(fileNameStr) and os.path.getsize(fileNameStr) >= 5000:
      os.remove(fileNameStr)
      f = open(fileNameStr, 'w')
      f.close()

    with open(fileNameStr, 'a') as f:
     timeDate=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
     f.write(timeDate + ": " + logStr +"\n")
     f.close()

    return True
  except Exception:
    print( "writeLogFile_Time(), error!")
    return False

#read file
def readFile(fileNameStr):
  try:
    import os
    with open(fileNameStr) as f:
      print(f.read())
  except Exception:
    print( "readFile(), error!")

#for check distance
#return ok-number, bad-0
def checkDist(pinTrig, pinEcho):
    try:
     import time
     from machine import Pin
     Trig, Echo = Pin(pinTrig, Pin.OUT), Pin(pinEcho, Pin.IN)
     Trig.value(0)
     Echo.value（0）
     Trig.value(1)
     time.sleep(0.00001)
     Trig.value（0）
     while(Echo.value()==0):
         pass
     t1 = time.ticks_us()
     while(Echo.value()==1):
         pass
     t2 = time.ticks_us()
     t3 = time.ticks_diff(t2, t1)/10000
     return t3*340/2
    except Exception:
        print( "checkDist(), error!")
        return 0

#sum(l)/len(l), l=[1,2,3,4,5,6]
def sum2len(binList):
  try:
    lenght =len(binList)
    count0 = binList.count(0)
    distance = 0
    if ( 0 == lenght):
        distance = 0
    elif (lenght == count0): #[0,0,0]
        distance = 0
    else:
        lenght = lenght - count0
        distance = "{:.2f}".format(sum(binList)/lenght)
    return distance
  except Exception:
    print( "sum2len(), error!")
    return 0

#set time and data
def setTimeData(year = 2017, month = 8, day =23, week =1, hour =12, minute =48):
    try:
        import RTC
        rtc = RTC()
        rtc.datetime((year, month, day, week, hour, minute, 0, 0)) # set a specific date and time
        rtc.datetime() # get date and time
    except Exception:
        print( "setTimeData(), error!")

def connectWifi(ssid,passwd):
  wlan=network.WLAN(network.STA_IF)
  wlan.active(True)
  wlan.disconnect()
  wlan.connect(ssid,passwd)
  while(wlan.ifconfig()[0]=='0.0.0.0'):
    time.sleep(1)  #time.sleep_ms(10)

def publishMessage(clientID, serverIP, username, password, topicName, message):
  try:
     c = MQTTClient(clientID, serverIP,1883,username,password)
     if ( 0 == c.connect() ):
       c.publish(topicName, message, False)
       c.disconnect()
       print("publish ok")
     else:
       print("connect failed")
  except Exception:
      print("publishMessage failed")
