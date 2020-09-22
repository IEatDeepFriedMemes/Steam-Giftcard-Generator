#Giftcard Generator
import random
import string
import pathlib
import requests, os, sys, random, os.path, time
import colorama
from colorama import Fore, init, Style, Back

count = 0
current_path = os.path.dirname(os.path.realpath(__file__))
os.system("cls")
	
cantidad = input("How many giftcards want to generate: ")

while(int(count)<int(cantidad)):
	Generated = random.choice(string.ascii_uppercase).upper()+''.join(random.choice(string.ascii_uppercase + string.digits).upper() for _ in range(4))+"-"+random.choice(string.ascii_uppercase).upper()+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))+"-"+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))+"-"+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
	f= open(current_path+"/"+str("GiftCards")+str("")+".txt","a") 
	f.write(Generated+"\n")
	print("Generated code: "+ Generated)
	count+=1
input("\nCodes have been generated & saved!\nPress enter to exit.")
pass
