class UrlManager:
    def __init__(self):
        self.pending_urls = set()
        self.crawled_urls = set()

    def has_pending_url(self):
        return len(self.pending_urls) != 0

    def add_url(self, url):
        if url is None or len(url) == 0:
            return
        if url in self.crawled_urls:
            return
        self.pending_urls.add(url)

    def add_urls(self, urls):
        for url in urls:
            self.add_url(url)

    def get_url(self):
        url = self.pending_urls.pop()
        self.crawled_urls.add(url)
        return url
