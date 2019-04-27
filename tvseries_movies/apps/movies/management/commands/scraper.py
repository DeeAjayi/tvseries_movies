import requests
from bs4 import BeautifulSoup as bs
from requests.exceptions import SSLError

each_data = {}


def get_page(url):
    request = requests.get(url)
    content = request.content.decode('utf-8')
    page = bs(content, 'html.parser')
    return page


def get_movies(year):
    url = f'https://yts.am/browse-movies/{year}/all/all/0/latest'
    page = get_page(url)
    num_of_movies = int(str(page.find('h2')).split(' ')[0][4:].replace(',', ''))
    num_of_pages = ((num_of_movies // 20) + 1)
    movies_url_list = []

    for movie in page.findAll('a', {'class': 'browse-movie-link'}):
        movies_url_list.append(movie['href'])

    page_no = 0

    while page_no <= num_of_pages:
        page = get_page(f'https://yts.am/browse-movies/{year}/all/all/0/latest?page={page_no}')
        page_no += 1

        for movie in page.findAll('a', {'class': 'browse-movie-link'}):
            movies_url_list.append(movie['href'])

    return movies_url_list


def get_movie_details(movies_list):

    for movie_url in movies_list:
        try:
            page = get_page(movie_url)
            info_container = page.find('div', {'id': ['movie-info']})
            title = info_container.div.h1.text
            image_url = page.find('div', {'id': ['movie-poster']}).find('img')['src']
            url = movie_url
            year = int(info_container.div.h2.text)
            download_urls = info_container.p.findAll('a')
            download_urls_info = {}
        except AttributeError:
            f = open('error.txt', 'a+')
            f.write(movie_url + '\n')
            f.close()
            continue
        except SSLError:
            cont_index = movies_list.index(movie_url)
            get_movie_details(movies_list[cont_index:])

        for each_url in download_urls:
            download_urls_info[each_url.text] = each_url['href']

        youtube_url = page.find('div', {'class': 'screenshot'}).a['href']
        imdb_rating = float(page.find('span', attrs={'itemprop': 'ratingValue'}).text)

        data = {
            title:
                {
                    "title": title,
                    "url": url,
                    "year": year,
                    "image_url": image_url,
                    "trailer_url": youtube_url,
                    "rating": imdb_rating,
                    "download_urls_info": download_urls_info
                }
        }

        each_data.update(data)

    return each_data

