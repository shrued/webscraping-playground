import requests
from bs4 import BeautifulSoup

response = requests.get(
	url="https://en.wikipedia.org/wiki/Toronto_Stock_Exchange",
)
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find_all('table')
print(table)