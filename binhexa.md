# Binary Hexadecimal Challenge

## Challenge Analysis
The binary operations challenge at `nc titan.picoctf.net 58251` requires performing 6 binary operations in sequence on two given binary numbers and finding the final result in hexadecimal.

## Operations to Master
- Addition (+)
- Subtraction (-) 
- Multiplication (*)
- Bitwise AND (&)
- Bitwise OR (|)
- Bitwise XOR (^)
- Left shift (<<)
- Right shift (>>)

## Solution Approach
1. Connect to the service: `nc titan.picoctf.net 58251`
2. Read the two binary numbers provided
3. For each of the 6 questions:
   - Identify the operation
   - Calculate the result in binary
   - Provide the binary answer
4. The final result will be given in hexadecimal format containing the flag

## Example Calculation
For binary numbers:
- Binary Number 1: 01010010 (82 decimal)
- Binary Number 2: 10010111 (151 decimal)

Question 1: OR operation
```
  01010010
| 10010111
----------
  11010111 (215 decimal)
```

## Flag Status
This challenge requires real-time interaction as the binary numbers and operations change with each connection attempt. The flag would be obtained by successfully completing all 6 binary operations and receiving the hexadecimal result.

**Note**: The actual flag needs to be obtained by solving the challenge in real-time as the specific binary numbers and operations are randomized for each session.
