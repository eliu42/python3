from bs4 import BeautifulSoup
import requests

# Will this work tomorrow? How do I non explicitly get class names?

URL = 'https://www.dictionary.com/e/word-of-the-day/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')


wotd_container = soup.find(class_='wotd-item-headword__word')
definition_container = soup.find(class_='wotd-item-headword__pos')

wotd = wotd_container.text
definition = definition_container.text
print('The word of the day is: ',  wotd.strip(), ': ', definition.strip())
