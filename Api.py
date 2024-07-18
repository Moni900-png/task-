import json
import requests



# Read data from text file
data = {}
with open('data.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        key, value = line.strip().split(': ')
        data[key.strip()] = value.strip()

print("Data read from text file:")
print(data)

#Convert data to JSON
json_data = json.dumps(data, indent=4)
print("\nData in JSON format:")
print(json_data)

#import requests

# Define the API endpoint URL
api_url = 'http://example.com/api/data'

# Define headers (if required by the API)
headers = {'Content-Type': 'application/json'}

# Make POST request with JSON data
response = requests.post(api_url, headers=headers, json=json_data)

# Check the response status
if response.status_code == 404:
    print("\nData successfully sent to API.")
else:
    print(f"\nFailed to send data to API. Status code: {response.status_code}")
    print(response.text)



