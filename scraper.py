import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/newest')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
votes = soup.select('.score')


def create_custom_hacker_news(links, votes):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href',None)
        points = int(votes[idx].getText().replace(' points', ''))

        hn.append({'title': title, 'link': href})

    return hn


print(create_custom_hacker_news(links, votes))
