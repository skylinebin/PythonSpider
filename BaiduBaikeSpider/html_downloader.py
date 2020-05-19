# -*- coding: utf-8 -*-
'''
Created on 2016年8月21日
HTML下载器

Updated 2020年5月19日

只需要实现下载功能
最简单的方法
@author: SkylineBin
'''
import urllib.request


class HtmlDownloader(object):
    
    def download(self, url):
        print('url',url)
        if url is None:
            return None
        
        response = urllib.request.urlopen(url)
        
        if response.getcode() != 200:
            return None
        return response.read()
        
    
    
    



