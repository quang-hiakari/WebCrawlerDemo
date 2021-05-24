import scrapy
from ..items import SchoolItem
from ..common.common import (
    clean_data,
    get_phone_number,
    get_school_id,
    write_to_file,
    get_district
)

result_list = []
class SchoolSpider(scrapy.Spider):
    name = "school"

    def start_requests(self):
        base_url = "https://kiddihub.com/tim-kiem/da-nang"

        # for i in range (1, 8):
        i = 7
        url = base_url + "?page=" + str(i)
        yield scrapy.Request(url=url, callback=self.parse)

        # local_url = "file:///D:/Project/WebCrawlerDemo/page.html"
        # yield scrapy.Request(url=local_url, callback=self.parse)

    def parse(self, response):
        i = 0
        for item in response.css('div.item-school'):
            school_object = SchoolItem()

            school_object['school_id'] = get_school_id(item.css('div::attr(id)').get())
            school_object['school_type'] = clean_data(item.css('span.school-cate-tag::text').get())
            school_object['address'] = clean_data(item.css('a[data-school-access="address"]::text').get())
            school_object['district'] = get_district(school_object['address'])
            school_object['name'] = clean_data(item.css('span[data-school-access="name"]::text').get())
            school_object['options'] = clean_data(item.css('span.school-option::text').getall())
            school_object['age_range'] = clean_data(item.xpath('//div[@class="right"]//div[@class="right"]/section/text()').get())
            school_object['school_fee'] = clean_data(item.xpath('//div[@class="right"]//div[@class="right"]/section[2]/text()').get())
            
            url_list = item.xpath('//div[@class="center"]/a/@href').extract()
            school_object['internal_link'] = url_list[i]
            i += 1

            #Get contact 
            # yield scrapy.Request(url=school_object['internal_link'], callback=self.parse_information_page, meta={'item': school_object})

            result_list.append(school_object)

            yield school_object
            # Write result to Excel File
            print("MIDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDLe")
            print(len(result_list))
            if len(result_list) == 13:
                write_to_file(result_list)
            print("--------------------------------------------")
        
    def parse_information_page(self, response):
        obj = response.meta['item']
        print("PAGE INFORMATIONNNNNNNNNNNNNNNNNNNN")
        contact_infor = response.css('c-modal#school-contacts')

        for item in contact_infor.css('div.text-center'):
            phone_infor = get_phone_number(item.css('a::attr(href)').get())
            if obj['tel'] == "":
                obj['tel'] = phone_infor
        
        yield obj


