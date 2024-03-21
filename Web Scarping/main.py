from bs4 import BeautifulSoup
import requests
import csv

base_url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
res = requests.get(base_url, headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
})

soup = BeautifulSoup(res.content, 'html.parser')

names = soup.find_all('a', {'class': 'ipc-title-link-wrapper'})
rankings = soup.find_all('span', {'class':'ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating'}) 

file = open("scraped_movies.csv", "w")
writer = csv.writer(file)

writer.writerow(["TITLES", "RATINGS"])

for name,ranking in zip(names,rankings):
    print(name.text + ' - ' + ranking.text)
    writer.writerow([name.text, ranking.text])

file.close()