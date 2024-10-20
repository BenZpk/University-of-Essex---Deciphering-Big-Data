#Web Scraping Project Unit 3

#Import important libraries
import requests
from bs4 import BeautifulSoup
import json

# URL to scrape
url = 'https://de.wikipedia.org/wiki/Data_Science'
word = "Data Scientist"

# Parse the HTML content of the page
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

#Retreive the text from the page
text = soup.get_text().lower()
word_count = text.count(word.lower())

#Creation of the JSON structure
data = {
'url': url,
'word': word,
'word count': word_count
}

#Finally parsing to a JSON file
with open('word_occurence_count.json', 'w') as f:
    json.dump(data, f, indent=4)
