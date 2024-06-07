# Cyber Security Internship Diary

## Day 4: Nmap and Network Scanning

### Today, we have a very interesting topic to discuss!

In today's session, we delved deep into network scanning using Nmap. We covered a variety of topics, explored essential commands, and even performed a practical example on `keralauniversity.ac.in`.

### Topics Covered

#### 1. **Nmap**

**Nmap** (Network Mapper) is a powerful open-source tool used for network discovery and security auditing. It helps in discovering hosts and services on a computer network.

#### 2. **Recon**

Reconnaissance involves gathering information about a target network or system. This is the first step in ethical hacking.

#### 3. **OSINT**

**Open Source Intelligence (OSINT)** involves collecting data from publicly available sources to gather information on a target.

#### 4. **IDS and IPS**

- **IDS (Intrusion Detection System):** Monitors network traffic for suspicious activity.
- **IPS (Intrusion Prevention System):** Monitors and takes action to prevent detected threats.

#### 5. **Why Not to Ping**

Pinging a website can sometimes alert IDS/IPS systems, leading to blocking or tracking of your IP address. Using more subtle methods can avoid detection.

### Practical Example

We used Nmap to scan `keralauniversity.ac.in` with the following command:

```sh
sudo nmap -Pn -p21,22,53,80,81,433,800,8080 -sV -oN test.txt keralauniversity.ac.in
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-06-07 10:39 EDT
NSE: Loaded 46 scripts for scanning.
Initiating Parallel DNS resolution of 1 host. at 10:39
Completed Parallel DNS resolution of 1 host. at 10:39, 0.01s elapsed
Initiating SYN Stealth Scan at 10:39
Scanning keralauniversity.ac.in (14.139.185.78) [8 ports]
Discovered open port 80/tcp on 14.139.185.78
Completed SYN Stealth Scan at 10:39, 2.27s elapsed (8 total ports)
Initiating Service scan at 10:39
Scanning 1 service on keralauniversity.ac.in (14.139.185.78)
Completed Service scan at 10:39, 6.31s elapsed (1 service on 1 host)
NSE: Script scanning 14.139.185.78.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 10:39
Completed NSE at 10:39, 23.02s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 10:39
Completed NSE at 10:39, 0.50s elapsed
Nmap scan report for keralauniversity.ac.in (14.139.185.78)
Host is up, received user-set (0.11s latency).
Scanned at 2024-06-07 10:39:15 EDT for 32s

PORT     STATE    SERVICE     REASON         VERSION
21/tcp   filtered ftp         no-response
22/tcp   filtered ssh         no-response
53/tcp   filtered domain      no-response
80/tcp   open     http        syn-ack ttl 64 Apache httpd 2.4.6 ((CentOS) OpenSSL/1.0.2k-fips mod_fcgid/2.3.9 mod_wsgi/3.4 Python/2.7.5 PHP/7.2.27)
81/tcp   filtered hosts2-ns   no-response
433/tcp  filtered nnsp        no-response
800/tcp  filtered mdbs_daemon no-response
8080/tcp filtered http-proxy  no-response

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 33.00 seconds
           Raw packets sent: 16 (704B) | Rcvd: 2 (88B)
```
## Detailed Analysis
### Accessing Vulnerable Websites
You can use websites like ```testphp.vulnweb.com```to perform various attacks for learning purposes.

### Key Concepts Explained
#### 1. *Recon*
Definition: Gathering preliminary data on a target.
Example: Using Nmap to identify open ports.

#### 2. *OSINT*:
Definition: Collecting publicly available information.
Example: Using Google to find information on a target.

#### 3. *IDS and IPS*:
IDS Example: Snort.
IPS Example: Cisco Firepower.

#### 4. *Why Not to Ping*:
Reason: Alerts IDS/IPS systems.
Diagram:
![Ping vs. TCP Explanation](https://i.sstatic.net/kudkw.png)

#### 5. *Service Detection Flowchart*: 
```
	       nmap
	 	|
	       / \
     id-service   TCP/UDP
	|	     |
     version	  state of
     deatils 	    port
	|	     |
	|	     |-open 
	|	     |-close
	|	     |-filter
	--------------
	       |
	vulnerabilites
	       |
	    exploit
```

#### 6. *Scanning*:
![Scanning](https://www.thesecuritybuddy.com/wordpress/bdr/uploads/2020/02/Nmap_20.jpg)
View headers sent by the server.
#### 7. *Wafw00f*:
Used to identify the Firewall service used by the website 
![example](https://miloserdov.org/wp-content/uploads/2021/07/wafw00f.png)

from this 👇 also you can find the information about the website which we gather from the 

``` Inspect -> Network -> Status -> Version -> Request Header -> Response Header ```
