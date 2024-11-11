import requests
from termcolor import colored

# Ask the user to enter the base URL
base_url = input("Please enter the base URL (e.g., https://example.com/): ")

# Open the common.txt file and read the words
with open("common.txt", "r") as file:
    words = file.readlines()

# Try each word in the common.txt file
for word in words:
    # Remove any whitespace around the word
    word = word.strip()
    
    # Construct the new URL
    test_url = f"{base_url}{word}"
    
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(test_url)
        
        # If the response is successful (200 OK), consider the URL valid
        if response.status_code == 200:
            print(colored(f"Valid URL: {test_url}", "green"))
        else:
            print(colored(f"Invalid URL: {test_url}", "red"))
    
    except requests.exceptions.RequestException:
        # If there is a connection error, consider the URL invalid
        print(colored(f"Invalid URL: {test_url}", "red"))
