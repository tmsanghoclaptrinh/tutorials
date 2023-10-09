# Import library
import requests
from googlesearch import search

# Enter your query
query = input("Enter your query: ")

# Get article links from Google Search
article_links = search(query, stop=10)

# Print the links
for link in article_links:
    print(link)
