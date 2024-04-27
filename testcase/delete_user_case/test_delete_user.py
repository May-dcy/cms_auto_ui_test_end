#coding=utf-8
"""
===========================
Author:杭州多测师_王sir
Time:2022-11-19 10:42
website:https://duoceshi.net
===========================
"""

import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.login import login_page
from pages.delete_user import delete_user_page
from utils.get_driver import GetDriver
from pages import login
import allure


@allure.epic("针对删除用户接口的测试")
@allure.feature("删除用户模块")
class TestDelete:

    def setup_class(self):
        self.driver = GetDriver().get_web_driver(login.url)
        self.login = login_page.PageLogin(self.driver)
        self.login.page_login('admin', '123456')
        self.delete_user = delete_user_page.DeleteUser(self.driver)

    def teardown_class(self):
        GetDriver().quit_web_driver()

    @allure.story("用例-删除用户正常场景")
    @allure.description("该用例是针对删除用户正常场景的ui自动化测试")
    @allure.issue("https://duoceshi.net", name="点击，跳转到对应BUG的链接地址")
    def test_delete_user(self):
        self.delete_user.delete_user()
        WebDriverWait(self.driver, timeout=20, poll_frequency=0.5).until(EC.title_is('过期更新'))
        expect = '过期更新'

        # 断言
        try:
            assert self.driver.title == expect
        except Exception as error:
            # 输出错误信息
            # log.error(error)
            # 截图
            self.login.base_get_image("delete_user")
            # 抛出异常
            raise

if __name__ == '__main__':
    pytest.main(["-q", "-s","-v",'test_delete_user.py'])

