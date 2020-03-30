import scrapy
from scrapy import cmdline
from urllib.parse import urljoin
import datetime
import test_dev.items


class PycoderSpider(scrapy.Spider):
    name = "pycoder"
    visited_urls = []
    start_urls = [
        'https://www.wildberries.ru/catalog/obuv/zhenskaya/sabo-i-myuli/myuli?page=1',
    ]

    def parse(self, response):
        if response.url not in self.visited_urls:
            self.visited_urls.append(response.url)
            for post_link in response.xpath(
                    '//div[@class="dtList i-dtList j-card-item"]/span/span/span/a/@href').extract():
                url = urljoin(response.url, post_link)
                yield response.follow(url, callback=self.parse_post)

            next_pages = response.xpath(
                    '//div[@class="pageToInsert"]/a/@href').extract()
            next_page = next_pages[-1]

            next_page_url = urljoin(response.url+'/', next_page)
            yield response.follow(next_page_url, callback=self.parse)

    def parse_post(self, response):
        item = test_dev.items.PycoderItem()

        # ______TIMESTAMP______ #
        timestamp = str(datetime.datetime.today())
        item['timestamp'] = timestamp

        # ______RPC______ #
        RPC = response.xpath(
            '//div[contains(@class, "article")]/span/text()').extract()
        item['RPC'] = str(RPC).replace(' ', '').replace('[', '').replace(']', '').replace("'", '')
        # _______________ #

        # ______URL______ #
        url = str(response.url)
        item['url'] = url
        # _______________ #

        # ______TITLE______ #
        title = response.xpath(
            '//div[contains(@class, "brand-and-name j-product-title")]/span/text()').extract()
        item['title'] = str(title).replace(' ', '').replace('[', '').replace(']', '').replace("'", '').replace(',', '/')
        # __________________ #

        # ______MARKETING_TAGS______ #
        marketing_tags = 'No tags'
        item['marketing_tags'] = str(marketing_tags)
        # __________________________ #

        # _______BRAND_______ #
        brand = response.xpath(
            '//div[contains(@class, "brand-and-name j-product-title")]/span/text()').extract()
        item['brand'] = str(brand).replace(' ', '') \
            .replace('[', '').replace(']', '').replace("'", '').split(',').pop(0)
        # __________________ #

        # _______SECTION_______ #
        section = response.xpath(
            '//div/ul[@class="bread-crumbs"]/li/a/span[@itemprop="title"]/text()').extract()
        item['section'] = str(section).replace('[', '').replace(']', '').replace("'", '').split(',')
        # _____________________ #

        # ____PRICE_DATA____ #
        current = response.xpath('//div[@class="final-price-block"]/span/text()').extract()
        original = response.xpath('//span[@class="old-price"]/del/text()').extract()
        sale_tag = response.xpath('//p[@class="economy"]/span[@class="discount-tooltipster-value"]/text()').extract()
        item['price_data'] = {
            'current': str(current).replace(' ', '').replace('\\n', '').replace('\\xa0', '').replace('₽', '') \
                .replace('[', '').replace(']', '').replace("'", ''),
            'original': str(original).replace(' ', '').replace('\\n', '').replace('\\xa0', '').replace('₽', '') \
                .replace('[', '').replace(']', '').replace("'", ''),
            'sale_tag': str(sale_tag).replace(' ', '').replace('\\n', '').replace('\\xa0', '').replace('₽', '') \
                .replace('[', '').replace(']', '').replace("'", '')
        }
        # __________________ #

        # _______STOCK_______ #
        in_stock = True
        count = None
        item['stock'] = {
            'in_stock': in_stock,
            'count': count
        }
        # __________________ #

        # ____ASSETS____ #
        main_image = response.xpath('//div[@class="MagicZoomBigImageCont'
                                    ' inner-zoom opacity-transition"]/div/img/@src').extract()
        set_images = response.xpath('//div[@class="MagicZoomBigImageCont'
                                    ' inner-zoom opacity-transition"]/div/img/@src').extract()

        item['assets'] = {
            'main_image': str(main_image).replace('[', '').replace(']', '').replace("'", ''),
            'set_images': str(set_images).replace('[', '').replace(']', '').replace("'", ''),
            'view360': [],
            'video': []
        }
        # _______________ #

        # ____METADATA____ #
        description = response.xpath('//div[contains(@class, "j-add-info-section")]/div/div/span/b/text()').extract()
        desc_item = response.xpath('//div[contains(@class, "j-add-info-section")]/div/div/span/text()').extract()
        article = response.xpath('//div[contains(@class, "article")]/span/text()').extract()

        item['metadata'] = {
            'description': str(description).replace('[', '').replace(']', '').replace("'", ''),
            'desc_item': str(desc_item).replace('[', '').replace(']', '').replace("'", ''),
            'article': str(article).replace('[', '').replace(']', '').replace("'", '')
        }
        # ________________ #

        yield item


# cmdline.execute("scrapy crawl pycoder".split())
