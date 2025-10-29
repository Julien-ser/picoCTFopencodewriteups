# PicoCTF Mercury Challenge Solution

## Target URL
http://mercury.picoctf.net:15931/

## Challenge Analysis
The webpage presented a simple interface with two options:
- **Red** (GET method form)
- **Blue** (POST method form)

## Discovery Process

### Initial Investigation
1. Fetched the main page which showed "Red" and "Blue" sections
2. Examined the HTML source code and found:
   - Red form uses GET method: `<form action="index.php" method="GET">`
   - Blue form uses POST method: `<form action="index.php" method="POST">`

### Testing HTTP Methods
1. **GET Request**: Submitted the Red form - returned the same page with red background
2. **POST Request**: Submitted the Blue form - returned the same page with blue background
3. **HEAD Request**: Used `curl -X HEAD` to test the HEAD method

### Flag Discovery
The flag was discovered in the HTTP response headers when using the HEAD method:

```bash
curl -X HEAD http://mercury.picoctf.net:15931/index.php -i
```

**Response Headers:**
```
HTTP/1.1 200 OK
flag: picoCTF{r3j3ct_th3_du4l1ty_82880908}
Content-type: text/html; charset=UTF-8
```

## Solution
The challenge required testing different HTTP methods beyond the obvious GET and POST. The flag was hidden in the response headers of a HEAD request, which aligns with the flag name "r3j3ct_th3_du4l1ty" (reject the duality) - suggesting to look beyond the binary choice of Red/Blue (GET/POST).

## Flag
**picoCTF{r3j3ct_th3_du4l1ty_82880908}**

## Tools Used
- curl for HTTP method testing
- Web browser for initial reconnaissance
- HTML source code analysis