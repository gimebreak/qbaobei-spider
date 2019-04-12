from qbaobei.spiders.QBabyTest import etree,requests
import re
def get_content(urls):
    total_content_list = []
    total_image_urls = []

    for url in urls:
        temp = requests.get(url)
        xml = etree.HTML(temp.content)
        div_list = xml.xpath("//div[@class='detail-area']/div")
        content_list = map(lambda x: x.xpath('string(.)'), div_list)
        image_urls = xml.xpath("//div[@class='detail-area']//img/@src")
        total_content_list += content_list
        total_image_urls += image_urls

    merge = zip(total_content_list, total_image_urls)
    list_content = map(lambda x: list(x), merge)
    reduced_list = reduce(lambda x, y: x + y, list_content)
    content_text = '\n'.join(reduced_list)

    content_text = re.sub('\s+(12)\s+','  ',content_text)
    return content_text, total_image_urls


urls=['http://www.qbaobei.com/jiankang/1184662.html',
     'http://www.qbaobei.com/jiankang/1184662_2.html']


with open('test.txt','wb+') as f:
    content_text,urls=get_content(urls)
    f.write(content_text.encode('utf-8'))
