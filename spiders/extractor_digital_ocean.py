from constants.items import ItemsEnum
from constants.extractor_digital_ocean import DigitalOceanEnum
from spiders.actuator_get_system import get_system

"""
    Função responsável por extrair os dados do sistema Digital Ocean
"""


def spider_extractor_digital_ocean():
    driver, rows = get_system(DigitalOceanEnum.URL, DigitalOceanEnum.DATA_XPATH)
    list_ssd_cloud_instances = []
    for row in rows:
        row_data = str(row.text).split('\n')
        ssd_cloud_instances = {
            ItemsEnum.CPU: row_data[4].split('/')[1].strip(),
            ItemsEnum.MEMORY: row_data[4].split('/')[0].strip(),
            ItemsEnum.SSD_DISK: row_data[5],
            ItemsEnum.TRANSFER: row_data[6],
            ItemsEnum.PRICE: row_data[0] + row_data[1] + row_data[2]
        }
        list_ssd_cloud_instances.append(ssd_cloud_instances)

    driver.close()

    return list_ssd_cloud_instances
