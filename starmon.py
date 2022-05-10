
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pdb import set_trace
mobilesetting={"deviceName":"iPhone 6 Plus"}
options=webdriver.ChromeOptions()  #选项
options.add_experimental_option("mobileEmulation",mobilesetting)  #模拟手机
driver=webdriver.Chrome(chrome_options=options)  #配置参数
driver.get('https://market.starmon.io/nft/pet')
# 翻页效果
next_element = '//*[@id="app"]/div[2]/div/div/div[2]/div[2]/div/div[2]/div[2]/ul/li[7]/a'
wait = WebDriverWait(driver,10,0.5)
wait.until(lambda diver:driver.find_element_by_xpath(next_element))
def parse_detail(driver):
    tag_element = '//*[@id="app"]/div[2]/div/div/div[2]/div/div/div[1]/section/div[1]/div[1]'
    tag = driver.find_element_by_xpath(tag_element).text
    if "egg" in tag.lower():
        res = parse_egg(driver)
        set_trace()

def parse_egg(driver):
    
    price_element = '//*[@id="app"]/div[2]/div/div/div[2]/div/div/div[1]/div[3]/div/span[1]'
    time_element = '//*[@id="app"]/div[2]/div/div/div[2]/div/div/div[2]/section[1]/div[2]/div[2]/div[1]'
    father_element = '//*[@id="app"]/div[2]/div/div/div[2]/div/div/div[2]/section[2]/div[2]/a[1]'
    mother_element = '//*[@id="app"]/div[2]/div/div/div[2]/div/div/div[2]/section[2]/div[2]/a[2]'
    price = driver.find_elements_by_xpath(price_element).text
    time = driver.find_elements_by_xpath(time_element).text
    mother = driver.find_elements_by_xpath(father_element)
    father = driver.find_elements_by_xpath(mother_element)
    return price, time, father, mother

def find_mon(driver):
    # driver.find_element_by_xpath(next_element).click()
    mon_url = '//*[@id="app"]/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/a'
    all_mons = driver.find_elements_by_xpath(mon_url)
    for mon in all_mons:
        mon.click()
        parse_detail(driver)

find_mon(driver)
