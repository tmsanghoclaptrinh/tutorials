# Import library
import requests

# Create a GET request to the web page
response = requests.get("https://learnpython.org")

# Get the response
html = response.text

# Print html
print(html)