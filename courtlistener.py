import os

import requests

# Load secrets from environment variables

pacer_username = os.getenv('PACER_USERNAME')
pacer_password = os.getenv('PACER_PASSWORD')
auth_token = os.getenv('COURT_LISTENER_API_KEY')

# Define the payload for the POST request

payload = {
'request_type': '1',
'docket_number': '5:16-cv-00432',
'court': 'okwd'
}

# Define the headers for the POST request

headers = {
'Authorization': f'Token {auth_token}'
}

# Make the POST request to the API

response = requests.post(
'https://www.courtlistener.com/api/rest/v3/recap-fetch/',
data=payload,
headers=headers,
auth=(pacer_username, pacer_password)
)

# Check if the request was successful

if response.ok:
    print('Request successful.')
else:
    print('Request failed.')

# End of Selection

# Make a POST request to fetch a PDF
pdf_response = requests.post(
    'https://www.courtlistener.com/api/rest/v3/recap-fetch/',
    data={
        'request_type': '2',
        'recap_document': '112'
    },
    headers={
        'Authorization': f'Token {auth_token}'
    },
    auth=(pacer_username, pacer_password)
)

# Check if the PDF request was successful
if pdf_response.ok:
    print('PDF request successful.')
else:
    print('PDF request failed.')
