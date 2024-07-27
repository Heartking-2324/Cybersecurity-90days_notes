# Detect suspicious outbound traffic
```
alert tcp any any -> $HOME_NET any (msg:"Suspicious outbound traffic"; flags:S; flow:established,to_server; content:"|28|"; nocase; sid:1000001; rev:1;)
```
# Detect port scans
```
alert tcp $EXTERNAL_NET any -> $HOME_NET 80 (msg:"Port scan to port 80"; flags:S; threshold: type both, track by_src, count 10, seconds 60; sid:1000002; rev:1;)
alert tcp $EXTERNAL_NET any -> $HOME_NET 443 (msg:"Port scan to port 443"; flags:S; threshold: type both, track by_src, count 10, seconds 60; sid:1000003; rev:1;)
```
# Detect suspicious file transfers
```
alert tcp $EXTERNAL_NET any -> $HOME_NET 21 (msg:"Suspicious FTP activity"; content:"|211-"; nocase; flow:established,to_server; sid:1000004; rev:1;)
alert tcp $EXTERNAL_NET any -> $HOME_NET 22 (msg:"Suspicious SSH activity"; content:"SSH-"; nocase; flow:established,to_server; sid:1000005; rev:1;)
```
# Detect suspicious DNS traffic
```
alert udp $EXTERNAL_NET any -> $HOME_NET 53 (msg:"Suspicious DNS activity"; content:"|00 01|00 02|00 05|00 06|"; nocase; sid:1000006; rev:1;)
```
# Detect suspicious HTTP traffic
```
alert tcp $EXTERNAL_NET any -> $HOME_NET 80 (msg:"Suspicious HTTP activity"; content:"GET /admin"; nocase; flow:established,to_server; sid:1000007; rev:1;)
alert tcp $EXTERNAL_NET any -> $HOME_NET 80 (msg:"Suspicious HTTP activity"; content:"POST /login"; nocase; flow:established,to_server; sid:1000008; rev:1;)
```
## These are some of commonly used rules by industries in their snort. 
