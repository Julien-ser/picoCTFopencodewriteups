# picoCTF Bookmarklet Challenge Solution

## Challenge Information
- **Target URL**: http://titan.picoctf.net:59705/
- **Challenge Type**: Bookmarklet Decryption
- **Final Flag**: `picoCTF{p@g3_turn3r_1d1ba7e0}`

## Process Documentation

### Step 1: Initial Exploration
Visited the target website and found a simple page with:
- picoCTF branding
- A welcome message stating "If you're reading this, your browser has successfully received the flag"
- A bookmarklet containing encrypted data

### Step 2: Analysis of the Bookmarklet
The bookmarklet contained the following JavaScript code:
```javascript
javascript:(function() { 
    var encryptedFlag = "àÒÆÞ¦È¬ëÙ£ÖÓÚåÛÑ¢ÕÓÔÅÐÙí"; 
    var key = "picoctf"; 
    var decryptedFlag = ""; 
    for (var i = 0; i < encryptedFlag.length; i++) { 
        decryptedFlag += String.fromCharCode((encryptedFlag.charCodeAt(i) - key.charCodeAt(i % key.length) + 256) % 256); 
    } 
    alert(decryptedFlag); 
})();
```

### Step 3: Decryption Algorithm Analysis
The encryption/decryption method used is:
1. **XOR-like cipher**: Character code subtraction with modular arithmetic
2. **Key**: "picoctf" (repeated cyclically)
3. **Formula**: `(encrypted_char_code - key_char_code + 256) % 256`

### Step 4: Flag Extraction
Using Python to replicate the decryption algorithm:
```python
encrypted_flag = 'àÒÆÞ¦È¬ëÙ£ÖÓÚåÛÑ¢ÕÓÔÅÐÙí'
key = 'picoctf'
decrypted_flag = ''
for i in range(len(encrypted_flag)):
    decrypted_flag += chr((ord(encrypted_flag[i]) - ord(key[i % len(key)]) + 256) % 256)
```

**Result**: `picoCTF{p@g3_turn3r_1d1ba7e0}`

## Technical Details

### Encryption Method
- **Type**: Vigenère-like cipher using character code arithmetic
- **Key**: "picoctf" (8 characters, repeated)
- **Algorithm**: Each character is decrypted by subtracting the corresponding key character's ASCII value, with modulo 256 to handle wrap-around

### Security Notes
- The bookmarklet approach demonstrates client-side decryption
- The key is hardcoded and visible in the JavaScript
- This is a basic cryptographic challenge suitable for CTF beginners

## Solution Summary
The challenge required analyzing a bookmarklet containing an encrypted flag. By understanding the simple character-based decryption algorithm and implementing it in Python, we successfully extracted the flag: `picoCTF{p@g3_turn3r_1d1ba7e0}`.