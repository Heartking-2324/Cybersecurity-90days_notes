# Day 30: Malicious Bash Script for Identifying Next Commands After Finding Open Ports

## Overview

This script uses Rustscan to find open ports on a target IP and suggests the next appropriate command based on the port found. This script can help automate the process of identifying the next steps in network reconnaissance.

## Script Usage

### Prerequisites

- Rustscan must be installed and accessible from your environment. To verify Rustscan installation:
  ```bash
  rustscan --version
  ```

### Running the Script

1. **Save the Script**

   Save the following script to a file, e.g., `scan_and_exploit.sh`:

    ```bash
    #!/bin/bash

    # Function to check for open ports
    check_ports() {
        target_ip=$1
        echo "Checking for open ports on $target_ip..."

        # Use Rustscan to scan for open ports
        open_ports=$(rustscan -a $target_ip -r 1-65535 -u 5000 2>/dev/null | grep "Open")

        # Check if any open ports were found
        if [ -n "$open_ports" ]; then
            echo "Open ports found:"
            echo "$open_ports"

            # Extract and process open ports
            echo "$open_ports" | while read -r line; do
                port=$(echo "$line" | awk '{print $4}')
                echo "Processing port: $port"

                # Identify the next command based on the port
                case $port in
                    22)
                        echo "Next command: ssh <username>@$target_ip"
                        ;;
                    80)
                        echo "Next command: wget http://$target_ip"
                        ;;
                    443)
                        echo "Next command: curl https://$target_ip"
                        ;;
                    8080)
                        echo "Next command: nmap -sC -sV $target_ip"
                        ;;
                    21)
                        echo "Next command: ftp $target_ip"
                        ;;
                    25)
                        echo "Next command: telnet $target_ip 25"
                        ;;
                    110)
                        echo "Next command: telnet $target_ip 110"
                        ;;
                    143)
                        echo "Next command: telnet $target_ip 143"
                        ;;
                    3306)
                        echo "Next command: mysql -h $target_ip -u <username> -p"
                        ;;
                    3389)
                        echo "Next command: rdesktop $target_ip"
                        ;;
                    5900)
                        echo "Next command: vncviewer $target_ip"
                        ;;
                    8081)
                        echo "Next command: nmap -sC -sV $target_ip -p 8081"
                        ;;
                    8888)
                        echo "Next command: curl http://$target_ip:8888"
                        ;;
                    9200)
                        echo "Next command: curl -X GET http://$target_ip:9200"
                        ;;
                    *)
                        echo "Port $port is open. Please manually investigate."
                        ;;
                esac
            done
        else
            echo "No open ports found or target IP might be incorrect."
        fi
    }

    # Check if target IP is provided
    if [ -z "$1" ]; then
        echo "Usage: $0 <target_ip>"
        exit 1
    fi

    # Call the function to check for open ports
    check_ports $1
    ```

2. **Make the Script Executable**

   Ensure the script has executable permissions:
    ```bash
    chmod +x scan_and_exploit.sh
    ```

3. **Run the Script**

   Execute the script by providing the target IP address:
    ```bash
    ./scan_and_exploit.sh <target_ip>
    ```

   Replace `<target_ip>` with the actual IP address you wish to scan.

### Example Output

Here is an example of the output you might see:

```bash
Checking for open ports on 192.168.1.1...
Open ports found:
Open 22/tcp on 192.168.1.1
Open 80/tcp on 192.168.1.1
Processing port: 22
Next command: ssh <username>@192.168.1.1
Processing port: 80
Next command: wget http://192.168.1.1
```

### Debugging Tips

- **Verify Target IP**: Ensure the target IP address is reachable and correct. You can use `ping` to verify connectivity:
  ```bash
  ping <target_ip>
  ```

- **Check Rustscan Installation**: Ensure Rustscan is installed and correctly set up in your PATH.

## Conclusion

This script automates the process of identifying open ports and suggesting the next appropriate command, making it a useful tool for network reconnaissance.
