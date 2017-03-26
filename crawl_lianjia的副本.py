#-*-coding:utf-8-*-#
import requests
import lxml.html
import json
import pymysql


url='http://sh.lianjia.com/zufang/jiading'

r=requests.get(url)

dom=lxml.html.document_fromstring(r.content)
#conn = pymysql.connect(host='106.75.65.56', port=3306, user='root', passwd='wotou', db='km_data', charset='utf8')
conn = pymysql.Connect(host="202.112.113.203",port=3306,user='sxw',passwd='0845',db='jyzxz',charset='utf8')
cur=conn.cursor()
cur.execute('delete from rent_info where area="'+u'黄浦区'+'"')
content=dom.xpath('//div[@class="option-list sub-option-list gio_plate"]')[0]
pinyin_list=[]
name_list=[]
for tag_a in content.xpath('./a')[1:]:
    pinyin=tag_a.get('gahref')
    name=tag_a.text
    pinyin_list.append(pinyin)
    name_list.append(name)

print pinyin_list

for i in range(len(pinyin_list)):
    pinyin=pinyin_list[i]
    name=name_list[i]

    url='http://soa.dooioo.com/api/v4/online/house/rent/listMapResult?access_token=7poanTTBCymmgE0FOn1oKp&client=pc&' \
        'cityCode=sh&siteType=quyu&type=village&dataId='+pinyin+'&showType=list&limit_count=2000'

    #print url
    r=requests.get(url)
    content = json.loads(r.content)
    for value in content['dataList']:
        try:
            showName=value['showName']
            latitude=value['latitude']
            longitude=value['longitude']
            renttotal=value['rentTotal']

            print showName+':'+str(renttotal)
            cur.execute('insert into rent_info(city,area,sub_area,name,lat,lng,count) values("'+u'上海'+'","'+u'嘉定区'+'","'+name+'","'+showName+'","'+str(latitude)+'","'+str(longitude)+'",'+str(renttotal)+')')
        except:
            continue
    conn.commit()

cur.close()
conn.close()

    # dom=lxml.html.document_fromstring(r.content)
    # print r.content
    # content=dom.xpath('//div[@class="search-list__list"]')
    # print len(content)
    # for li in content:
    #     area_name=li.xpath('./span[1]')[0].text
    #     area_count=li.xpath('./span[2')[0].text
    #     print area_name,area_count




