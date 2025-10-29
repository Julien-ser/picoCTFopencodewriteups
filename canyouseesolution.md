# CTF Challenge Solution: unknown.zip

## Challenge Summary
This CTF challenge involved extracting a hidden flag from a zip file containing a JPEG image.

## Solution Steps

### 1. Extract the ZIP file
```bash
unzip unknown.zip
```
- Extracted `ukn_reality.jpg` (2.3 MB JPEG image)

### 2. Analyze the JPEG file
- Used `file` command to confirm it's a valid JPEG image
- Searched for strings in the file but didn't find obvious flag patterns
- Attempted binwalk (failed due to missing dependencies)

### 3. Extract EXIF metadata
```bash
exiftool ukn_reality.jpg
```
- Found suspicious data in the "Attribution URL" field:
  ```
  Attribution URL: cGljb0NURntNRTc0RDQ3QV9ISUREM05fM2I5MjA5YTJ9Cg==
  ```

### 4. Decode the Base64 string
```bash
echo "cGljb0NURntNRTc0RDQ3QV9ISUREM05fM2I5MjA5YTJ9Cg==" | base64 -d
```
- Result: `picoCTF{ME74D47A_HIDD3N_3b9209a2}`

## Flag
**picoCTF{ME74D47A_HIDD3N_3b9209a2}**

## Techniques Used
- ZIP file extraction
- EXIF metadata analysis
- Base64 decoding
- Steganography (data hidden in image metadata)

## Key Insight
The flag was hidden in the EXIF metadata of the JPEG image, specifically in the "Attribution URL" field as a base64-encoded string. This is a common steganography technique where data is hidden in the metadata of image files rather than in the image content itself.