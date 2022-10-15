# We create shortern URL using Bitly service.
# Generate it's access token.

# POST

import pyshorteners
long_url = input("Enter the long URL:")
obj = pyshorteners.Shortener(api_key='******************')
short_url = obj.bitly.short('https://www.google.com/ABC/xyz/24243253254-244/ABC')
print("The Shortened URL is: " + short_url)

# GET
long_url = obj.bitly.expand('https://bit.ly/TESTING')
print(long_url)