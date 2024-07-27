# Day-21 Wi-Fi Penetration Testing-2

## Overview

This document outlines a manual approach to performing a wireless penetration test. Unlike automated tools such as `wifite`, this guide focuses on detailed, hands-on methodologies for evaluating the security of a Wi-Fi network. Wireless penetration testing involves simulating attacks to identify vulnerabilities and strengthen network defenses.

## Table of Contents

1. [What Is A Wireless Penetration Test?](#what-is-a-wireless-penetration-test)
2. [Goals of a Wireless Pen Test](#goals-of-a-wireless-pen-test)
3. [Steps to Performing a Wireless Penetration Test](#steps-to-performing-a-wireless-penetration-test)
    - [Step 1: Wireless Reconnaissance](#step-1-wireless-reconnaissance)
    - [Step 2: Identify Wireless Networks](#step-2-identify-wireless-networks)
    - [Step 3: Vulnerability Research](#step-3-vulnerability-research)
    - [Step 4: Exploitation](#step-4-exploitation)
    - [Step 5: Reporting](#step-5-reporting)
    - [Step 6: Remediation & Security Controls](#step-6-remediation--security-controls)
4. [Other Wireless Attacks](#other-wireless-attacks)
5. [Conclusion](#conclusion)

## What Is A Wireless Penetration Test?

Wireless penetration testing involves manually identifying and examining connections between devices connected to a Wi-Fi network, such as laptops, tablets, smartphones, and IoT devices. This type of testing is performed on-site, as proximity to the wireless signal is necessary for effective analysis.

## Goals of a Wireless Pen Test

The goal of a wireless penetration test is to identify and exploit vulnerabilities manually, focusing on weaknesses that are most easily exploited. This approach contrasts with automated tools like `wifite`, which perform similar tasks but with less granular control over the testing process.

## Steps to Performing a Wireless Penetration Test

### Step 1: Wireless Reconnaissance

**Objective:** Manually gather information about available wireless networks.

**Tools Needed:**
- Car or transportation vehicle
- Laptop with a Wi-Fi antenna
- Wireless network adapter
- Packet capture and analysis software

**Process:**
- Conduct War Driving to manually sniff out Wi-Fi signals.
- Collect encrypted information protected by WPA2 using your setup, which includes manual configuration and monitoring.

### Step 2: Identify Wireless Networks

**Objective:** Manually scan and identify wireless networks.

**Tools:**
- `airodump-ng`

**Process:**
- Set your wireless card to "monitor" mode manually.
- Use `airodump-ng` to scan traffic on different channels and specify channels manually to streamline data collection.

### Step 3: Vulnerability Research

**Objective:** Manually identify vulnerabilities, focusing on the 4-way handshake process.

**Process:**
- Capture the 4-way handshake by manually initiating and monitoring traffic.
- Analyze the captured data to identify vulnerabilities in the pre-shared key manually, rather than relying on automated tools.

### Step 4: Exploitation

**Objective:** Manually exploit identified vulnerabilities to gain unauthorized access.

**Tools:**
- Aircrack-ng suite

**Process:**
- Manually de-authenticate a legitimate client to capture the handshake.
- Use Aircrack-ng to manually crack the captured handshake and extract the password, rather than using automated scripts.

### Step 5: Reporting

**Objective:** Document the penetration testing process and findings manually.

**Process:**
- Create a detailed report that includes:
  - Executive summary
  - Technical risks and vulnerabilities
  - Detailed exploitation process
  - Recommendations for mitigation
- Ensure all findings are documented comprehensively for manual review.

### Step 6: Remediation & Security Controls

**Objective:** Implement manual security controls to prevent future vulnerabilities.

**Recommendations:**
- Enable MAC filtering and Network Access Control (NAC) solutions.
- Consider deploying wireless honeypots to detect and analyze unauthorized access attempts.

## Other Wireless Attacks

In addition to manual exploitation of the 4-way handshake, other manual attacks include deploying rogue access points to intercept network traffic. This method involves manually overpowering legitimate access points and requires significant hands-on intervention.

## Conclusion

This guide provides a manual approach to wireless penetration testing, emphasizing hands-on techniques and detailed methodologies. Unlike automated tools such as `wifite`, this approach offers greater control and understanding of each step in the testing process. By following these steps, you can effectively assess and enhance the security of your Wi-Fi network.

For a more automated approach, tools like `wifite` are available but offer less granular control over the testing process.

---
