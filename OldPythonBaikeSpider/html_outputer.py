# coding:utf8
'''
Created on 2016年8月21日
html 输出部分

输出成html文件
@author: Liubin
'''


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
        
    
    
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)
        #收集数据
        
    
    def output_html(self,):
        fout = open('output.html', 'w')
        
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
#             print data['summary'].encode('utf-8')
            fout.write("</tr>")
        
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        
        #输出HTML文件
    
    
    
    



