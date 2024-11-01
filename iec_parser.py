# parser/iec_parser.py

from bs4 import BeautifulSoup
import requests
from config import URLS, ELEMENTS

def parse_iec_page(url, element):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:129.0) Gecko/20100101 Firefox/129.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection': 'keep-alive',
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'lxml')
    except requests.RequestException:
        return None

    tag = None
    if element == 'title':
        tag = soup.find("a", id="tdashsub_wg")
    elif element == 'name':
        tag = soup.find("td", style="white-space:nowrap;")
    elif element == 'description':
        tag = soup.find("td", class_="title-description")
    elif element == 'project':
        tag = soup.find("div", id="list-relpro")
    elif element == 'project2':
        project2_elements = soup.find_all("div", class_="dash-inner-txt")
        tag = project2_elements[1] if len(project2_elements) > 1 else None
    elif element == 'publication':
        publication_div = soup.find("div", id="PROJ_INIT_DATE")
        tag = publication_div.find_all("tr")[1].find_all("td")[-1] if publication_div else None

    return tag.get_text(strip=True) if tag else "-"
