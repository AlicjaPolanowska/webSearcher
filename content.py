import urllib.request


def read_url(url: str):
    with urllib.request.urlopen(url) as response:
        html = response.read()
        return html.decode("utf-8")


def get_page_hrefs(page: str, splitter: str = '\n'):
    return set(x[x.index('href="http')+6:x.index('"', x.index('href="http')+6)] for x in page.split(splitter) if x.find('href="http') > -1)
