import urllib.request


def read_url(url: str):
    with urllib.request.urlopen(url) as response:
        html = response.read()
        return html.decode("utf-8")


def get_page_hrefs(page: str, splitter: str = '\n', content: str = 'href'):
    return set(x for x in page.split(splitter) if x.find(content) > -1)
