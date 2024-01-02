from requests import get
import requests
from requests.exceptions import Timeout
import socket
import time
import argparse
import sys

## Mute Warnings
import urllib3
urllib3.disable_warnings()

## Clear Terminal
import os
os.system('cls' if os.name == 'nt' else 'clear')

#Coloured output
class ColoredOutput:
    def __init__(self, color_code):
        self.color_code = color_code
        self.original_stdout = sys.stdout

    def write(self, message):
        self.original_stdout.write(f"{self.color_code}{message}\033[0m")

    def flush(self):
        self.original_stdout.flush()


sys.stdout = ColoredOutput('\033[92m')

# Title
title = r"""
_____________________________________________________/\\\\\\\\\\\___/\\\\\\\\\\\\\___        
 ____________________________________________________\/////\\\///___\/\\\/////////\\\_       
  ___/\\\\\\\\\____/\\\___________________/\\\\\\\\_______\/\\\______\/\\\_______\/\\\_      
   __/\\\/////\\\__\///____/\\/\\\\\\_____/\\\////\\\______\/\\\______\/\\\\\\\\\\\\\/__     
    _\/\\\\\\\\\\____/\\\__\/\\\////\\\___\//\\\\\\\\\______\/\\\______\/\\\/////////____    
     _\/\\\//////____\/\\\__\/\\\__\//\\\___\///////\\\______\/\\\______\/\\\_____________   
      _\/\\\__________\/\\\__\/\\\___\/\\\___/\\_____\\\______\/\\\______\/\\\_____________  
       _\/\\\__________\/\\\__\/\\\___\/\\\__\//\\\\\\\\____/\\\\\\\\\\\__\/\\\_____________ 
        _\///___________\///___\///____\///____\////////____\///////////___\///______________
"""
print(title)
sys.stdout = sys.__stdout__

##Arg Parser
parser = argparse.ArgumentParser(description='pingIP')
parser.add_argument(action="store", dest='hostname')
parser.add_argument('-n', action="store", dest='pingamount', default=8, help="Number of times to ping the server; default is 8 times")
parser.add_argument('-t', action="store", dest='timeout', default=5, help="Duration before ping timesout; default is 5 seconds")
parser.add_argument('-q', action="store_true", dest="quickmode", default=False, help="Aims to speed up the processing by enabling streamlined responses, disables SSL Certificate verification and disabling connection checks - Warning may lead to crashes / errors; default False")
parser.add_argument('-v', action="store_true", dest='verify', default=False, help="Verifies SSL Certificate before pinging websites; highly recommended if pinging potentially dangerous sites but does negatively affect overall speed ratings; default False")
parser.add_argument('--sl', action="store_true", dest='streamlined', default=False, help="Streamlines outputs; default False")
parser.add_argument('--ver', action="version",version='You are running %(prog)s Version 1.0')
args = parser.parse_args()

# arg variables to program variables
hostname = args.hostname
pingamount = int(args.pingamount)
streamlined = args.streamlined
timeout = float(args.timeout)
quickmode = args.quickmode
verification = args.verify

if quickmode == True:
    streamlined = True
    verification = False

## Program variables
avgtimetaken = []
avgserverresponse = []
failCon = 0
http_status_codes = {
    100: "Continue: The server has received the initial part of the request and the client should continue with the request.",
    200: "OK: The request was successful.",
    201: "Created: The request has been fulfilled, resulting in the creation of a new resource.",
    204: "No Content: The server successfully processed the request but there is no content to send in the response.",
    301: "Moved Permanently: The requested resource has been permanently moved to a new location.",
    302: "Found (or 307 Temporary Redirect): The requested resource has been temporarily moved to another location.",
    304: "Not Modified: The client's cached version of the requested resource is still valid.",
    400: "Bad Request: The server could not understand the request.",
    401: "Unauthorized: Authentication is required and has failed, or the user has not been authenticated.",
    403: "Forbidden: The server understood the request, but it refuses to authorize it.",
    404: "Not Found: The requested resource could not be found on the server.",
    500: "Internal Server Error: A generic error message returned when an unexpected condition was encountered by the server.",
    501: "Not Implemented: The server does not support the functionality required to fulfill the request.",
    503: "Service Unavailable: The server is not ready to handle the request. Common causes include maintenance, temporary overloading, or server issues."
}

# Example usage


## Host/User
try:
    if quickmode == False:
        ## Parse hostname into valid ip
        try:
            if "192" in hostname or "172" in hostname:
                raise ValueError("ERROR WRONG HOSTNAME OR IP")

            print("Establishing host IP...")
            hostip = socket.gethostbyname(hostname)
            
            time.sleep(0.2)
            
        except Exception as error:
            print("Error establishing Host IP")
            sys.exit(0)

   
        ## Determine local user outbound IP
        try:
            print("Establishing user IP...")
            userip = get('https://api.ipify.org').text

        except:
            userip = "System"

    hostname = "https://"+hostname

    ##Main Ping
    try:
        if quickmode == False:
            ##Test base connection to server - can it be reached??
            for i in range(0,4):
                print(f"Connecting to {hostname.replace('https://','')} @ {hostip} from {userip}{'.' * i}                 ", end="\r")
                time.sleep(0.2)
            
            response = requests.get(hostname, timeout=10, verify=verification)

            if response.status_code != "":
                print("HOST FOUND                                                                                           ")
                time.sleep(0.1)

    except Timeout:
        print("HOST TIMED OUT                                                                                                ")
        sys.exit(0)

    except Exception as error:
        print (error)
        print("SSL ERROR PLEASE TRY AGAIN                                                                                    ")
        sys.exit(0)

    ##Ping host and record time taken
    for i in range(pingamount):
        try:
            start = time.time()
            response = requests.get(hostname, timeout=timeout, verify=verification)
            end = time.time()
            timetaken = (round(end-start,3)*100)
            avgtimetaken.append(timetaken)
            avgserverresponse.append(response.status_code)

            if streamlined == False and quickmode == False:
                print(f"Pinged {hostip} from {userip} with response code {response.status_code}. Time taken = {'{0:.2f}'.format(timetaken)}ms")
        
            if streamlined == True or quickmode == True:
                print(f"Response {response.status_code}: {'{0:.2f}'.format(timetaken)}ms")

        except Timeout:
            print("Host timed out")
            failCon += 1
            continue

        except Exception as error:
            #print (error)
            print("ERROR CONNECTION FAILED")
            failCon += 1
            


    print("\n")




    # Final Details
    print(f"Sent {pingamount-failCon}/{pingamount} pings {'{0}'.format(((pingamount-failCon)/pingamount)*100)}%")
    if len(avgtimetaken) != 0:
        average = round((sum(avgtimetaken) / len(avgtimetaken)),3)#
        minimum = min(avgtimetaken)
        maximum = max(avgtimetaken)
        print(f"Minimum = {'{0:.2f}'.format(minimum)}ms, Average = {'{0:.2f}'.format(average)}ms, Maximum = {'{0:.2f}'.format(maximum)}ms")
    if len(avgserverresponse) != 0 and streamlined == False:
        avgservercode = max(set(avgserverresponse), key=avgserverresponse.count)
        print(f"Average server response {avgservercode} - {http_status_codes[avgservercode]}")


except KeyboardInterrupt as error:
    print("PROCESS HALTED - EXITING")
    sys.exit(0)