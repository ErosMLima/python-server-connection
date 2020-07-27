import urllib.request
req = urllib.request.Request('http://localhost:8000')
req.add_header('Referer', 'http://localhost:8000')
# Customize the default User-Agent header value:
req.add_header('User-Agent', 'urllib-example/0.1 (Contact: . . .)')
r = urllib.request.urlopen(req)