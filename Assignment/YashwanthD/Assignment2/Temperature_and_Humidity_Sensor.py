import random
rdm = 5
while(True):
 a=random.randint(10,100)
 b=random.randint(10,100)
 if(a>30 and b<70):
 print("HIGH TEMPERATURE AND HUMIDITY OF:",a,b,"%", "ALARM IS ON")
 elif(a<30 and b>70):
 print("NORMAL TEMPERATURE AND HUMIDITY OF:",a,b,"%","ALARM IS OFF")
 if(rdm<70):
 rdm=rdm+1
 random
 else:
 break
