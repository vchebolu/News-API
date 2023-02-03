import requests

api_key = "1cd479676ea244cd8f9e244e1db52dfc"
url = f"https://newsapi.org/v2/everything" \
      f"?q=tesla&from=2023-01-03&sortBy=publishedAt" \
      f"&apiKey={api_key}"
# Make request
request = requests.get(url)

# content = request.text
# print(content)
# print(type(content))

# Get a dictionary with data
content = request.json()

# Get the article titles and description
for article in content["articles"]:
      print(article["title"])
