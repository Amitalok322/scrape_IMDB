import csv
import requests
from bs4 import BeautifulSoup

source = requests.get('https://www.imdb.com/chart/top/')
source.raise_for_status()
soup = BeautifulSoup(source.text, 'html.parser')

movies = soup.find('tbody', class_='lister-list').find_all('tr')

with open('top_movies.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Rank', 'Name', 'Year', 'Rating'])
    
    for movie in movies:
        name = movie.find('td', class_='titleColumn').a.text
        rank = movie.find('td', class_='titleColumn').get_text(strip=True).split('.')[0]
        year = movie.find('td', class_='titleColumn').span.text.strip('()')
        rating = movie.find('td', class_='ratingColumn imdbRating').strong.text
        writer.writerow([rank, name, year, rating])
