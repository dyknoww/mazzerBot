# vivekGusain
# MarmikSharma #MaxDevilio
# MayankSingh #Dyknoww

import csv #to save and read data
import time as t #For delay and all
import RPi.GPIO as g #to use gpio
import json  #to convert data in dictionary
import requests as r #to fetch data from a site

g.setmode(g.BOARD)
g.setwarnings(False)
# right forward  wheel 
g.setup(29,g.OUT)
# right backward wheel
g.setup(31,g.OUT)
# left backward wheel
g.setup(33,g.OUT)
# left  forward wheel
g.setup(35,g.OUT)
arr=[]

def direction(p ,k):
   
	#for going forward	
	if p=="f":
		g.output(29,g.HIGH)
		g.output(35,g.HIGH)
		g.output(31,g.LOW)
		g.output(33,g.LOW)
		print("Going Forward")
	#for going backward
	elif p=="b":
		g.output(29,g.LOW)
		g.output(35,g.LOW)
		g.output(31,g.HIGH)
		g.output(33,g.HIGH)
		print("Going Backward")
	#for going right
	elif p=="r":
		g.output(29,g.LOW)
		g.output(31,g.LOW)
		g.output(35,g.HIGH)
		g.output(33,g.LOW)
		print("Going Right")
	#for going left
	elif p=="l":
		g.output(29,g.HIGH)
        	g.output(35,g.LOW)
        	g.output(31,g.LOW)
        	g.output(33,g.LOW)
		print ("Going Left")
	for o in range(k):
                t.sleep(0.23)
                print(o)
                

q = 'a'
while(1):
	data = r.get("https://api.thingspeak.com/channels/458106/feeds.json?api_key=XQ037NVAG71W4PWA&results=2")
	dict = data.json()
	for x in range(1):
		x = int(dict['feeds'][1]['field1'][1])
		y = int(dict['feeds'][1]['field1'][2])
		z = int(dict['feeds'][1]['field1'][3])
		p = dict['feeds'][1]['field1'][5]
		k =  z + y*10 +x*100
	#print("dist " + str(k)+ " dir " + p)
        #direction( p, k)
        if p == 'R':
               while(p != 'M' and p!= 'S'):
                        data = r.get("https://api.thingspeak.com/channels/458106/feeds.json?api_key=XQ037NVAG71W4PWA&results=2")
                        dict = data.json()
                        for x in range(1):
                                x = int(dict['feeds'][1]['field1'][1])
                                y = int(dict['feeds'][1]['field1'][2])
                                z = int(dict['feeds'][1]['field1'][3])
                                p = dict['feeds'][1]['field1'][5]
                                k =  z + y*10 +x*100
                        if p != q:
                                arr.append((p,k))
                                q = p
                                print(arr)
        print("S or M is present")

        if p == 'M':
                print("keep rolling baby")
                sz = len(arr)
                for i in range(1,sz):
                        p_dash = arr[i][0]
                        k_dash = arr[i][1]
                        direction(p_dash,k_dash)
                        if i == sz-2:
                                p = 'S'
                                print("S detected")
                                break
        
        if p == 'S':
                        print("stop mode baby")
                        









                
