from selenium import webdriver
from constants.extractor_vultr import VultrEnum,VultrItemsEnum


def spider_extractor_vultr():
    """
    Existe um bug do ChromeDriver ao rodar o selenium pela linha de comando,
    as linhas 9 e 10 contornam esse problema
    """
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.get(VultrEnum.URL)

    rows = driver.find_elements_by_xpath(VultrEnum.DATA_XPATH)
    list_ssd_cloud_instances = []

    for row in rows:
        row_data = str(row.text).split('\n')
        if 'IPv6' in row_data: row_data.remove('IPv6')
        ssd_cloud_instances = {
            VultrItemsEnum.CPU: row_data[2],
            VultrItemsEnum.MEMORY: row_data[3],
            VultrItemsEnum.STORAGE: row_data[1],
            VultrItemsEnum.BANDWIDTH: row_data[4],
            VultrItemsEnum.PRICE: row_data[5]
        }
        list_ssd_cloud_instances.append(ssd_cloud_instances)

    driver.close()

    return list_ssd_cloud_instances
