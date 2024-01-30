# _*_ coding : utf-8 _*_
# @Time : 2024/1/28 16:25
# @Author Jared
# @File seleniumUtil
# @Project seleniumTest
import time
# 导入selenium包
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class SeleniumUtil:
    # 设置驱动路径
    executable_path = r"Driver\chromedriver.exe"

    # 创建一个Service对象，传入浏览器驱动的路径
    service = Service(executable_path)

    # 初始化驱动
    def initDriver(self, service=None):

        # 防止浏览器自动关闭
        option = webdriver.ChromeOptions()
        option.add_experimental_option("detach", True)

        # 传入service和options参数
        self.browser = webdriver.Chrome(service=service, options=option)

    # 退出
    def quit(self):
        self.browser.quit()

    # 获取浏览器实例
    def getBrowser(self):
        return self.browser

    def __init__(self):
        self.initDriver()
