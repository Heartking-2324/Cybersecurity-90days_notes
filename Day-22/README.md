# Port Scan Detection using Python

This project demonstrates a simple port scan detection script using Python. The script monitors network traffic and detects any incoming or outgoing port scans.

## Prerequisites

- Python 3.x
- Scapy library (can be installed using `pip install scapy`)

## Installation

1. **Install Scapy**: Open a terminal and run the following command:

   ```bash
   sudo pip install scapy
   ```

2. **Save the Script**: Copy the Python script provided below into a file named `port_scan_detection.py`.

## Usage

1. **Run the Script**: Navigate to the directory where you saved the script and execute it with the following command:

   ```bash
   python port_scan_detection.py
   ```

2. **Monitor Output**: The script will start capturing network traffic and print messages indicating any detected port scans.

## Python Script
 ``` git clone  ```

## Explanation

- **Function `detect_port_scan`**: This function is called for each captured packet. It checks if the packet has a TCP layer and if it contains the SYN or SYN-ACK flags. It then verifies if the destination or source port is less than 1024, which indicates a possible port scan attempt. A message is printed if a port scan is detected.

- **Sniffing Network Traffic**: The `sniff` function from Scapy captures network packets and calls the `detect_port_scan` function for each packet.

## Notes

- **Permissions**: Ensure you have the required permissions to capture network packets. This might require running the script with `sudo` in some environments.

- **Enhancements**: This is a basic implementation. Consider adding additional checks and features to improve accuracy and reliability based on your specific needs.

- **Environment**: The script is suitable for use in Kali Linux or WSL (Windows Subsystem for Linux). Keep the terminal running to monitor network traffic while the script is active.

Feel free to adapt and enhance the script based on your specific requirements and preferences.

---

For further customization and advanced port scan detection techniques, refer to the Scapy documentation and network security resources.
```
