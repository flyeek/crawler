import urllib2


class HtmlDownloader:
    def __init__(self):
        pass

    @staticmethod
    def download_html(url):
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()
