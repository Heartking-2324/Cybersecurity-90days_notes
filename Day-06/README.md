# Day 06: TryHackMe Basic Pentesting

Today, we delved into the Basic Pentesting room on TryHackMe. This room is ideal for beginners to practice fundamental penetration testing skills. You can access the room [here](https://tryhackme.com/r/room/basicpentestingjt).
## Overview

### TryHackMe Platform
We created a new profile on TryHackMe and started with the Basic Pentesting room, which involves a series of challenges designed to teach basic pentesting techniques.

<img src="https://tryhackme-badges.s3.amazonaws.com/Heartking.png" alt="TryHackMe">

### Activities and Learnings

1. **Enumeration**: Used tools to gather information on open ports and services.
2. **Brute Force Attack**: Performed password guessing attacks using Hydra.
3. **Hash Cracking**: Used John the Ripper to decode password hashes.
4. **Service Enumeration**: Identified running services and potential vulnerabilities.

### for finding the severice which the website is working we use nmap for this 
` nmap -sV -vv ip adderess  `
the ouput we got was 

![main ouput of the nmap](https://raw.githubusercontent.com/Heartking-2324/Cybersecurity-90days_notes/main/Day-06/Screenshot%202024-06-13%20183148.png)

### With the help of the nmap we got to known about the sevices the server is using lets look the exploit which the certain service contain 
#### The first which we looked was a Apache 2.8.14 
#### We look for exploit through the tool called searchexploit
###  searchexploit: Allow you to search through exploits and shellcodes using one or more terms from Exploit-DB

![main ouput of the nmap](https://github.com/Heartking-2324/Cybersecurity-90days_notes/blob/main/Day-06/Screenshot%202024-06-13%20183349.png?raw=true)

#### After the apache 2.8.14 then we looked in the OpenSSH 7.2p2 
![](https://github.com/Heartking-2324/Cybersecurity-90days_notes/blob/main/Day-06/Screenshot%202024-06-13%20183515.png?raw=true)

#### In the OpenSSH 7.2p2 we got know the that it is used for the user enumerate and it is done by the linux/remote/40136.py. Then we lets see for any exploit in the python file on the searchexploit 
![](https://github.com/Heartking-2324/Cybersecurity-90days_notes/blob/main/Day-06/Screenshot%202024-06-13%20183606.png?raw=true)

#### Now that we didn't find any proper exploit then we used the gobuster to identify the users present on the server through the tool called gobuster. We the s username listed in the directory called as (directory-list-2.3-medium.txt) through this we got to known about the directory in the web server which contained the users.
#### gobuster: Gobuster is a tool used to brute-force: URIs (directories and files) in web sites, DNS subdomains (with wildcard support), Virtual Host names on target web servers, Open Amazon S3 buckets, Open Google Cloud buckets and TFTP servers.
![](https://github.com/Heartking-2324/Cybersecurity-90days_notes/blob/main/Day-06/Screenshot%202024-06-13%20185216.png?raw=true)
![]()

#### Now after the username we got we will use the tool called enum4linux which is used for the SMB analysis. 
#### SMB Analysis: Tools and techniques for analyzing and exploiting SMB (Server Message Block) protocol vulnerabilities on network shares.
#### enum4linux: A Linux tool for enumerating information from Windows machines via SMB, similar to the functionality of enum.exe. 
In this we will the local user of the web server 
![](https://github.com/Heartking-2324/Cybersecurity-90days_notes/blob/main/Day-06/Screenshot%202024-06-13%20190254.png?raw=true)

#### After a successfull search we got the 2 users reprent in the server. Which was as a local users in web server kay & jan 
![](https://github.com/Heartking-2324/Cybersecurity-90days_notes/blob/main/Day-06/Screenshot%202024-06-13%20191434.png?raw=true)

### So far the important things we got from the all the serach were 
![](https://github.com/Heartking-2324/Cybersecurity-90days_notes/blob/main/Day-06/Screenshot%202024-06-13%20191458.png?raw=true)

#### After this we will brute force the password of the 2 local users present in the server kay & jan with help of the tool called as Hydra. We have used a password list which is already represent in the kali linux 'rockyou.txt'
#### rockyou.txt: A widely-used password dictionary file containing millions of common passwords for use in brute-force attacks and password cracking.
#### Hydra: Hydra is a parallelized login cracker which supports numerous protocols to attack. It is very fast and flexible, and new modules are easy to add. 
![](https://github.com/Heartking-2324/Cybersecurity-90days_notes/blob/main/Day-06/Screenshot%202024-06-13%20192239.png?raw=true)

#### We got our first password of the user jan 
![]()
#### With the help of that we login in the system using the passwords with the command SSH jan@ip address
![](https://github.com/Heartking-2324/Cybersecurity-90days_notes/blob/main/Day-06/Screenshot%202024-06-13%20220030.png?raw=true)

#### With moving in the home/kay where the pass.bak the passwords contained and the we don't have the access where we cannot get directly so we use a tool called as the peas for linux and then we get crack into the root user and get the password of the kay.
![](https://github.com/Heartking-2324/Cybersecurity-90days_notes/blob/main/Day-06/Screenshot%202024-06-13%20220937.png?raw=true)
