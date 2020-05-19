# -*- coding: utf-8 -*-
'''
Created on 2016年8月21日
URL管理器

Updated 2020年5月19日

URL管理器需要维护两个列表：
            待爬取的列表 
            已爬取的列表
@author: SkylineBin
'''


class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
        #初始化建立待爬取的列表和已爬取的列表
        
    def add_new_url(self, url):
        if url is None:
            return
        if (url not in self.new_urls) and (url not in self.old_urls):
            self.new_urls.add(url)

    def add_new_urls(self,urls):
        #判断urls列表是否为空，传进来参数先判断，好习惯！！
        if (urls is None) or (len(urls) ==0):
            return
        for url in urls:
            self.add_new_url(url)
            #对列表中的元素单个添加进new_urls中
            
    
    def has_new_url(self):
        return len(self.new_urls)!= 0

    
    def get_new_url(self):
        new_url = self.new_urls.pop() #从列表中获取一个URL 并移除这个URL
        self.old_urls.add(new_url)
        return new_url
    
    

    
    
    
    
    
    
    



