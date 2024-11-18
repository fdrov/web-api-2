import os
from urllib.parse import urlparse
import argparse

from dotenv import load_dotenv
import requests


def shorten_link(token: str, url: str) -> str:
    api_method = "https://api.vk.ru/method/utils.getShortLink"
    params = {
        "v": "5.199",
        "access_token": token,
        "url": url,
    }
    response = requests.get(url=api_method, params=params)
    response.raise_for_status()
    parsed_response = response.json()
    if "error" in parsed_response:
        raise ValueError(parsed_response["error"]["error_msg"])
    short_link = parsed_response["response"]["short_url"]
    return short_link


def count_clicks(token, link):
    api_method = "https://api.vk.ru/method/utils.getLinkStats"
    path = urlparse(link).path.strip("/")
    params = {"v": "5.199", "access_token": token, "key": path, "interval": "forever"}
    response = requests.get(url=api_method, params=params)
    response.raise_for_status()
    parsed_response = response.json()
    if "error" in parsed_response:
        raise ValueError(parsed_response["error"]["error_msg"])
    clicks_count = parsed_response["response"]["stats"][0]["views"]
    return clicks_count


def is_shorten_link(token, url):
    api_method = "https://api.vk.ru/method/utils.getLinkStats"
    path = urlparse(url).path.strip("/")
    params = {"v": "5.199", "access_token": token, "key": path, "interval": "forever"}
    response = requests.get(url=api_method, params=params)
    response.raise_for_status()
    parsed_response = response.json()
    return not "error" in parsed_response


def main():
    load_dotenv()
    vk_service_token = os.environ["VK_SERVICE_TOKEN"]

    try:
        parser = argparse.ArgumentParser(
            description="Скрипт сократит ссылку или покажет количество просмотров уже сокращенной"
        )
        parser.add_argument("url", help="Обычная или уже сокращенная ссылка")
        args = parser.parse_args()
        url = args.url

        if is_shorten_link(vk_service_token, url):
            print("Кликов: ", count_clicks(vk_service_token, url))
        else:
            print("Сокращенная ссылка: ", shorten_link(vk_service_token, url))
    except requests.exceptions.HTTPError as err:
        print("Произошла HTTP ошибка:", err)
    except ValueError as err:
        print("Проверьте правильность ссылки:", err)
    except IndexError:
        print("Повторите запрос")


if __name__ == "__main__":
    main()
