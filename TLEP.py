#Introduction
name = input("What is your name? ")
print ("Hello", name.title(), "let's find out your life expectancy.")
print ("To find out your life expectancy, I will need some information from you.")

#Information; should all be a drop down menu
age = input("How old are you? ")
race = input("What is your race? ") 
s = input("What is your gender? M or F") 
loc = input("What is the state of your residence? ")

#Suspense because people like drama
print ("We are going to run an analysis of your answers to provide you with an estimate of your life expectancy.")
print ("This might take a couple of seconds.")

import time
time.sleep(2)
print ("Analyzing...")
time.sleep(3)

#if staement that chooses where age input gets classified
if int(age) < 15:
 a = 13
elif int(age) >= 15 and int(age) < 20:
 a = 15
elif int(age) >= 20 and int(age) < 25:
 a = 20
elif int(age) >= 25 and int(age) < 30:
 a = 25
elif int(age) >= 30 and int(age) < 35:
 a = 30
elif int(age) >= 35 and int(age) < 40:
 a = 35
elif int(age) >= 40 and int(age) < 45:
 a = 40
elif int(age) >= 45 and int(age) < 50:
 a = 45
elif int(age) >= 50 and int(age) < 55:
 a = 50
elif int(age) >= 55 and int(age) < 60:
 a = 55
elif int(age) >= 60 and int(age) < 65:
 a = 60
elif int(age) >= 65 and int(age) < 70:
 a = 65
elif int(age) >= 70 and int(age) < 75:
 a = 70
elif int(age) >= 75 and int(age) < 80:
 a = 75
elif int(age) >= 80 and int(age) < 85:
 a = 80
elif int(age) >= 85 and int(age) < 90:
 a = 85
elif int(age) >= 90 and int(age) < 95:
 a = 90
elif int(age) >= 95 and int(age) < 100:
 a = 95
else:
 a = 100

 #if statement that categorize race input
if race == "black":
 r = "b"
elif race == "white":
 r = "w"
elif race == "hispanic":
 r = "h"
else:
 r = "o"
 
#Dictionary for race,gender,age values; m=male f=female o=ther w=white h=hispanic b=black
le = {
"om13":67,"om15":62.1,"om20":57.3,"om25":52.6,"om30":48,"om35":43.3,"om40":38.7,"om45":34.1,"om50":29.7,"om55":25.6,"om60":21.7,"om65":17.9,"om70":14.4,"om75":11.2,"om80":8.3,"om85":5.9,"om90":4.1,"om95":2.8,"om100":2,
"of13":71.7,"of15":66.8,"of20":61.9,"of25":57,"of30":52.1,"of35":47.3,"of40":42.6,"of45":37.9,"of50":33.3,"of55":28.9,"of60":24.6,"of65":20.5,"of70":16.5,"of75":12.9,"of80":9.7,"of85":6.9,"of90":4.8,"of95":3.3,"of100":2.3,
"wm13":67.3,"wm15":62.3,"wm20":57.5,"wm25":52.8,"wm30":48.2,"wm35":43.5,"wm40":38.8,"wm45":34.3,"wm50":29.9,"wm55":25.7,"wm60":21.7,"wm65":18,"wm70":14.4,"wm75":11.1,"wm80":8.3,"wm85":5.9,"wm90":4,"wm95":2.8,"wm100":2,
"wf13":71.8,"wf15":66.9,"wf20":62,"wf25":57.1,"wf30":52.3,"wf35":47.4,"wf40":42.7,"wf45":38,"wf50":33.4,"wf55":28.9,"wf60":24.6,"wf65":20.4,"wf70":16.5,"wf75":12.9,"wf80":9.7,"wf85":6.9,"wf90":4.8,"wf95":3.2,"wf100":2.3,
"hm13":69.8,"hm15":64.8,"hm20":60,"hm25":55.3,"hm30":50.5,"hm35":45.8,"hm40":41.1,"hm45":36.4,"hm50":31.9,"hm55":27.6,"hm60":23.5,"hm65":19.6,"hm70":15.9,"hm75":12.5,"hm80":9.4,"hm85":6.8,"hm90":4.7,"hm95":3.3,"hm100":2.4,
"hf13":74.8,"hf15":69.9,"hf20":64.9,"hf25":60,"hf30":55.1,"hf35":50.3,"hf40":45.4,"hf45":40.6,"hf50":35.9,"hf55":31.4,"hf60":26.9,"hf65":22.6,"hf70":18.5,"hf75":14.6,"hf80":11.1,"hf85":8.1,"hf90":5.7,"hf95":3.9,"hf100":2.7,
"bm13":63.4,"bm15":58.4,"bm20":53.7,"bm25":49.2,"bm30":44.6,"bm35":40.1,"bm40":35.6,"bm45":31.2,"bm50":27,"bm55":23,"bm60":29.5,"bm65":16.2,"bm70":13.2,"bm75":10.4,"bm80":8,"bm85":6,"bm90":4.5,"bm95":3.4,"bm100":1.6,
"bf13":69.3,"bf15":64.4,"bf20":59.5,"bf25":54.6,"bf30":49.8,"bf35":45.1,"bf40":40.4,"bf45":35.9,"bf50":31.5,"bf55":27.3,"bf60":23.3,"bf65":19.5,"bf70":15.9,"bf75":12.6,"bf80":9.7,"bf85":7.2,"bf90":5.2,"bf95":3.8,"bf100":2.8
}

#Dictionary for state values
sl = {
"AL":75.4,"AK":78.3,"AZ":79.6,"AR":76,"CA":80.8,"CO":80,"CT":80.8,"DE":78.4,"FL":79.4,"GA":77.2,"HI":81.3,"ID":79.5,"IL":79,"IN":77.6,"IA":79.7,"KS":78.7,"KY":76,"LA":75.7,"ME":79.2,"MD":78.8,"MA":80.5,"MI":78.2,"MN":81.1,"MS":75,
"MO":77.5,"MT":78.5,"NE":79.8,"NV":78.1,"NH":80.3,"NJ":80.3,"NM":78.4,"NY":80.5,"NC":77.8,"ND":79.5,"OH":77.8,"OK":75.9,"OR":79.5,"PA":78.5,"RI":79.9,"SC":77,"SD":79.5,"TN":76.3,"TX":78.5,"UT":80.2,"VT":80.5,"VA":79,"WA":79.9,"WV":75.4,"WI":80,"WY":78.3
}

lu = str(r)+str(s.lower())+str(a)
lu1 = le[lu]
af = int(lu1) + int(age)

lul = sl[loc.upper()]

final = (int(af) + int(lul))/2

if final < af:
    print (af)
else:
    print (final)
    print (time)