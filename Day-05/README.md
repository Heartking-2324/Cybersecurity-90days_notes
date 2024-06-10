# Day 05: Exploring TryHackMe and Basic Penetration Testing

## Introduction to TryHackMe Platform

Today, we delved into the exciting world of TryHackMe, a platform designed to enhance cybersecurity skills through interactive learning. We began by creating a new profile on TryHackMe, which will be our hub for various cybersecurity challenges and learning modules.

[tryHackMe Profile Setup](https://tryhackme.com/p/Heartking)

## Getting Started

### Creating a New Profile

1. **Sign Up**: We started by signing up for a TryHackMe account. This was a straightforward process requiring an email and a password.
2. **Profile Setup**: After registration, we set up our profile, filling out necessary details and preferences.

### Exploring the Beginner Level

We explored the beginner-level challenges, focusing on the "Basic Penetration Testing" room. This module is designed to teach fundamental penetration testing skills through hands-on exercises.

![TryHackMe Beginner Level](https://www.thedutchhacker.com/wp-content/uploads/2021/07/Basic-Pentesting-tryhackme.png)

## OWASP Top Ten

As part of our learning, we reviewed the OWASP Top Ten security risks. Here is a brief explanation of each:

1. **Broken Access Control**: When users can access data or perform actions they shouldn't be allowed to.
2. **Cryptographic Failures**: Inadequate protection of sensitive data through weak encryption or poor key management.
3. **Injection**: When malicious data tricks the app into executing unintended commands.
4. **Insecure Design**: Lack of proper security measures in the design phase, leading to vulnerabilities.
5. **Security Misconfiguration**: Incorrectly configured security settings that expose the system to attacks.
6. **Vulnerable and Outdated Components**: Using software with known vulnerabilities due to outdated versions.
7. **Identification and Authentication Failures**: Weaknesses in the login systems that allow unauthorized access.
8. **Software and Data Integrity Failures**: Using untrusted software or updates that compromise data integrity.
9. **Security Logging and Monitoring Failures**: Inadequate logging and monitoring, making it hard to detect breaches.
10. **Server-Side Request Forgery (SSRF)**: When an attacker tricks the server into accessing internal resources.

## New Tools and Concepts

### SearchSploit

We were introduced to **SearchSploit**, a command-line tool included in Kali Linux that helps find known exploits and vulnerabilities for software. It is part of the Exploit Database (exploit-db.com) and is incredibly useful for penetration testing.

![SearchSploit in Action](https://www.exploit-db.com/images/searchsploit-v3.png)

### CVE and CVSS

We explored the **Common Vulnerabilities and Exposures (CVE)** system and the **Common Vulnerability Scoring System (CVSS)** on the [NIST website](https://nvd.nist.gov). CVE provides a standardized identifier for known vulnerabilities, while CVSS offers a scoring system to assess their severity.

![CVE and CVSS Exploration](https://bit-sentinel.com/wp-content/uploads/2019/05/cvss2-free-calculator-online.png)

### Exploit Database

Another valuable resource we discovered is the [Exploit Database](https://www.exploit-db.com), which houses a vast collection of exploits and vulnerabilities for various software.

## Basic Penetration Testing Skills

To prepare for the "Basic Penetration Testing" challenge, we learned about three key techniques:

1. **Brute Force**: Attempting multiple passwords or keys to gain unauthorized access.
2. **Hash Cracking**: Decoding hashed passwords to obtain the original text.
3. **Service Enumeration**: Identifying services running on a target system to find potential vulnerabilities.

## Practical Exercises

We practiced each of these techniques through hands-on exercises, gaining a deeper understanding of how they are applied in real-world scenarios.

## Introducing ngrok

### Downloading ngrok

We learned about **ngrok**, a tool that creates secure tunnels to localhost, making it accessible over the internet. Here's how to get started:

1. **Download ngrok**: Visit [ngrok's download page](https://ngrok.com/download) and download the appropriate version for your operating system.
2. **Install ngrok**: Follow the installation instructions provided on the website.

### Creating and Deploying index.html

We created a simple `index.html` file with the text "I'm from the ngrok". Here is the code for the HTML file:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ngrok Test</title>
</head>
<body>
    <h1>I'm from the ngrok</h1>
</body>
</html>
```

### Deploying with ngrok
#### 1. Run a Local Server: Start a local server using a command like python -m http.server 8080.
#### 2. Expose the Server: Use ngrok to create a tunnel to the local server with the command ngrok http 8080.
#### 3. Access via Internet: ngrok provides a public URL that you can use to access your local server from the internet.

## Special Mention
Today, I received a gift as a reward for answering a question correctly during the internship. Details will be shared tomorrow—stay tuned!

