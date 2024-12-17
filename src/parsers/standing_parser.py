from typing import List

from src.models.standing import Standing
from src.parsers import utils
from bs4 import BeautifulSoup


class StandingParser:
    def __init__ (self, config: dict):
        self.config = config

    def parse (self, year: int) -> list[Standing]:
        """
        Parse the standings for the given year

        :param year: Year to get the standings for
        :return: List of standings
        """

        # Get the page content
        url: str = self.config['api']['base_url'] + self.config['api']['endpoints']['standings']
        page: BeautifulSoup = utils.get_page(url.replace('{year}', str(year)))

        # Get the table
        table = page.find('table', attrs={'class': 'f1-table'})
        tbody = table.find('tbody')
        rows = tbody.find_all('tr')

        # Get the standings
        standings: List[Standing] = []
        for row in rows:
            columns = row.find_all('td')

            # Get the full name
            names = columns[1].find_all('span')
            full_name = names[0].text + ' ' + names[1].text

            # Create the standing object
            standing = Standing(
                position=int(columns[0].text),
                driver=full_name,
                nationality=columns[2].text,
                constructor=columns[3].text,
                points=int(columns[4].text),
            )

            standings.append(standing)

        return standings
