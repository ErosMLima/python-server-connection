import urllib.request
DATA = b'some data'
req = urllib.request.Request(url='http://localhost:8000', data=DATA,method='GET')
with urllib.request.urlopen(req) as f:
    pass
print(f.status)
print(f.reason)