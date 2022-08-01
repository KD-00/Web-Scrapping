from bs4 import BeautifulSoup 
import requests
from csv import writer

try:
	url='https://www.imdb.com/chart/top/'
	source=requests.get(url)
	source.raise_for_status()     

	soup=BeautifulSoup(source.content,'html.parser')  
	mov=soup.find('tbody',class_='lister-list') 
	movies=mov.find_all('tr')  

	with open('IMDBmovie.csv','w',encoding='utf8',newline='') as f:
		thewriter = writer(f)
		header=['Rank', 'Name', 'Year', 'Rating']
		thewriter.writerow(header)

		for movie in movies:
	
			name=movie.find('td',class_='titleColumn').a.text 
			rank=movie.find('td',class_='titleColumn').get_text(strip=True).split('.')[0] 
			year=movie.find('td',class_='titleColumn').span.text.strip('()')
			rating=movie.find('td',class_='ratingColumn imdbRating').strong.text
		
			info=[rank, name, year, rating]
			thewriter.writerow(info)
	print("Finished Successfully")

except Exception as e:
	print(e)