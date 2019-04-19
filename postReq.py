import requests as req
import json
import urllib.parse as up
# Analyzing and sending request
HOST = 'http://127.0.0.1:8000'
payload = {
    'first_name': 'Hello',
    'last_name': 'Mike',
    'middle_name': 'Mickey',
    'email': 'hm38@gmail.com',
    'password': 'test123',
}
# payload = json.dumps(payload)
ourRequest = req.post(
    up.urljoin(HOST, 'api/v1/patient_/user/'), data=payload)
print(ourRequest)
