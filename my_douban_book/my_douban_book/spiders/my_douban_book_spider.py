import scrapy
import time
from my_douban_book.items import MyDoubanBookItem
class BookSpider(scrapy.Spider):
    name = 'douban_book'
    allowed_domain = ['douban.com']
    start_urls = ['https://book.douban.com/tag/?view=type&icn=index-sorttags-all']
    cookie = {'bid':'bZoeEecWG3s',
              'll':'"108309"',
              'gr_user_id':'02457720-bc3a-4896-8368-ac43b3476204',
              '_vwo_uuid_v2':'1C31A076950B9C621693510BC3E3492F|3c51720ca2fd8b88d714ad441651199e',
              'viewed':'"27113800_26740503"',
              '__utmc':'30149280',
              'ps':'y',
              'push_noty_num':'0',
              'push_doumail_num':'0',
              '__utmv':'30149280.17340',
              'ap':'1',
              '_ga':'GA1.2.881074325.1515297161',
              'ct':'y',
              '__utmz':'30149280.1518253626.30.16.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
              '__utma':'30149280.881074325.1515297161.1518253626.1518256653.31',
              'gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03':'8c2178bf-31de-4717-8a2d-1039bc6fd799',
              'gr_cs1_8c2178bf-31de-4717-8a2d-1039bc6fd799':'user_id%3A1',
              '__utmb':'30149280.6.10.1518256653',
              'dbcl2':'"173402998:zzHF62tbRgw"',
              'as':'"https://sec.douban.com/b?r=https%3A%2F%2Fbook.douban.com%2F"',
              'ck':'SQ6Z'}
      
   
    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0],cookies=self.cookie)# 这里带着cookie发出请求

    '''


    def start_requests(self):
        return [Request("https://www.douban.com/accounts/login", callback = self.post_login)]  #重写了爬虫类的方法, 实现了自定义请求, 运行成功后会调用callback回调函数

    #FormRequeset
    def post_login(self, response):
        print 'Preparing login'
        #下面这句话用于抓取请求网页后返回网页中的_xsrf字段的文字, 用于成功提交表单
        xsrf = Selector(response).xpath('//input[@name="_xsrf"]/@value').extract()[0]
        print xsrf
        #FormRequeset.from_response是Scrapy提供的一个函数, 用于post表单
        #登陆成功后, 会调用after_login回调函数
        return [FormRequest.from_response(response,   
                            formdata = {
                            '_xsrf': xsrf,
                            'email': '123456',
                            'password': '123456'
                            },
                            callback = self.after_login
                            )]
        '''
    def parse(self,response):
        for tag in response.xpath('//*[@id="content"]/div/div/div/div/table/tbody/tr/td/a'):
            # print(tag.xpath('text()').extract()[0])
            tag_page = 'https://book.douban.com/tag/' + tag.xpath('text()').extract()[0]
            print(tag_page)
            yield scrapy.Request(tag_page,callback=self.parse_tag)
            time.sleep(3)

    def parse_tag(self,response):
        for book in response.xpath('//li[@class="subject-item"]'):
            #print(book.xpath('div[2]/h2/a/text()').extract()[0].strip())
            # //*[@id="subject_list"]/ul/li[1]/div[2]/h2/a
            # //*[@id="subject_list"]/ul/li[1]/div[2]/div[1]
            # //*[@id="subject_list"]/ul/li[2]/div[2]/div[2]/span[2]
            # //*[@id="subject_list"]/ul/li[2]/div[2]/div[2]/span[3]
            # //*[@id="subject_list"]/ul/li[2]/div[2]/p/text()
            doubanbook = MyDoubanBookItem()
            doubanbook['name'] = book.xpath('div[2]/h2/a/text()').extract()[0].strip()
            doubanbook['content'] = book.xpath('div[2]/div[1]/text()').extract()[0].strip()
            doubanbook['score'] = book.xpath('div[2]/div[2]/span[2]/text()').extract()[0].strip()
            doubanbook['judge_people'] = book.xpath('div[2]/div[2]/span[3]/text()').extract()[0].strip()
            a = book.xpath('div[2]/p/text()')
            try:
                doubanbook['introduce'] = book.xpath('div[2]/p/text()').extract()[0].strip()
            except:
                a ==''
            yield doubanbook
        
        np = response.xpath('//span[@class="next"]/a/@href').extract()[0]
        next_page = 'https://book.douban.com'+np
        yield scrapy.Request(next_page,callback=self.parse_tag)
        time.sleep(3)
                                 
        

