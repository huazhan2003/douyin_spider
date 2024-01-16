from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def get_video_page(url, wait_time):
    video_info = []  # 视频界面信息
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
        # 获取视频文案
        title_element = driver.find_element(By.XPATH, '//*[@id="douyin-right-container"]/div[2]/div/div[1]/div[3]/div/div[1]/div/h1/span/span[2]/span/span[1]/span/span/span')
        title_text = title_element.text
        video_info.append(title_text)
        # 获取昵称
        nickname_element = driver.find_element(By.XPATH, '//*[@id="douyin-right-container"]/div[2]/div/div[1]/div[4]/div/div[1]/div[2]/a/div/span/span/span/span/span/span')
        nickname_text = nickname_element.text
        video_info.append(nickname_text)
        # 获取主页链接
        homelink = driver.find_element(By.CSS_SELECTOR, 
        '#douyin-right-container > div:nth-child(2) > div > div.leftContainer.gkVJg5wr > div.JBvFTwr7 > div > div.UbblxGZr > div.WdX5lXbX > a').get_attribute('href')
        video_info.append(homelink)
        driver.close()
    finally:
        # 关闭浏览器
        driver.quit()
    return video_info
