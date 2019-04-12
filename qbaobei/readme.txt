1.http://www.qbaobei.com/jiankang/beiyun/hyzb/
读取menu_url
urls = response.xpath("//div[@class='second-nav']/a/@href").re('.*?beiyun/.+/').extract()   unicode
menu_name = urls=response.xpath("//div[@class='second-nav']/a/text()").extract()[1:]

页面文章
取单页文章节点
title_node= response.xpath('//ul[@class="list-conBox-ul"]/li')
一篇文章的tag
title_tag=title_node.xpath('div//span[@class="tipsm"]/a/text()')
所有文章tag
class_tag=map(lambda x:x.xpath('div//span[@class="tipsm"]/a/text()'),title_node)


title= response.xpath('//ul[@class="list-conBox-ul"]/li/a/@href').extract()
title_url = response.xpath('//ul[@class="list-conBox-ul"]/li/div/a/text()').extract()


进入文章:
content_html=response.xpath('//div[@class="detail-area"]')
content_text=content_html.xpath('string(.)').extract_first()

下一页url
http://www.qbaobei.com/jiankang/beiyun/hyzb/List_8.html


最后一页(停止遍历条件)
response.xpath('//div[@class="page"]/a[@class="end"]/text()').re('...(\d*)')[0]
