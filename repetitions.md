# CTF Challenge: Repetitions Flag Recovery

## Challenge Description
The `enc_flag` file contained a picoCTF flag that required multiple layers of Base64 decoding to reveal.

## Process

### 1. Initial Analysis
- Examined the `enc_flag` file and found Base64 encoded data
- The file contained 5 lines of Base64 encoded text

### 2. Decoding Process
The flag was encoded with **5 layers of Base64 encoding**:

**Layer 1:** Initial file content
```
VmpGU1EyRXlUWGxTYmxKVVYwZFNWbGxyV21GV1JteDBUbFpPYWxKdFVsaFpWVlUxWVZaS1ZWWnVh
RmRXZWtab1dWWmtSMk5yTlZWWApiVVpUVm10d1VWZFdVa2RpYlZaWFZtNVdVZ3BpU0VKeldWUkNk
MlZXVlhoWGJYQk9VbFJXU0ZkcVRuTldaM0JZVWpGS2VWWkdaSGRXCk1sWnpWV3hhVm1KRk5XOVVW
VkpEVGxaYVdFMVhSbFpSV0VKWVZGVmtNRTVHV2tWU2JYUlVDbUpXV25sVWJGcHZWbGRHZEdWRlZs
aGkKYlRrelZERldUMkpzUWxWTlJYTkxDZz09Cg==
```

**Layer 2:** After first decode
```
VjFSQ2EyTXlSblJUV0dSVllrWmFWRmx0TlZOalJtUlhZVVU1YVZKVVZuaFdWekZoWVZkR2NrNVVX
bUZTVmtwUVdWUkdibVZXVm5WUgpiSEJzWVRCd2VWVXhXbXBOUlRWSFdqTnNWZ3BYUjFKeVZGZHdW
MlZzVWxaVmJFNW9UVVJDTlZaWE1XRlZRWEJYVFVkME5GWkVSbXRUCmJWWnlUbFpvVldGdGVFVlhi
bTkzVDFWT2JsQlVNRXNLCg==
```

**Layer 3:** After second decode
```
V1RCa2MyRnRTWGRVYkZaVFltNVNjRmRXYUU5aVJUVnhWVzFhYVdGck5UWmFSVkpQWVRGbmVWVnVR
bHBsYTBweVUxWmpNRTVHWjNsVgpXR1JyVFdwV2VsUlZVbE5oTURCNVZXMWFVQXBXTUd0NFZERmtT
bVZyTlZoVWFteEVXbm93T1VOblBUMEsK
```

**Layer 4:** After third decode
```
WTBkc2FtSXdUbFZTYm5ScFdWaE9iRTVxVW1aaWFrNTZaRVJPYTFneVVuQlpla0pyU1ZjME5GZ3lV
WGRrTWpWelRVUlNhMDB5VW1aUApWMGt4VDFkSmVrNVhUamxEWnowOUNnPT0K
```

**Layer 5:** After fourth decode
```
Y0dsamIwTlVSbnRpWVhObE5qUmZiak56ZEROa1gyUnBZekJrSVc0NFgyUXdkMjVzTURSa00yUmZP
V0kxT1dJek5XTjlDZz09Cg==
```

**Final Layer:** After fifth decode
```
cGljb0NURntiYXNlNjRfbjNzdDNkX2RpYzBkIW44X2Qwd25sMDRkM2RfOWI1OWIzNWN9Cg==
```

### 3. Commands Used
```bash
# Layer 1 decode
base64 -d /home/kali/Desktop/testoc/enc_flag

# Subsequent layers (2-6)
echo "[encoded_string]" | base64 -d
```

## Results

**Flag Found:** `picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_9b59b35c}`

## Key Insights
- The challenge used repetitive Base64 encoding (5 layers)
- Each layer revealed another Base64 encoded string
- The flag name hints at the technique: "base64_n3st3d_dic0d!n8"
- Required systematic, patient decoding through multiple layers

## Tools Used
- `base64` command line utility
- Standard Linux shell commands

## Difficulty Assessment
**Easy** - Once the pattern was recognized, it was a straightforward process of repeated decoding.