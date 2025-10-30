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

**Part 1 Result**: `picoCTF{1_l3d4b0utng` (incomplete - missing middle component)

## Part 2: Server Response Analysis
**Location**: OTP verification server response
**OTP Code**: `9673` (found in strings.xml)
**Method**: Server returns complete flag when correct OTP is submitted

**Key Findings**:
- OTP.smali handles server response containing "flag" and "hint" fields
- MainActivity.smali contains hint: "Have you analyzed the server's response when handling OTP requests?"
- The missing part requires actual server interaction

## Part 3: Date-Sorted Binary Analysis
**Discovery**: The same binary amounts sorted by transaction date reveal the missing middle component
**Method**: Binary amounts sorted chronologically (2023-06-15 to 2023-07-21) and read in reverse

**Date-Sorted Binary Pattern**:
```
Chronological order (reversed reading): _gn3b_tu0b4_d3l_1{FTCocip
When reversed: picoCTF{1_l3d_4b0ut_b3ng_
```

**Missing Middle Component**: `_4b0ut_b3ng_` (about_being_)

## Complete Flag
**picoCTF{1_l3d_4b0ut_b3ng_r1ch}**

## Summary
This challenge demonstrated a complex multi-stage flag retrieval:
1. **Code-order analysis**: Binary decoding from transaction data in code order
2. **Chronological analysis**: Same binary data sorted by date reveals missing middle component
3. **Server-side interaction**: OTP verification to complete the flag ending

**Flag Construction**:
- Part 1 (code order): `picoCTF{1_l3d`
- Part 2 (date-sorted): `_4b0ut_b3ng_` 
- Part 3 (server response): `r1ch}`

The flag phrase "1_l3d_4b0ut_b3ng_r1ch" translates to "I led about being rich" with leetspeak substitutions - fitting the banking app theme.

## Tools Used
- apktool for APK decompilation
- Binary-to-ASCII conversion scripts
- Static code analysis of smali files
- String analysis in Android resources