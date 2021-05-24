# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class SchoolItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    school_id = Field()
    school_type = Field()
    name = Field()
    address = Field()
    age_range = Field()
    school_fee = Field()
    options = Field()
    internal_link = Field()
    facebook_link = Field()
    district = Field()
    tel = Field()
