import requests as req
import json
import urllib.parse as up
# Python urllib works on source code but for dynamic code requests can be used as the code changes
# get and post requests can be done using this library
HOST = 'http://127.0.0.1:8000'

ourRequestkaResponse = req.get(up.urljoin(HOST, '/api/v1/patient_/user/'))

response_data = json.loads(ourRequestkaResponse.text)

result = response_data.get('results')
print(type(result))
print(result)
# Itterate over all list using this array
