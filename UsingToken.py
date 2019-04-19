import requests as req
import json
import urllib.parse as up
# Python urllib works on source code but for dynamic code requests can be used as the code changes
# get and post requests can be done using this library
HOST = 'http://127.0.0.1:8000'

token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNjBjNGUwNzEtMGI4My00MTgwLTg1YTUtNjZmNGY3Mjc2ODQ2IiwidXNlcm5hbWUiOiJobTM4QGdtYWlsLmNvbSIsImV4cCI6MTU1NjkwMjY1NSwiZW1haWwiOiJobTM4QGdtYWlsLmNvbSIsIm9yaWdfaWF0IjoxNTU1NjkzMDU1fQ.kTJKKGcgvqA8dHeviem9uuLLzJFVcZGWUxtFIisEG8s'
Auth_data = "JWT {}".format(token)
headers = {
    'Authorization': Auth_data
}

ourRequestkaResponse = req.get(up.urljoin(
    HOST, '/api/v1/patient_/patient/'), headers=headers)

response_data = json.loads(ourRequestkaResponse.text)
print(ourRequestkaResponse)
result = response_data.get('results')
print(type(result))
print(result)
# Iterate over all list using this array
