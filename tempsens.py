import conf,json,time,computebounds
from boltiot import Bolt, Sms

highbound=0
lowbound=0
flag=1

def activate():

    prevdata=[]
    global highbound
    global lowbound
    global flag
    
    framesize=5
    temp_sens=Bolt(conf.apikey,conf.device_id)
    sms=Sms(conf.ssid,conf.auth_token,conf.tonumber,conf.fromnumber)
    while True:
        
        response=temp_sens.analogRead('A0')
        data=json.loads(response)
        try:
            sensor_value=int(data['value'])        
            temp=sensor_value/10.24
            print(temp)
            
        except Exception as e:
            print("Error",e)
            continue
        if flag ==1 :
            bounds=computebounds.computebounds(prevdata,framesize)
            if not bounds:
                print("Need ",(framesize-len(prevdata))," more points")
                prevdata.append(temp)
                time.sleep(5)
                continue
        try:
            if flag==1:
                highbound=bounds[0]
                lowbound=bounds[1]
            
            print("High Bound = ",highbound,"   Low Bound = ",lowbound)
            #highbound=data['up']
            #lowbound=data['low']            
            if temp>highbound:
                
                try:
                    print("Temperature has gone up to ", temp)
                    response=sms.send_sms("Temperature has increased to "+str(temp))
                    break
                except Exception as e:
                    print("Error",e)
            elif temp<lowbound:
                
                try:
                    print("Temperature has gone down to ",temp)
                    response=sms.send_sms("Temperature has decreased to "+str(temp))
                    break
                except Exception as e:
                    print("Error",e)
        except Exception as e:
            print("Error ",e)
        prevdata.append(temp)
        time.sleep(5)


