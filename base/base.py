import os
import time
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

import config
from utils.get_log import GetLog

log = GetLog.get_logger()

class Base:
    def __init__(self, driver):
        log.info("正在初始化driver：{}".format(driver))
        self.driver = driver

    # 刷新页面
    def refresh(self):
        log.info("刷新页面")
        self.driver.refresh()

    # 浏览器前进
    def forward(self):
        log.info("操作浏览器前进")
        self.driver.forward()

    # 浏览器后退
    def back(self):
        log.info("操作浏览器后退")
        self.driver.back()

    # 查找单个元素方法封装
    def base_find_element(self, loc, timeout=3, poll_frequency=0.5):
        """使用显示等待查找元素"""
        log.info("正在查找元素:{}".format(loc))
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll_frequency).until(lambda x: x.find_element(*loc))

    # 查找多个元素方法封装
    def base_find_elements(self, loc, timeout=3, poll_frequency=0.5):
        """使用显示等待查找元素"""
        log.info("正在查找元素:{}".format(loc))
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll_frequency).until(lambda x: x.find_elements(*loc))

    # 当前页面title
    def base_title(self):
        log.info("页面标题为:{}".format(self.driver.title))
        return self.driver.title

    # 当前页面的URL
    def base_url(self):
        log.info("当前页面URL为:{}".format(self.driver.current_url))
        return self.driver.current_url

    # 点击元素方法封装
    def base_click_element(self, loc):
        log.info("正在点击元素:{}".format(loc))
        self.base_find_element(loc).click()

    # 输入方法封装
    def base_input(self, loc, value):
        """
        :param loc:
        :param value: 输入的内容
        :return:
        """
        # 寻找元素
        element = self.base_find_element(loc)
        log.info("正在对元素:{}执行清空操作".format(loc))
        # 清空输入内容
        element.clear()
        # 输入内容
        log.info("正在对元素:{}执行输入:{}操作".format(loc, value))
        element.send_keys(value)

    # 上传文件方法封装
    def base_upload(self, loc, value):
        """
        :param loc:
        :param value: 上传的文件
        :return:
        """
        # 寻找元素
        element = self.base_find_element(loc)
        # 输入内容
        log.info("正在对元素:{}执行上传:{}操作".format(loc, value))
        element.send_keys(value)

    # 下拉选择方法封装
    def base_select(self, loc, value):
        # 寻找元素
        element = self.base_find_element(loc)
        se = Select(element)
        se.select_by_value(value)

    # 获取文本方法封装
    def base_get_text(self, loc):
        log.info("正在对:{}元素获取文本操作，文本值为：{}".format(loc, self.base_find_element(loc).text))
        return self.base_find_element(loc).text

    # 获取元素尺寸
    def base_get_size(self, loc):
        log.info("正在对:{}元素获取尺寸操作，文本值为：{}".format(loc, self.base_find_element(loc).size))
        return self.base_find_element(loc).size

    # 截图方法封装
    def base_get_image(self, info):
        """
        :param info:断言失败时的说明
        :return:
        """
        # 调用截图方法
        log.error("断言出错，正在执行截图操作")
        # 图片名称
        file_name = config.BASE_PATH + os.sep + 'screenshots/%s.png' % (time.strftime('%Y_%m_%d %H_%M_%S'))
        # 保存图片
        self.driver.get_screenshot_as_file(file_name)
        # 打开图片
        with open(file_name, mode='rb') as f:
            file = f.read()
        # 将图片添加到测试报告中
        allure.attach(file, info, allure.attachment_type.PNG)

    # 判断元素是否存在
    def base_element_is_exist(self, loc):
        try:
            self.base_find_element(loc, timeout=3)
            # 返回True,代表元素存在
            log.info("{}元素存在".format())
            return True
        except:
            # 返回False,代表元素不存在
            log.info("{}元素不存在".format(loc))
            return False

    # 鼠标操作-悬停
    def base_move_to_element(self, loc):
        ActionChains(self.driver).move_to_element(self.driver.base_find_element(loc)).perform()

    # 鼠标操作-悬停到指定偏移量
    def base_move_to_element_with_offset(self, loc, x, y):
        """
        :param loc:
        :param x: 向X轴偏移量
        :param y: 向Y轴偏移量
        :return:
        """
        ActionChains(self.driver).move_to_element_with_offset(self.base_find_element(loc), x, y).perform()

    # 鼠标操作-右击
    def base_context_click(self, loc):
        ActionChains(self.driver).context_click(self.base_find_element(loc)).perform()

    # 鼠标操作-单击
    def base_click(self, loc):
        ActionChains(self.driver).click(self.base_find_element(loc)).perform()

    # 鼠标操作-双击
    def base_double_click(self, loc):
        ActionChains(self.driver).double_click(self.base_find_element(loc)).perform()

    # 鼠标操作-拖动
    def base_drag_and_drop(self, loc1, loc2):
        ActionChains(self.driver).drag_and_drop(self.base_find_element(loc1), self.base_find_element(loc2)).perform()

    # 进入frame弹框方法封装
    def base_switch_frame(self,loc):
        element = self.base_find_element(loc)
        log.info("正在查找元素:{}".format(loc))
        self.driver.switch_to.frame(element)

    # 退出frame主文档弹框方法封装
    def base_switch_to_default_content(self):
        self.driver.switch_to_default_content()

    # 退出frame父文档弹框方法封装(相当于后退)
    def base_switch_to_parent_frame(self):
        self.driver.switch_to.parent_frame()

    # 刷新页面方法封装
    def base_refresh(self):
        self.driver.refresh()



