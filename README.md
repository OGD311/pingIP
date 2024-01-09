# pingIP
Command Line python code to ping webservers with greater statistics, functionality and speed compared to inbuilt ping
pingIP varies from the inbuilt ping function because it requests the entire webserver, meaning the server response as well as the content is recorded

![pingIP](https://github.com/OGD311/pingIP/assets/114223604/0fcf6843-eda5-4b2d-91ca-928abbf2920e)


## Installation
First things first clone the github repository:
git clone https://github.com/OGD311/pingIP <br>
Then using a terminal navigate to the folder it has been cloned to and run either:
pip install -r requirements.txt <br>
Or:
init (Which calls the init.bat file) <br>
Once thats complete now you can finally run pingIP!

## Usage
### Default Use
To use pingIP in its default state with no changes simply run
<code>python pingIP.py 'hostname'</code><br>
This will first establish whether the server can be reached, before then pinging it 8 times to establish latency and connectivity. <br>
Finally it will output:
* Number of successful packets sent
* Minimum, Average and Maximum timings
* Average response code and its meaning

For example: <br>
<code>python pingIP.py google.com</code> <br>
Returns: <br>
```
Establishing host IP...<br>
Establishing user IP...<br>
HOST FOUND<br>
Pinged 142.250.178.14 from 'YOUR IP' with response code 200. Time taken = 29.10ms<br>
Pinged 142.250.178.14 from 'YOUR IP' with response code 200. Time taken = 30.40ms<br>
Pinged 142.250.178.14 from 'YOUR IP' with response code 200. Time taken = 33.10ms<br>
Pinged 142.250.178.14 from 'YOUR IP' with response code 200. Time taken = 29.50ms<br>
Pinged 142.250.178.14 from 'YOUR IP' with response code 200. Time taken = 29.20ms<br>
Pinged 142.250.178.14 from 'YOUR IP' with response code 200. Time taken = 28.80ms<br>
Pinged 142.250.178.14 from 'YOUR IP' with response code 200. Time taken = 28.10ms<br>
Pinged 142.250.178.14 from 'YOUR IP' with response code 200. Time taken = 28.40ms<br>

Sent 8/8 pings 100.0%<br>
Minimum = 28.10ms, Average = 29.57ms, Maximum = 33.10ms<br>
Average server response 200 - OK: The request was successful.<br>
```

### Advanced Use
pingIP comes inbuilt with several functions to change the behaviour of how the program functions. These are: <br>

* -n  PINGAMOUNT
* -t  TIMEOUT
* -q  QUICKMODE
* -v  VERIFICATION
* --sl  STREAMLINE

## Examples
### -n PINGAMOUNT
Number of times to ping the server; default is 8 times <br>
<code>python pingIP.py google.com -n 4</code> <br>
Output: <br>
```
Establishing host IP...<br>
Establishing user IP...<br>
HOST FOUND<br>
Pinged 142.250.178.14 from 'YOUR IP' with response code 200. Time taken = 51.70ms<br>
Pinged 142.250.178.14 from 'YOUR IP' with response code 200. Time taken = 39.40ms<br>
Pinged 142.250.178.14 from 'YOUR IP' with response code 200. Time taken = 32.80ms<br>
Pinged 142.250.178.14 from 'YOUR IP' with response code 200. Time taken = 35.10ms<br>

Sent 4/4 pings 100.0%<br>
Minimum = 32.80ms, Average = 39.75ms, Maximum = 51.70ms<br>

Average server response 200 - OK: The request was successful.<br>
```

### -t TIMEOUT
Duration before ping timesout measured in seconds; default is 5 seconds <br>
<code>python pingIP.py google.com -t 0.01 -n 4</code><br>
> [!NOTE]
> I've used -t 0.01 (10 ms)  in order to force the "Host timed out" output as a demonstration
 
Output: <br>
```
Establishing host IP...<br>
Establishing user IP...<br>
HOST FOUND<br>
Host timed out<br>
Host timed out<br>
Host timed out<br>
Host timed out<br>

Sent 0/4 pings 0.0%<br>
```
> [!NOTE]
> No statistics are output here because there are none to record; if 1 or more are successful then there will be statistics outputted


### -q QUICKMODE
Aims to speed up the processing by enabling streamlined responses, disables SSL Certificate verification and disabling connection checks; default False <br>
<code>python pingIP.py google.com -n 4 -q</code><br>
Outputs: <br>
```
Response 200: 36.00ms<br>
Response 200: 26.40ms<br>
Response 200: 27.10ms<br>
Response 200: 25.30ms<br>

Sent 4/4 pings 100.0%<br>
Minimum = 25.30ms, Average = 28.70ms, Maximum = 36.00ms<br>
```
>[!CAUTION]
> Activating quickmode may lead to unknown crashes / errors and can make your computer vulnerable to Man in the Middle Attacks amongst other HTTP vulnerabilities

### -v VERIFICATION
Verifies SSL Certificate before pinging websites; highly recommend using this if pinging potentially dangerous sites but does negatively affect overall speed ratings; default False <br>
<code>python PingIP.py google.com -n 4 -v</code><br>
Outputs: <br>
```
Establishing host IP...<br>
Establishing user IP...<br>
HOST FOUND<br>
Pinged 142.250.179.238 from 'YOUR IP' with response code 200. Time taken = 62.50ms<br>
Pinged 142.250.179.238 from 'YOUR IP' with response code 200. Time taken = 60.90ms<br>
Pinged 142.250.179.238 from 'YOUR IP' with response code 200. Time taken = 62.40ms<br>
Pinged 142.250.179.238 from 'YOUR IP' with response code 200. Time taken = 60.30ms<br>

Sent 4/4 pings 100.0%<br>
Minimum = 60.30ms, Average = 61.52ms, Maximum = 62.50ms<br>
Average server response 200 - OK: The request was successful.<br>
```
>[!CAUTION]
> Deactivating SSL Certificate Verification can make your computer vulnerable to Man in the Middle Attacks amongst other HTTP vulnerabilities

### -sl STREAMLINE
Streamlines outputs, only showing number of successful pings and speed statistics; default False <br>
<code>python PingIP.py google.com -n 4 --sl</code><br>
Outputs: <br>
```
Establishing host IP...<br>
Establishing user IP...<br>
HOST FOUND<br>
Response 200: 26.00ms<br>
Response 200: 25.30ms<br>
Response 200: 28.00ms<br>
Response 200: 28.60ms<br>

Sent 4/4 pings 100.0%<br>
Minimum = 25.30ms, Average = 26.98ms, Maximum = 28.60ms<br>
```

## Speed Comparisons
Average Speed of these different settings <br>
<code>python pingIP.py google.com</code> <br>
|Number of pings| Quickmode OFF Verify ON  | Quickmode OFF Verify OFF | Quickmode ON | Streamlined ON |
|---------------|-------------------------| ------------------------ |--------------|----------------|
| -n | -v | | -q | --sl |
| 4 | 62.45ms | 28.35ms | 26.60ms | 28.93ms |
| 8 | 63.84ms | 29.24ms | 27.79 | 28.62ms |
| 16 | 63.96ms | 31.94ms | 29.61ms | 30.50ms |

>[!NOTE]
>Obviously these numbers vary by machine, internet speed, etc but they show the speed of quickmode and disabling verify.


## Future Features
These are features I would like to add but are currently WIP / I lack the knowledge on how to implement: <br>
* Ability to change the size of data sent, similar to how the current windows 'ping' works



