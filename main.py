# _*_ coding : utf-8 _*_
# @Time : 2024/1/28 16:23
# @Author Jared
# @File main
# @Project seleniumTest
from selenium.webdriver.common.by import By

import searchUtil
# 在主程序中导入自定义模块
import seleniumUtil
import time

util = seleniumUtil.SeleniumUtil()
browser = util.getBrowser()
browser.get("https://www.baidu.com")

# 当前分支:

print("hot-fix")

print("master")


# 构造一个搜索的对象
searchText = searchUtil.Search()

time.sleep(3)

# 输入框中输入关键字
browser.find_element(By.XPATH,'//*[@id="kw"]').send_keys(searchText.searchText)

# 点击查询按钮
browser.find_element(By.ID,"su").click()

#
util.quit()
