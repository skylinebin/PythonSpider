# -*- coding: utf-8 -*-
'''
Created on 2016年8月21日
HTML解析器
Updated 2020年5月19日

只需要对外提供解析HTML的功能
@author: SkylineBin
'''
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse
from urllib.parse import urljoin


class HtmlParser(object):
        
    def _get_new_urls(self, page_url, soup):
        # print('hahah',page_url)
        new_urls = set()
        # /item/洋葱网络/7680393
        links = soup.find_all('a', href=re.compile(r"/item/."))
        # links = soup.find_all('a', target="_blank")
        # print(links)
        #利用正则匹配获取所有页面里按照相应格式的链接
        for link in links:
            new_url = link['href']
            # print(new_url)
            new_full_url = urljoin(page_url, new_url)
            #按照 page_url 的格式把 new_url 拼接成一个全新的 URL
            new_urls.add(new_full_url)
            # print(new_full_url)
        
        return new_urls
    #可以获取到页面中所有词条的URL

    
    #获取数据
    def _get_new_data(self, page_url, soup):
        res_data = {}
        #将解析所得的数据存入数据字典中
        
        #存放url
        res_data['url'] = page_url
        
        #按照格式解析标题
        #<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node.get_text()
        # print(title_node.get_text())
        #存入字典的标题中
        
        #按照格式解析内容
        #<div class="lemma-summary" label-module="lemmaSummary">
        
        summary_node = soup.find('div', class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()
        #存入字典的数据中
        
        # print(res_data)
        return res_data
        
    
    
    def parse(self, page_url, html_cont):
        
        if page_url is None or html_cont is None:
            return
        
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        
        new_urls = self._get_new_urls(page_url, soup)
        
        #解析新的URL
        new_data = self._get_new_data(page_url, soup)
        #解析出URL对应的数据
        return new_urls, new_data
    
    
    



