# Day-08: Learning to host a webiste 

## Overview

This project demonstrates an e-commerce website that sells huge money bills. It includes a sleek design with a white-blue color scheme, backend functionality to log user IP addresses, and basic user authentication with a login and registration page.

## Features

1. **Stylish Design:** The website features a white-blue color combination and is designed to accommodate images of the products.
2. **IP Logging:** The backend captures the IP address of users when they interact with the website.
3. **User Authentication:** Includes a login and registration system to manage user access.

## Getting Started

### Prerequisites

- Apache Web Server
- Ngrok
- Basic understanding of HTML, CSS, and PHP

### Installation

1. **Download and Install Apache:**

```  bash
   sudo apt update
   sudo apt install apache2
   sudo systemctl start apache2
   sudo systemctl enable apache2
   sudo cp -r ~/Desktop/hidden_formfield/* /var/www/html/
   cd /var/www/html
   ls -la
   sudo systemctl start apache2
   ./ngrok http 80
```
### Using Ngrok
Ngrok is a tool that creates secure tunnels to your localhost, enabling you to expose your local server to the internet. Here's how to use it:
Download Ngrok:
Download ngrok from ngrok.com.
Use the public URL provided by ngrok to access your local server.

##John the Ripper
John the Ripper is a popular password cracking tool included in Kali Linux. It is used to detect weak passwords and perform brute force attacks to crack them.

###Usage
Basic Command:

#### bash

``` john --wordlist=/usr/share/wordlists/rockyou.txt hashed_passwords.txt ```

This command uses the wordlist rockyou.txt to crack the passwords in hashed_passwords.txt.

#### Features:
Supports various encryption technologies
Highly configurable and extensible
Can be used in conjunction with other tools for more effective penetration testing
