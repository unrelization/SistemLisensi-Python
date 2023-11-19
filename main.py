import json
import bcrypt

def login(username, password, data):
    for user in data:
        if user["username"] == username:
            # Check the password
            hashed_password = user["password"].encode('utf-8')
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                return user["owned"]
            else:
                return "Wrong password"
    
    return "User not exists"

# Load data from the URL
import requests
url = "https://unrelization.github.io/data.json"
response = requests.get(url)
data = json.loads(response.text)

# Example usage
username_input = input("Enter username: ")
password_input = input("Enter password: ")

result = login(username_input, password_input, data)

print(result)
