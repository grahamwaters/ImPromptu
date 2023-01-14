# # https://github.com/f/awesome-chatgpt-prompts/network/members
# go to each of the fork urls at the url above and scrape the readme.md file for the prompts.

import requests
from bs4 import BeautifulSoup
import json

# Use requests to access the GitHub API and search for repositories containing "chatgpt" in the readme file
url = "https://github.com/f/awesome-chatgpt-prompts/network/members"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find all the fork URLs on the page
fork_urls = []
for element in soup.find_all("a", class_="muted-link"):
    if "Forks" in element.text or 'chatgpt' in element.text:
        fork_urls.append(element["href"]) # element["href"] is the URL of the fork
        print(element["href"])


# save the links to a file
with open("fork_urls.txt", "w") as f:
    for url in fork_urls:
        f.write(url + "\n")

# Iterate through each fork URL and scrape the contents of the "readme.md" file
# prompts = []
# for fork_url in fork_urls:
#     readme_url = fork_url + "/readme.md"
#     readme_response = requests.get(readme_url)
#     readme_soup = BeautifulSoup(readme_response.content, "html.parser")
#     # Use Beautiful Soup to find specific elements on the page (e.g. file names containing "prompts")
#     # and store the data in a list
#     for element in readme_soup.find_all("p"):
#         if "prompts" in element.text:
#             prompts.append(element.text)

# Print the list of prompts
# print(prompts)
