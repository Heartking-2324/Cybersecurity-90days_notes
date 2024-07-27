# Intrusion Detection and Prevention with Snort and Suricata

Welcome to the Intrusion Detection and Prevention project! In this guide, we’ll explore how to set up and configure both Snort and Suricata, two powerful open-source Intrusion Detection Systems (IDS), to safeguard your network from potential threats.

## 🛠️ Prerequisites

Before we get started, make sure you have the following:

- **Snort**: Download it from [Snort's official website](https://www.snort.org/downloads).
- **Suricata**: Download it from [Suricata's official website](https://suricata-ids.org/download/).
- **Libdnet**: Install it using the following command on Ubuntu/Debian:

  ```bash
  sudo apt-get install libdnet-dev
  ```

## 📥 Installation

1. **Download and Install Snort and Suricata**

   Follow the installation guides provided on the Snort and Suricata websites to install both IDS tools.

2. **Configure Snort**

   Create a configuration file named `snort.conf` in the `/etc/snort` directory. You can refer to the [Snort documentation](https://www.snort.org/documents) for configuration details.

3. **Configure Suricata**

   Create a configuration file named `suricata.yaml` in the `/etc/suricata` directory. Check out the [Suricata documentation](https://suricata-ids.org/docs/) for guidance.

4. **Set Up Directories and Rules for Snort**

   - **Create Directories:**

     ```bash
     sudo mkdir -p /etc/snort/rules
     sudo mkdir -p /etc/snort/preproc_rules
     sudo mkdir -p /etc/snort/so_rules
     ```

   - **Download and Extract Default Snort Rules:**

     ```bash
     sudo wget -P /etc/snort/rules https://www.snort.org/rules/snortrules-snapshot-2976.tar.gz
     sudo tar -xvzf /etc/snort/rules/snortrules-snapshot-2976.tar.gz -C /etc/snort/rules
     ```

   - **Create and Add Custom Rules:**

     Create a file named `local.rules` in the `/etc/snort/rules` directory. Add your custom rules to this file to monitor specific traffic patterns.

5. **Set Up Directories and Rules for Suricata**

   Follow similar steps to create necessary directories and download rules if applicable for Suricata.

## 🚀 Usage

1. **Start Snort**

   Use the following command to start Snort:

   ```bash
   sudo snort -c /etc/snort/snort.conf -i <interface>
   ```

   Replace `<interface>` with the network interface you want to monitor.

2. **Start Suricata**

   Use the following command to start Suricata:

   ```bash
   sudo suricata -c /etc/suricata/suricata.yaml -i <interface>
   ```

   Replace `<interface>` with the network interface you want to monitor.

## 🕵️‍♂️ Explanation

### **Snort**

Snort is a versatile IDS that uses a rule-based approach to detect and alert on suspicious network activities. It can be configured to monitor specific network interfaces and provide real-time alerts based on predefined rules.

### **Suricata**

Suricata is a more advanced IDS that supports multiple protocols and provides detailed analysis of network traffic. It uses pattern matching and protocol-specific rules to detect intrusions and can also perform network traffic analysis.

### **Combining Both**

By configuring both Snort and Suricata, you can benefit from their complementary features. This combination offers a robust security solution, enhancing both detection capabilities and context around alerts.

## 🔔 Note

This guide provides a foundational setup for Snort and Suricata. To maximize security, consider adding additional rules and fine-tuning configurations based on your network environment.

Remember to run both Snort and Suricata with appropriate permissions and ensure you have authorization to monitor and analyze network traffic.
