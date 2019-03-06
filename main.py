import os
import re
import argparse

import requests
from dotenv import load_dotenv

load_dotenv()


def get_authorization_headers(token):
    return {
        "Authorization": "Bearer {}".format(token)
    }


# сделаем функцию внутренней
def _generate_api_url(end_point, host='https://api-ssl.bitly.com/v4'):
    return os.path.join(host, end_point)


def shorten(long_url, token, additional_parameters=None):
    end_point = "shorten"
    url = _generate_api_url(end_point)

    headers = get_authorization_headers(token)

    parameters = additional_parameters or {}
    parameters['long_url'] = long_url

    response = requests.post(url, headers=headers, json=parameters)
    link = response.json()['link'] if response.ok else None
    return link


def clicks(bitlink, token, additional_parameters=None):
    prepared_bitlink = re.sub('http[s]?://', '', string=bitlink)
    end_point = "bitlinks/{bitlink}/clicks/summary".format(bitlink=prepared_bitlink)
    url = _generate_api_url(end_point)

    headers = get_authorization_headers(token)

    parameters = {}
    parameters.update(additional_parameters or {})
    response = requests.get(url, headers=headers, json=parameters)
    total_clicks = response.json()['total_clicks'] if response.ok else None
    return total_clicks


def get_user_input():
    print("Insert url or bitlink: ")
    return input()


def parse_input():
    parser = argparse.ArgumentParser(description="program create bitlink from URL or show statisticks for bitlink")
    parser.add_argument("link", help="pass URL or bitlink")
    args = parser.parse_args()
    return args.link


def main():
    # "http://bit.ly/2TgAkTE" -> https://google.com
    token = os.getenv("BITLY_TOKEN")
    lnk = parse_input()
    result = shorten(lnk, token) or clicks(lnk, token) or None
    result = result if result else 'Your link "{}" is wrong. Try again'.format(lnk)
    print(result)


if __name__ == '__main__':
    main()
