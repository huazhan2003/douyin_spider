from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def get_home_page(url, wait_time):
    home_info = []  # 达人主页信息
    # 设置 Chrome 为无头模式
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    # 启动 Chrome 浏览器
    driver = webdriver.Chrome(options=chrome_options)
    try:
        # 打开网页
        driver.get(url)
        # 等待页面加载（你可能需要根据页面实际情况调整等待时间）
        driver.implicitly_wait(wait_time)
        # 获取粉丝数量
        fans_element = driver.find_element(By.XPATH, '//*[@id="douyin-right-container"]/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]')
        fans_text = fans_element.text
        home_info.append(fans_text)
        # 获取抖音号
        id_element = driver.find_element(By.XPATH, '//*[@id="douyin-right-container"]/div[2]/div/div/div[2]/div[2]/p/span[1]')
        id = id_element.text
        home_info.append(id)
        # 获取主页简介
        summary_element = driver.find_element(By.XPATH, '//*[@id="douyin-right-container"]/div[2]/div/div/div[2]/div[2]/div[3]/div/span/span/span/span/span/span')
        summary = summary_element.text
        home_info.append(summary)
        driver.close()
    finally:
        # 关闭浏览器
        driver.quit()
    return home_info

