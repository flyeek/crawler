import url_manager
import html_downloader
import html_parser
import html_outputer
from sys import path

class CrawlerMain() :
    def __init__(self) :
        self.url_manager = url_manager.UrlManager()
        self.html_downloader = html_downloader.HtmlDownloader()
        self.html_parser = html_parser.HtmlParser()
        self.html_outputer = html_outputer.HtmlOutputer()

    def crawl(self, baseUrl, result_max_count) :
        data_count = 0
        failed_url_count = 0

        self.url_manager.add_url(baseUrl)
        while self.url_manager.has_pending_url() :
            try :
                target_url = self.url_manager.get_url()

                html_content = self.html_downloader.download_html(target_url)
                urls, data = self.html_parser.parse_html(target_url, html_content)

                self.url_manager.add_urls(urls)
                self.html_outputer.collect_data(data)

                data_count += 1
                if data_count >= result_max_count :
                    break
            except Exception, e:
                failed_url_count += 1

        self.html_outputer.output_html('crawle_result.html')
        print 'fail count = %d' % (failed_url_count)
        print 'success count = %d' % (data_count)


if __name__ == '__main__' :
    startUrl = 'http://baike.baidu.com/view/21087.htm'
    crawle_count = 100
    crawler_main = CrawlerMain()
    crawler_main.crawl(startUrl, crawle_count)
