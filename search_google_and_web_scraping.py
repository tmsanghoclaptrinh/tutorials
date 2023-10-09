# Import library
import requests
from googlesearch import search

# Enter your query
query = input("Enter your query: ")

# Get the first article link from Google Search
article_links = search(query, stop=1)
link=next(article_links)

# Print the link
print(f"The first article link: {link}")

# Create a GET request to the web page
response = requests.get(link)

# Get the response
html = response.text

# Print html
print(html)