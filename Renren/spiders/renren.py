# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/PLogin.do']
    # 重写start_requests方法:因start_requests方法默认是get请求，此时需要重写将其改成post请求
    def start_requests(self):
        # 构造post请求参数
        data = {
            'email':'214578765@qq.com',
            'password':'MYSELF93542'
        }
        # 发送请求
        yield scrapy.FormRequest(url=self.start_urls[0],formdata=data)

    def parse(self, response):
        with open('renren.html','wb') as f:
            f.write(response.body)
