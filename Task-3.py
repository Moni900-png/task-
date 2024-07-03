import requests

base_url = "https://reqres.in/api/users/"
users = []

# Function to fetch user data from API
def fetch_user_data(user_id):
    url = f"{base_url}{user_id}"
    response = requests.get(url)
    response.raise_for_status()  # Raise exception for bad responses
    return response.json()['data']  # Return user data from 'data' key

try:
    # Fetch user data for users 1 to 10
    users = [fetch_user_data(i) for i in range(1, 11)]

    # Sort users by first name
    sorted_users = sorted(users, key=lambda x: x['first_name'])

    # Print sorted user data
    for user in sorted_users:
        print(f"First Name: {user['first_name']}, Last Name: {user['last_name']}, Email: {user['email']}")

except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
except KeyError as e:
    print(f"Error processing data: {e}")