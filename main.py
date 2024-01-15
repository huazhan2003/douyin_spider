import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from home_page import get_home_page
from video_page import get_video_page

# 参数，自行根据需求修改
key_word = '美容仪'  # 内容关键词
down_step = 4  # 1-99之间，越小爬取内容越多
wait_time = 1  # 等待网页加载时间

# 滑动操作
def drop_down(down_step):
    # 执行页面滚动操作
    for x in range(1, 100, down_step): 
        j = x / 9
        # document.documentElement.scrollTop 指定滚动条的位置
        # document.documentElement.scrollHeight 获取浏览器页面的最大高度
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        driver.execute_script(js)
        time.sleep(2)


if __name__ == "__main__":
    # 打开网页，滑动窗口，显示更多的视频
    driver = webdriver.Chrome()
    driver.get(f'https://www.douyin.com/search/{key_word}?type=video')
    time.sleep(3)
    drop_down(down_step)

    # 视频文案、视频链接、昵称
    titles = []  # 视频文案
    li_urls = []  # 视频链接
    nicknames = []  # 昵称
    fans_nums = []  # 粉丝量
    douyin_ids = []  # 抖音号
    summaries = []  # 简介
    home_links = []  # 主页链接

    # 获得所有要爬取的视频链接
    lis = driver.find_elements(By.CSS_SELECTOR, '#search-content-area > div > div.HHwqaG_P > div:nth-child(1) > ul li')
    for li in lis:
        li_url = li.find_element(By.CSS_SELECTOR,'a').get_attribute('href')
        print(li_url)
        li_urls.append(li_url)
    
    # 获取视频文案、昵称、主页链接
    for li_url in li_urls:
        title = get_video_page(li_url, wait_time)[0]
        nickname = get_video_page(li_url, wait_time)[1]
        home_link = get_video_page(li_url, wait_time)[2]
        titles.append(title)
        nicknames.append(nickname)
        home_links.append(home_link)

    # 获取粉丝数量、抖音号、简介
    for home_link in home_links:
        fans_num = get_home_page(home_link, wait_time)[0]
        douyin_id = get_home_page(home_link, wait_time)[1]
        summary = get_home_page(home_link, wait_time)[2]
        fans_nums.append(fans_num)
        douyin_ids.append(douyin_id)
        summaries.append(summary)

    # 创建一个DataFrame
    df = pd.DataFrame({
        '视频文案': titles,
        '视频链接': li_urls,
        '昵称': nicknames,
        '粉丝量': fans_nums,
        '抖音号': douyin_ids,
        '简介': summaries,
        '主页链接': home_links
    })

    # 将DataFrame写入Excel文件
    df.to_excel('output.xlsx', index=True)
    driver.quit()
