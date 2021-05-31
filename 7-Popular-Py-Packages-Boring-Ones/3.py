# web scraping

import requests
from bs4 import BeautifulSoup

response = requests.get("https://stackoverflow.com/questions")
soup = BeautifulSoup(response.text, "html.parser")

questions = soup.select(".question-summary")
# check out questions[0].attrs
print(questions[0].get("id", 0))

print(questions[0].select(".question-hyperlink"))
print("sample " + questions[0].select_one(".question-hyperlink").getText())