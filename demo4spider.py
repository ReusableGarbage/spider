from multiprocessing import pool
import bs4 as bs
import random
import requests
import string

# making a change for practice on github

def random_starting_url():
    starting = ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(3))
# everything inside join gets joined by separator ('')
# random.SystemRandom generates random numbers from sources provided by OSError
# choice returns random item from list, tuple, or a string. In this case it will return lowercase characters for the range of 3.
    url = ''.join(['http://', starting, '.com'])
    return url

# this is how to get a random url. We want to create a spider that finds all the links on that website and so on.

def handle_local_links(url,link):
    if link.startswith('/'):
        return ''.join([url, link])
    else:
        return link

def get_links(url):
    try:
        resp = requests.get(url) # gets contents of randomly generated url
        soup = bs.BeautifulSoup(resp.text, 'lxml') # resp.text converts contents of randomly generated url to text. .text belongs to requests. 'lxml' is specifying what parser to use.
        body = soup.body # .body belong to the beautiful soup module and is used to navigate
        links = [link.get('href') for link in body.find_all('a')] # .find_all belongs to the beautiful soup and looks for tags. 'a' is a tag used for urls
        links = [handle_local_links(url,link) for link in links] # this deals with local links
        links = [str(link.encode("ascii")) for link in links]
        return links #returns list of lists on any given url

    except TypeError as e:
        print(e)
        return []
    except IndexError as e:
        print(e)
        return[]
    except AttributeError as e:
        print(e)
        return[]
    except Exception as e:
        print(str(e))

def main():
    how_many = 50
    p = pool(processes=how_many)
    parse_us = [random_starting_url() for _ in range(how_many)]
    data = p.map(get_links [link for link in parse_us])
    data = [url for url_list in data for url in url_list]
    p.close()

    with open('D:\\intermediate\\urls.txt', 'w') as f:
        f.write(str(data))

in __name__ == '__main__':
    main()
