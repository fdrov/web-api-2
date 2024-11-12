import os
from urllib.parse import urlparse

from dotenv import load_dotenv
import requests

load_dotenv()

token = os.environ['TOKEN']


def shorten_link(token: str, url: str) -> str:
    api_method = 'https://api.vk.ru/method/utils.getShortLink'
    params = {
        'v': '5.199',
        'access_token': token,
        'url': url,
    }
    response = requests.get(url=api_method, params=params)
    response.raise_for_status()
    parsed_response = response.json()
    if 'error' in parsed_response:
        raise ValueError(parsed_response['error']['error_msg'])
    short_link = parsed_response['response']['short_url']
    return short_link


def count_clicks(token, link):
    api_method = 'https://api.vk.ru/method/utils.getLinkStats'
    path = urlparse(link).path.strip('/')
    params = {
        'v': '5.199',
        'access_token': token,
        'key': path,
        'interval': 'forever'
    }
    response = requests.get(url=api_method, params=params)
    response.raise_for_status()
    result = response.json()
    if 'error' in result:
        raise ValueError(result['error']['error_msg'])
    clicks_count = result['response']['stats'][0]['views']
    return clicks_count


def is_shorten_link(url):
    site = urlparse(url).netloc
    if site == 'vk.cc':
        return True
    return False


def main():
    try:
        url = input('Type your link:\n')
        if is_shorten_link(url):
            print('Кликов: ', count_clicks(token, url))
        else:
            print('Сокращенная ссылка: ', shorten_link(token, url))
    except requests.exceptions.HTTPError as err:
        print('There is an HTTP error:', err)
    except ValueError as err:
        print('ValueError', err)
    except IndexError:
        print('Please, retry the request')


if __name__ == '__main__':
    main()
