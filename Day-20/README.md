Day-20 
# We will learn about wifi penetration 

# THIS IS FOR EDUCATIONAL PURPOSE. AFTER FOLLOWING THE STEP GIVEN BELOW IF ANY HAPPENS THIS PAGE & OWNER NOT RESPONSIBLE! 

#### Lets get it started 

For the first Step in the we need a [WIFI ADAPTER](https://amzn.in/d/08289vCi). This is the adapter which i have in my buget if you have no limit to your budget then you may try for this[Alfa Network Adapter](https://amzn.in/d/06gaCZPK). 

### After this we have some important configuration changes to be made in VB 
- Connect your adapter to you system
- Go to Virtual box > To your kali settings > USB
- After selecting USB > add new usb which has '+' icon  > select your adapter
- click 'ok'

### Commands for further hacking 
- To check the wifi adapter in kali linux 
``` lsusb  ```
- to check whether the adapter is on 'monitoring mode' or 'managing mode'
``` iwconfig ```
- to convert it from managable to monitoring mode
``` sudo airmon-ng start wlan0 ```
- After turning on the monitoring mode we will search for the wifi near us
``` sudo airodump-ng  ```
- after seeing the wifi near us we have to check the power it has if the networking you want to target is above 30 then only select that network to attack or else get closer to network.

### Now we have all set and want to attack a wifi! :)
Let's get started we will use tool called "wifite". This tool is used for the automated scripted attack which it will perform.
#### Working
- It first send deauthn. packets to the router which disconnects all the users.
- When the userrs try to connect to the router again it captures the targets packets via wireshark and generate a .pcap file
- Then the file which will be generate which will try to a common wordlist on the wifi to guess the password/ brute force the password
- After successfull burte force you will recive the password and you can connect it successfully

### Now lets attack 
1. Initiate
``` sudo wifiti ```
