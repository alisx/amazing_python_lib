import scrapy

from myproject.items import BookItem

class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["book.douban.com"]
    start_urls = ["https://book.douban.com/"]
    
    def start_requests(self):
    
        cookies = {
            'bid': 'gCbkoQiRGPA',
            '__utmc': '30149280',
            'viewed': '"1053623_4171549_30194615_26435820_35594496_26877306_36473857"',
            'll': '"108288"',
            '_ga': 'GA1.2.1807824611.1708779278',
            '_gid': 'GA1.2.1474294118.1708779279',
            '_ck_desktop_mode': '1',
            'vmode': 'pc',
            '_ga_Y4GN1R87RG': 'GS1.1.1708779278.1.1.1708779292.0.0.0',
            'ap_v': '0,6.0',
            '_pk_ref.100001.3ac3': '%5B%22%22%2C%22%22%2C1708779303%2C%22https%3A%2F%2Fm.douban.com%2F%22%5D',
            '_pk_id.100001.3ac3': 'caed93afd17179ee.1708779303.',
            '_pk_ses.100001.3ac3': '1',
            '_vwo_uuid_v2': 'DDD15FCC4169920E307C95BB8F0656375|294e000ebcc63013b3cc11d6d6eb5228',
            '__yadk_uid': 'GAU0lvsVmgkjTGotlOIwBmB3mShFBVS6',
            '__utma': '30149280.25122012.1699801585.1705914889.1708779304.9',
            '__utmz': '30149280.1708779304.9.8.utmcsr=m.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
            '__utmb': '30149280.1.10.1708779304',
            '__utma': '81379588.1807824611.1708779278.1708779304.1708779304.1',
            '__utmc': '81379588',
            '__utmz': '81379588.1708779304.1.1.utmcsr=m.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
            '__utmb': '81379588.1.10.1708779304',
        }

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Referer': 'https://m.douban.com/',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
        }
        yield scrapy.Request(BooksSpider.start_urls[0], headers=headers, cookies=cookies, callback=self.parse)
        
    def parse(self, response):
        book_items = []
        
        li_elements = response.xpath('//*[@id="content"]/div/div[1]/div[1]/div[2]/div[1]/div/ul[2]/li')
        
        for li in li_elements:
            item = BookItem()
            item['title'] = li.xpath('.//div[@class="info"]/div[@class="title"]/a/text()').get()
            item['author'] = li.xpath('.//div[@class="info"]/div[@class="author"]/text()').get()
            item['year'] = li.xpath('.//div[@class="info"]/div[@class="more-meta"]/p/span[@class="year"]/text()').get()
            item['publisher'] = li.xpath('.//div[@class="info"]/div[@class="more-meta"]/p/span[@class="publisher"]/text()').get()

            book_items.append(item)

        return book_items
        pass
