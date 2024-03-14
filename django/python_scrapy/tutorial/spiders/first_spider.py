from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "amazon"

    def start_requests(self):
        
        # for i in range(1,21):
        #     urls = [
        #         f"https://www.amazon.in/s?k=headphones&page={i}",
        #     ]
            
        urls = []
        for i in range(1, 101):
            urls.append(f"https://www.amazon.in/s?k=headphones&page={i}")
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            
    def parse(self,response):
        names=response.css(".a-color-base.a-text-normal::text").getall()
        for i in names:
            with open("amazon_names.txt","a") as f:
                f.write(i+"\n")

    