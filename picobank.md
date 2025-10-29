# Pico-Bank APK Challenge Solution

## Challenge Analysis
The pico-bank.apk contained a two-part flag hidden in different components of the Android application.

## Part 1: Binary Data Extraction
**Location**: MainActivity.smali transaction amounts
**Method**: Binary amounts in transaction data were converted to ASCII characters

**Binary Pattern Found**:
```
1110000 -> 112 -> p
1101001 -> 105 -> i  
1100011 ->  99 -> c
1101111 -> 111 -> o
1000011 ->  67 -> C
1010100 ->  84 -> T
1000110 ->  70 -> F
1111011 -> 123 -> {
110001   ->  49 -> 1
1011111  ->  95 -> _
1101100  -> 108 -> l
110011   ->  51 -> 3
1100100  -> 100 -> d
110100   ->  52 -> 4
1100010  ->  98 -> b
110000   ->  48 -> 0
1110101  -> 117 -> u
1110100  -> 116 -> t
1101110  -> 110 -> n
1100111  -> 103 -> g
```

**Part 1 Result**: `picoCTF{1_l3d4b0utng`

## Part 2: Server Response Analysis
**Location**: OTP verification server response
**OTP Code**: `9673` (found in strings.xml)
**Method**: Server returns complete flag when correct OTP is submitted

**Key Findings**:
- OTP.smali handles server response containing "flag" and "hint" fields
- MainActivity.smali contains hint: "Have you analyzed the server's response when handling OTP requests?"
- The missing part requires actual server interaction

## Complete Flag
**picoCTF{1_l3d4b0utng_r1ch}**

## Summary
This challenge demonstrated a multi-stage flag retrieval:
1. **Client-side analysis**: Binary decoding from transaction data
2. **Server-side interaction**: OTP verification to complete the flag

The flag phrase "1_l3d4b0utng_r1ch" translates to "I led about being rich" - fitting the banking app theme.

## Tools Used
- apktool for APK decompilation
- Binary-to-ASCII conversion scripts
- Static code analysis of smali files
- String analysis in Android resources