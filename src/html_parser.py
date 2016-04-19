import re
import urlparse
from bs4 import BeautifulSoup


def _parse_data(soup, base_url):
    data_dict = dict()

    data_dict['url'] = base_url

    # <dd class="lemmaWgt-lemmaTitle-title">
    # <h1>Python</h1>
    title = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
    data_dict['title'] = title.get_text()

    # <div class="lemma-summary" label-module="lemmaSummary">
    summary = soup.find('div', class_="lemma-summary")
    data_dict['summary'] = summary.get_text()

    return data_dict


class HtmlParser:
    def __init__(self):
        pass

    @staticmethod
    def _parse_urls(soup, base_url):
        find_urls = set()

        # <a target="_blank" href="/view/130692.htm">GPL</a>
        urls = soup.find_all('a', href=re.compile(r'/view/\d+\.htm'))
        for url in urls:
            full_url = urlparse.urljoin(base_url, url['href'])
            find_urls.add(full_url)
        return find_urls

    def parse_html(self, base_url, content):
        soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
        urls = self._parse_urls(soup, base_url)
        data = _parse_data(soup, base_url)
        return urls, data
