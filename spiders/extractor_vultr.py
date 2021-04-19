from constants.extractor_vultr import VultrEnum
from constants.items import ItemsEnum
from spiders.actuator_get_system import get_system

"""
    Função responsável por extrair os dados do sistema Vultr
"""


def spider_extractor_vultr():
    driver, rows = get_system(VultrEnum.URL, VultrEnum.DATA_XPATH)
    list_ssd_cloud_instances = []
    for row in rows:
        row_data = str(row.text).split('\n')
        if 'IPv6' in row_data: row_data.remove('IPv6')
        ssd_cloud_instances = {
            ItemsEnum.CPU: row_data[2],
            ItemsEnum.MEMORY: row_data[3],
            ItemsEnum.STORAGE: row_data[1],
            ItemsEnum.BANDWIDTH: row_data[4],
            ItemsEnum.PRICE: row_data[5]
        }
        list_ssd_cloud_instances.append(ssd_cloud_instances)

    driver.close()

    return list_ssd_cloud_instances
