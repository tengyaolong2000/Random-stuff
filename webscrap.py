import bs4
import requests

res = requests.get('https://www.amazon.sg/Automate-Boring-Stuff-Python-Sweigart/dp/1593275994')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
elems = soup.select('#buyNewSection > div > div > span > span')
print(elems[0].text)
