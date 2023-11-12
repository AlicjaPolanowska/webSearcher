import urllib.request
from html.parser import HTMLParser

class HTMLFilter(HTMLParser):
    text = ""
    def handle_data(self, data):
        self.text += data


def read_url(url: str):
    with urllib.request.urlopen(url) as response:
        html = response.read()
        try:
            return html.decode("utf-8")
        except:
            return None


def get_page_hrefs(page: str, splitter: str = '\n'):
    if page is None:
        return None
    return set(x[x.index('href="http')+6:x.index('"', x.index('href="http')+6)] for x in page.split(splitter) if x.find('href="http') > -1)


def plain_text_from_html(page:str) -> str:
    if page is None:
        return None
    f = HTMLFilter()
    f.feed(page)
    return f.text
