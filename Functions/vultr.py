from selenium import webdriver


def vultr():
    """
    Existe um bug do ChromeDriver ao rodar o selenium pela linha de comando,
    as linhas 9 e 10 contornam esse problema
    """
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.vultr.com/products/cloud-compute/#pricing')
    rows = driver.find_elements_by_xpath('//div[@class="pt__row"]')
    list_ssd_cloud_instances = []

    for row in rows:
        row_data = str(row.text).split('\n')
        if 'IPv6' in row_data: row_data.remove('IPv6')
        ssd_cloud_instances = {
            "cpu": row_data[2],
            "memory": row_data[3],
            "storage": row_data[1],
            "bandwidth": row_data[4],
            "price": row_data[5]
        }
        list_ssd_cloud_instances.append(ssd_cloud_instances)


    driver.close()

    return list_ssd_cloud_instances
