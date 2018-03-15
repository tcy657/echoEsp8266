from simple import MQTTClient
import network
import time

#for log file
#return ok-True, bad-False
def writeLogTime(fileNameStr, logStr):
  try:
    import time
    if os.path.exists(fileNameStr) and os.path.getsize(fileNameStr) >= 5000: #存在，文件大于5k？(待测)
      os.remove(fileNameStr) #删除文件
      f = open(fileNameStr, 'w') #创建文件
      f.close()

    with open(fileNameStr, 'a') as f: #追加，必要时创建
     timeDate=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
     f.write(timeDate + ": " + logStr +"\n")
     f.close()

    return True
  except Exception, e:
    exstr = traceback.format_exc()
    print( "writeLogFile_Time(), error!" + '\n' + exstr)
    return False

#for check distance
#return ok-number, bad-0
def checkDist(pinTrig, pinEcho):
  try:
    impot time
    from machine import Pin
    Trig, Echo = Pin(pinTrig, Pin.OUT), Pin(pinEcho, Pin.IN)
    Trig.value(0)
    Echo.value（0）
    Trig.value(1)
    time.sleep(0.00001)
    Trig.value（0）
    while(Echo.value()==0)
        pass
    t1 = time.ticks_us()
    while(Echo.value()==1)
        pass
    t2 = time.ticks_us()
    t3 = time.ticks_diff(t2, t1)/10000
    return t3*340/2
   except Exception, e:
    exstr = traceback.format_exc()
    print( "checkDist(), error!" + '\n' + exstr)
    return 0
    pass

#set time and data
def setTimeData(year = 2017, month = 8, day =23, week =1, hour =12, minute =48):
  try:
    import RTC
    rtc = RTC()
    rtc.datetime((year, month, day, week, hour, minute, 0, 0)) # set a specific date and time
    rtc.datetime() # get date and time
   except Exception, e:
    exstr = traceback.format_exc()
    print( "setTimeData(), error!" + '\n' + exstr)
    pass

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
