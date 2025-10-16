import requests
import json


class TestJSONPlaceholderAPI:
    baseURL = "https://jsonplaceholder.typicode.com"

    def test_fetch_user_successfully(self):
        # Create full endpoint
        fullURL = f"{self.baseURL}/users/1"
        # Make request
        response = requests.get(fullURL)
        # Get the server response
        print(f"GET {fullURL}")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}\n")

    def test_create_new_post(self, title, body, userId):
        # Create full endpoint
        fullURL = f"{self.baseURL}/posts"
        # Create the request in JSON format
        payload = {
            "title": title,
            "body": body,
            "userId": userId
        }
        headers = {"Content-Type": "application/json"}
        # Make request
        response = requests.post(fullURL, headers=headers, data=json.dumps(payload))
        # Get the server response
        print(f"POST {fullURL}")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}\n")
        
    def test_handle_nonexistent_user(self):
        # Create full endpoint
        fullURL = f"{self.baseURL}/users/999"
        # Make request
        response = requests.get(fullURL)
        # Get the server response
        print(f"GET {fullURL}")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}\n")


# Run all the test cases
if __name__=="__main__":
    # Create an instance of the TestJSONPlaceholderAPI class
    testInstance = TestJSONPlaceholderAPI()
    # For the post request, let's have the request json come from user input so that different inputs can be used
    title = input("Write a title: ")
    body = input("Write a body: ")
    id = int(input("Your User ID: "))
    print(f"\n")
    # Test 1: First endpoint (GET)
    print(f"\n--- TEST: First Endpoint ---\n")
    testInstance.test_fetch_user_successfully()
    # Test 2: Second Endpoint (POST)
    print(f"\n--- TEST: Second Endpoint ---\n")
    testInstance.test_create_new_post(title, body, id)
    # Test 3: Third Endpoint (GET)
    print(f"\n--- TEST: Third Endpoint ---\n")
    testInstance.test_handle_nonexistent_user()