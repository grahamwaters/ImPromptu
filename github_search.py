import requests
from bs4 import BeautifulSoup
import json

# Use requests to access the GitHub API and search for repositories containing "chatgpt" in the name
# url = "https://api.github.com/search/repositories?q=chatgpt+in:name"
url = "https://api.github.com/search/repositories?q=chatgpt+in:readme"
response = requests.get(url)

# Parse the JSON response
data = json.loads(response.text)

# Iterate through the list of repositories and store the URLs in a list
repo_urls = []
for repo in data["items"]:
    repo_urls.append(repo["html_url"])

# save repo_urls to a file
with open("repo_urls.txt", "w") as f:
    for url in repo_urls:
        f.write(url + "\n")

# Iterate through each repository URL and use Beautiful Soup to scrape the contents of the page
for url in repo_urls:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    # Use Beautiful Soup to find specific elements on the page (e.g. file names containing "prompts")
    # and store the data in a list
    prompts = []
    for element in soup.find_all("a", class_="js-navigation-open"):
        if "prompts" in element.text:
            prompts.append(element.text)

# Print the list of prompts
print(prompts)
