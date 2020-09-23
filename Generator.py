import random #line:2:import random
import string #line:3:import string
import pathlib #line:4:import pathlib
import requests ,os ,sys ,random ,os .path ,time #line:5:import requests, os, sys, random, os.path, time
import colorama #line:6:import colorama
from colorama import Fore ,init ,Style ,Back #line:7:from colorama import Fore, init, Style, Back
count =0 #line:9:count = 0
current_path =os .path .dirname (os .path .realpath (__file__ ))#line:10:current_path = os.path.dirname(os.path.realpath(__file__))
os .system ("cls")#line:11:os.system("cls")
cantidad =input ("How many giftcards want to generate: ")#line:13:cantidad = input("How many giftcards want to generate: ")
while (int (count )<int (cantidad )):#line:15:while(int(count)<int(cantidad)):
	Generated =random .choice (string .ascii_uppercase ).upper ()+''.join (random .choice (string .ascii_uppercase +string .digits ).upper ()for _OOOO0OOOO0OOO0OOO in range (4 ))+"-"+random .choice (string .ascii_uppercase ).upper ()+''.join (random .choice (string .ascii_uppercase +string .digits )for _O00O00000OOOOOOO0 in range (4 ))+"-"+''.join (random .choice (string .ascii_uppercase +string .digits )for _O0O00OOOO0O0O000O in range (5 ))+"-"+''.join (random .choice (string .ascii_uppercase +string .digits )for _OO00OO0OOO0OOOO0O in range (5 ))#line:16:Generated = random.choice(string.ascii_uppercase).upper()+''.join(random.choice(string.ascii_uppercase + string.digits).upper() for _ in range(4))+"-"+random.choice(string.ascii_uppercase).upper()+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))+"-"+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))+"-"+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
	f =open (current_path +"/"+str ("GiftCards")+str ("")+".txt","a")#line:17:f= open(current_path+"/"+str("GiftCards")+str("")+".txt","a")
	f .write (Generated +"\n")#line:18:f.write(Generated+"\n")
	print ("Generated code: "+Generated )#line:19:print("Generated code: "+ Generated)
	count +=1 #line:20:count+=1
input ("\nCodes have been generated & saved!\nPress enter to exit.")#line:21:input("\nCodes have been generated & saved!\nPress enter to exit.")
pass #line:22:pass
