#!/usr/bin/env python3

# Numbers from the image as provided by user
numbers = [16, 9, 3, 15, 3, 20, 6, 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14]

# Convert numbers to letters (A=1, B=2, etc.)
flag = ""
for num in numbers:
    if num == 0:  # space
        flag += " "
    else:
        flag += chr(num + 64)  # A=65 in ASCII

print(f"Decoded flag: {flag}")

# Write to numbers.md
with open('numbers.md', 'w') as f:
    f.write("# Numbers Challenge Flag\n\n")
    f.write(f"Original numbers: {numbers}\n\n")
    f.write(f"Decoded flag: {flag}\n")

print("Results saved to numbers.md")