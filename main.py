import scrapy


class ProxySpider(scrapy.Spider):
    name = 'proxy_spider'
    start_urls = ['https://free-proxy-list.net/']

    def parse(self, response):
        for proxy in response.xpath('*//tbody/tr'):

            proxy_selector = 'td[1]//text()'
            port_selector = 'td[2]//text()'

            with open('proxy.txt', 'a+') as f:
                proxy_final = proxy.xpath(proxy_selector).extract_first()
                port_final = proxy.xpath(port_selector).extract_first()
                f.write('{}:{}\n'.format(proxy_final, port_final))

            yield {
                'proxy': proxy.xpath(proxy_selector).extract_first(),
                'port': proxy.xpath(port_selector).extract_first(),
            }
