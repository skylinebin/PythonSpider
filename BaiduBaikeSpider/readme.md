## 更新版本说明  
- 将 Python 版本从 Python2.7 更新到 Python3.5+
- 更新了新版本的百度百科链接规则

### 所需额外安装的Python库
- bs4 :(Shell: pip install bs4) 
- requests :(Shell: pip install requests) 


### 更新后的百度百科数据词条  

目标地址：https://baike.baidu.com/item/Python/407313
URL格式：
   词条页面URL格式：/item/Python/407313
   外部页面的URL格式：/item/教学

数据格式：

标题格式：
```
<dd class="lemmaWgt-lemmaTitle-title"></dd>
```

简介正文格式：
```
<div class="lemma-summary" label-module="lemmaSummary">
</div>
```

页面编码：
```
<meta charset="UTF-8">
```
