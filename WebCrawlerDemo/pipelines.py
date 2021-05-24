# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from .common.common import write_to_file
from scrapy.exceptions import DropItem

class WebcrawlerdemoPipeline:
    def process_item(self, item, spider):
        adaper = ItemAdapter(item)
        if adaper['id'] in self.ids_seen:
            raise DropItem(f"Duplicate item found: {item/r}")
        else:
            self.ids_seen.add(adaper['id'])
        return item
