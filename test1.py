# -*- coding: utf-8 -*-
a='''
                                        女生的内裤应该怎么洗-一定要手洗


	现在很多人洗衣服都喜欢用洗衣机，有时候还会把内裤一起丢进洗衣机洗，这是非常不卫生的一种做法，一是因为洗衣机里面有很多细菌，二是如果把内裤把其他衣服、袜子等一起洗的话很可能会导致交叉感染，所以建议大家洗内裤一定要手洗，千万不要偷懒哦!





https://pic.qbaobei.com/Uploads/Editor/2017-10-30/59f70f994279c.jpg

                                        女生的内裤应该怎么洗-每天清洗


	内裤一定要每天清洗，不要堆积很多内裤再一次性清洗，这样很容易使得内裤上的分泌物滋长更多的细菌，进而影响我们的身体健康，同时也加重了洗涤的难度，所以内裤换下来最好及时用水清洗干净。





https://pic.qbaobei.com/Uploads/Editor/2017-10-30/59f70fa37bfa1.jpg

                                        女生的内裤应该怎么洗-正确选择洗涤剂


	女生的私处都比较较弱，且女生阴道是一个弱酸环境，清洁用品一般都是碱性的，所以我们要选碱性不要太强、清洁能力比较好的清洁剂，比如肥皂，或者有杀菌消毒能力的肥皂。很多女孩为了把贴身衣物洗干净，往往用了太多洗衣剂，反而造成残留，引发皮肤过敏问题。





https://pic.qbaobei.com/Uploads/Editor/2017-10-30/59f70faeef6c3.jpg

                                        女生的内裤应该怎么洗-搓洗不能少于3分钟


	有很多人洗内裤都是匆匆地用清水冲一冲就完事，这样洗是不能完全把内裤洗干净的，建议选用专用清洗内裤的肥皂，用手轻轻揉搓内裤，让肥皂液与内裤上的细菌充分接触，搓完再用清水把泡沫冲洗干净，这样才能彻底洗净内裤。





	12
https://pic.qbaobei.com/Uploads/Editor/2017-10-30/59f70fbb0aff1.jpg
'''


import re
res=re.findall('.*?(http.*jpg).*?',a)
print res
img_path = ['123123',
            '234234',
            '345345',
            '456456']



for i in range(len(res)):
    b=re.sub(res[i],img_path[i],a)
    a=b

print(a)