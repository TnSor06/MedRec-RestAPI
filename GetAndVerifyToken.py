import requests as req
import json
import urllib.parse as up
HOST = 'http://127.0.0.1:8000'
# Receiving token
# data = {
#     "email": "hm38@gmail.com",
#     "password": "test123"
# }

# ourRequestkaResponse = req.post(
#     up.urljoin(HOST, '/api/v1/token-auth/'), data=data)
# response_data = json.loads(ourRequestkaResponse.text)
# print(ourRequestkaResponse.text)
# # Gives {"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNjBjNGUwNzEtMGI4My00MTgwLTg1YTUtNjZmNGY3Mjc2ODQ2IiwidXNlcm5hbWUiOiJobTM4QGdtYWlsLmNvbSIsImV4cCI6MTU1NjkwMjY1NSwiZW1haWwiOiJobTM4QGdtYWlsLmNvbSIsIm9yaWdfaWF0IjoxNTU1NjkzMDU1fQ.kTJKKGcgvqA8dHeviem9uuLLzJFVcZGWUxtFIisEG8s"}
# token = response_data.get('token')
# print(token)
token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNjBjNGUwNzEtMGI4My00MTgwLTg1YTUtNjZmNGY3Mjc2ODQ2IiwidXNlcm5hbWUiOiJobTM4QGdtYWlsLmNvbSIsImV4cCI6MTU1NjkwMjY1NSwiZW1haWwiOiJobTM4QGdtYWlsLmNvbSIsIm9yaWdfaWF0IjoxNTU1NjkzMDU1fQ.kTJKKGcgvqA8dHeviem9uuLLzJFVcZGWUxtFIisEG8s'

# Verify Token
data = {
    "token": token
}
ourRequestkaResponse = req.post(
    up.urljoin(HOST, '/api/v1/api-token-verify/'), data=data)
response_data = json.loads(ourRequestkaResponse.text)
veirfy_token = response_data.get('token')
if(veirfy_token == token):
    print('Token Verified')

else:
    print('Token Invalid')
