from selenium import webdriver


def first_step():
    driver = webdriver.Chrome()
    driver.get('https://www.vultr.com/products/cloud-compute/#pricing')
    rows = driver.find_elements_by_xpath('//div[@class="pt__row"]')

    for row in rows:
        row_data = str(row.text).split('\n')
        if 'IPv6' in row_data: row_data.remove('IPv6')
        ssd_cloud_instances = {
            'cpu': row_data[2],
            'memory': row_data[3],
            'storage': row_data[1],
            'bandwidth': row_data[4],
            'price': row_data[5]
        }
        print(ssd_cloud_instances)

    driver.close()
