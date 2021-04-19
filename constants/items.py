from typing import NamedTuple


class ItemsEnum(NamedTuple):
    CPU = 'cpu'
    MEMORY = 'memory'
    STORAGE = 'storage'
    BANDWIDTH = 'bandwidth'
    PRICE = 'price'
    TRANSFER = 'transfer'
    SSD_DISK = 'ssd_disk'


class OutputsEnum(NamedTuple):
    VULTR_CSV_FILE = 'outputs/files/vultr/vultr_output.csv'
    DIGITAL_OCEAN_CSV_FILE = 'outputs/files/digital_ocean/digital_ocean.csv'
    VULTR_JSON_FILE = 'outputs/files/vultr/vultr_output.json'
    DIGITAL_OCEAN_JSON_FILE = 'outputs/files/digital_ocean/digital_ocean.json'


class SystemsEnum(NamedTuple):
    VULTR = 'VULTR'
    DIGITAL_OCEAN = "DIGITAL OCEAN"
