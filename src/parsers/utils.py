import requests
from bs4 import BeautifulSoup


def get_page (url: str) -> BeautifulSoup:
    """
    Get the page content from the given URL

    :param url: URL to get the page content from
    :return: BeautifulSoup object
    """
    page = requests.get(url)
    return BeautifulSoup(page.content, 'html.parser')
