# picoCTF Blame Game Challenge Solution

## Challenge Overview
The Blame Game challenge provides a zip file containing a git repository. The goal is to find the hidden picoCTF flag using git commands.

## Files Provided
- `challenge.zip` - Contains a git repository in the `drop-in/` directory

## Solution Process

### 1. Extraction
```bash
unzip challenge.zip
```
Extracted to `drop-in/` directory containing:
- `message.txt` - A file with a hint about checking commit history
- `.git/` - Complete git repository with commit history

### 2. Initial Analysis
The `message.txt` file contains:
```
This is what I was working on, but I'd need to look at my commit history to know why...
```
This clearly indicates we need to examine the git history.

### 3. Git Investigation

#### Method 1: Git Log
```bash
cd drop-in
git log --oneline
```
Output:
```
e65fedb picoCTF{t1m3m@ch1n3_88c35e3b}
```

#### Method 2: Git Blame
```bash
git blame message.txt
```
Output:
```
^e65fedb (picoCTF 2024-03-12 00:07:29 +0000 1) This is what I was working on, but I'd need to look at my commit history to know why...
```

#### Method 3: Git Show
```bash
git show e65fedb
```
Output shows the commit details with the flag as the commit message.

## Flag Found
**picoCTF{t1m3m@ch1n3_88c35e3b}**

## Key Techniques
1. **Git Log** - Revealed commit history with flag as commit message
2. **Git Blame** - Shows commit hash and author information for each line
3. **Git Show** - Displays detailed commit information including the flag

## Challenge Category
Forensics / Git Analysis

## Difficulty
Easy - Basic git knowledge required