from typing import NamedTuple


class VultrEnum(NamedTuple):
    URL = 'https://www.vultr.com/products/cloud-compute/#pricing'
    DATA_XPATH = '//div[@class="pt__row"]'


class VultrItemsEnum(NamedTuple):
    CPU = 'cpu'
    MEMORY = 'memory'
    STORAGE = 'storage'
    BANDWIDTH = 'bandwidth'
    PRICE = 'price'
