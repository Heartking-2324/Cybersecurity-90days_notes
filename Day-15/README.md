# Day-15 tryhackme room (c4ptur3-th3-fl4g)

This is very interseting room which i found while srcolling the rooms on tryhackme platform where we have to convert and identify the flags where we get idea's of the cyptography and its various methods. 
## Overview
This room is focused on decoding, deciphering, and extracting hidden data. It covers various methods of cryptography and data encoding.

## Task 1   Translation & Shifting

### Q.1 c4n y0u c4p7u23 7h3 f149?  
 Answer   Can you capture the flag?  
 Explanation   This is  leet speak (or  1337 speak ), where numbers and symbols replace letters. 

### Q.2 01101100 01100101 01110100 01110011 00100000 01110100 01110010 01111001 00100000 01110011 01101111 01101101 01100101 00100000 01100010 01101001 01101110 01100001 01110010 01111001 00100000 01101111 01110101 01110100 00100001   
 Answer   lets try some binary out!  
 Explanation   This is  binary encoding . Each 8-bit segment represents a character in ASCII. [Convert binary to text](https  //www.rapidtables.com/convert/number/binary-to-ascii.html).

### Q.3 MJQXGZJTGIQGS4ZAON2XAZLSEBRW63LNN5XCA2LOEBBVIRRHOM======  
 Answer   base32 is super common in CTF’s.  
 Explanation   This is  Base32 encoding . [Decode Base32](https  //www.dcode.fr/base-32).

### Q.4 RWFjaCBCYXNlNjQgZGlnaXQgcmVwcmVzZW50cyBleGFjdGx5IDYgYml0cyBvZiBkYXRhLg==  
 Answer   Each Base64 digit represents exactly 6 bits of data.  
 Explanation   This is  Base64 encoding . [Decode Base64](https  //base64decode.org/).

### Q.5 68 65 78 61 64 65 63 69 6d 61 6c 20 6f 72 20 62 61 73 65 31 36 3f  
 Answer   hexadecimal or base16?  
 Explanation   This is  hexadecimal encoding . [Convert hexadecimal to text](https  //www.dcode.fr/hexadecimal).

### Q.6 Ebgngr zr 13 cynprf!
 Answer   Rotate me 13 places!  
 Explanation   This is a  ROT-13 cipher . [Decode ROT-13](https  //www.dcode.fr/rot-13).

### Q.7 *@F DA  ? >6 C  89E C@F?5 323J C  89E C@F?5 Wcf E  >6DX  
 Answer   You spin me right round baby right round (47 times) (ROT -47 cipher)  
 Explanation   This is a  ROT-47 cipher . Tools like [dcode.fr](https  //www.dcode.fr/rot-47) can help decode it.

### Q.8 
```
        - . .-.. . -.-. — — — — ..- -. .. -.-. .- — .. — — -.
        . -. -.-. — — -.. .. -. — .
```
 Answer   telecommunication encoding.  
 Explanation   This is  Morse code . [Decode Morse code](https  //morsedecoder.com/).

### Q.9 85 110 112 97 99 107 32 116 104 105 115 32 66 67 68 
 Answer   Unpack this BCD (Binary Coded Decimal)  
 Explanation   This is  Binary Coded Decimal (BCD) . [Convert BCD to text](https  //www.dcode.fr/binary-coded-decimal).

### Q.10 LS0tLS0gLi0tLS0gLi0tLS0gLS0tL.......  
 Answer   Let’s make this a bit trickier…  
 Explanation   This involves multiple steps    
1.  Base64 decoding  
2.  Morse Code decoding  
3.  Binary decoding  
4.  ROT -47 cipher  
5.  Decimal conversion

## Task 2   Spectrograms

1.  Download Sonic Visualizer   [Sonic Visualizer Download](https  //www.sonicvisualiser.org/download.html)  
2.  Open the Sound File   Launch Sonic Visualizer and open the provided sound file.
3.  Add Spectrogram Layer   Click on `Layer -> Add Spectrogram`.  
4.  Find the Flag   The spectrogram will reveal the flag.

 Answer   Super Secret Message.

## Task 3   Steganography

1.  Extract Hidden Data   Use the `steghide` tool to extract hidden data from the image.
   ```bash
   steghide extract -sf stegosteg.jpg
   ```
 Answer   SpaghettiSteg

## Task 4   Security through Obscurity

1.  Check the File Content   Use the `cat` command to view the contents of the file.
   ```bash
   cat meme.jpg
   ```

### Q.1 Download and get 'inside' the file. What is the first filename & extension?
 Answer   hackerchat.png

### Q.2 Get inside the archive and inspect the file carefully. Find the hidden text.
 Answer   AHH_YOU_FOUND_ME!

## Conclusion

Feel free to explore and solve the tasks using the provided links and tools. Enjoy decoding and deciphering!
```
