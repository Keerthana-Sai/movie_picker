import random
import requests 
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/top/'

def main():
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    #soup = BeautifulSoup(response.text, 'lxml') #faster
    #  print(soup.prettify())
    movietags = soup.select('td.titleColumn')
    inner_movietags = soup.select('td.titleColumn a')
    ratingtags =  soup.select('td.posterColumn span[name=ir]')
    def get_year(movie_tag):
        moviesplit = movie_tag.text.split()
        year = moviesplit[-1]
        return year

    years = [get_year(tag) for tag in movietags]
    actors_list =[tag['title']for tag in inner_movietags]
    titles = [tag.text for tag in inner_movietags]
    ratings = [float(tag['data-value']) for tag in ratingtags]

    n_movies = len(titles)
    print(n_movies)
    #while(True):
    idx = random.randrange(0, n_movies)

    print(f'{titles[idx]}, rating: {ratings[idx]:.1f}, starring: {actors_list[idx]}')

    #user_input = input('Do you want another movie (y/[n])? ')
    #if user_input != 'y':
         #break




if __name__ == '__main__':
    main()