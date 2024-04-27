from time import sleep

from selenium import webdriver

class GetDriver:
    # 声明driver变量
    # 类属性
    __web_driver = None

    # 获取driver方法封装
    @classmethod
    def get_web_driver(cls, url):
        # 如果driver为空
        if cls.__web_driver is None:
            # 实例化driver
            cls.__web_driver = webdriver.Chrome()
            # 最大化浏览器
            cls.__web_driver.maximize_window()
            # 打开网页
            cls.__web_driver.get(url)
        # driver不为空，返回driver
        return cls.__web_driver

    # 退出driver方法封装
    @classmethod
    def quit_web_driver(cls):
        # 如果driver不为空
        if cls.__web_driver is not None:
            # 退出浏览器
            cls.__web_driver.quit()
            # 注意:退出后driver要置空
            cls.__web_driver = None
