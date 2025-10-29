# Static Binary Analysis - picoCTF Flag Found

## Flag
The flag found in the static binary is:

**picoCTF{d15a5m_t34s3r_6f8c8200}**

## Analysis Process

### 1. Binary Information
- File: `static` (ELF 64-bit LSB pie executable, x86-64)
- Not stripped binary, making analysis easier

### 2. Disassembly Process
Used the provided `ltdis.sh` script to:
- Disassemble the binary using `objdump -Dj .text`
- Extract strings using `strings -a -t x`

### 3. Flag Location
The flag was found in the strings output at offset `0x1020`:
```
1020 picoCTF{d15a5m_t34s3r_6f8c8200}
```

### 4. Additional Context
The binary also contains an interesting message at offset `0x6e8`:
```
Oh hai! Wait what? A flag? Yes, it's around here somewhere!
```

## Files Generated
- `static.ltdis.x86_64.txt` - Full disassembly
- `static.ltdis.strings.txt` - Extracted strings with offsets

The flag was successfully extracted from the static binary using string analysis.