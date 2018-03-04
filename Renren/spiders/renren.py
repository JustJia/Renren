# -*- coding: utf-8 -*-
import scrapy

# 方式一：通过FormRequest类实现模拟登陆：该方式只能通过重写start_requests方法修改请求才能实现
class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/PLogin.do']
    # 重写start_requests方法:因start_requests方法默认是get请求，此时需要重写将其改成post请求
    def start_requests(self):
        # 构造post请求参数
        data = {
            'email':'账号',
            'password':'密码'
        }
        # 发送请求
        yield scrapy.FormRequest(url=self.start_urls[0],formdata=data)

    def parse(self, response):
        with open('renren.html','wb') as f:
            f.write(response.body)
