# -*- coding: utf-8 -*-
import scrapy

# 方式二：通过formRequest.from_response类方法实现模拟登陆：该方式是通过请求响应自动获取表单的post链接，然后再返回一个FormRequest请求。
class RenrenFormSpider(scrapy.Spider):
    name = 'renren_form'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    def parse(self, response):
        # 构造请求参数
        data = {
            'email': '账号',
            'password': '密码'
        }
        # 发送请求
        yield scrapy.FormRequest.from_response(response=response,formdata=data,callback=self.parse_login)
    def parse_login(self,response):
        with open('renren1.html','wb') as f:
            f.write(response.body)