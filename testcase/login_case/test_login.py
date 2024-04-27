import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.login import login_page
from utils.get_driver import GetDriver
from pages import login
from utils.read_yaml import read_yaml
from utils.get_log import log
from time import sleep
import allure


@allure.epic("针对登录接口的测试")
@allure.feature("登录模块")
class TestLogin:

    def setup_class(self):
        self.driver = GetDriver().get_web_driver(login.url)
        self.login = login_page.PageLogin(self.driver)

    def teardown_class(self):
        sleep(5)
        GetDriver().quit_web_driver()

    @allure.story("用例-登录正常场景")
    @allure.description("该用例是针对admin用户登录ui自动化的测试")
    @allure.issue("https://duoceshi.net", name="点击，跳转到对应BUG的链接地址")
    @pytest.mark.parametrize('username,password', read_yaml('login.yaml'))
    def test_login(self, username, password):
        self.login.page_login(username, password)

        WebDriverWait(self.driver, timeout=3, poll_frequency=0.5).until(EC.title_is('过期更新'))
        expect = '过期更新'

        # 断言
        try:
            assert self.driver.title == expect
        except Exception as error:
            # 输出错误信息
            # log.error(error)
            # 截图
            self.login.base_get_image("login")
            # 抛出异常
            raise

if __name__ == '__main__':
    pytest.main(['-vs','test_login.py'])




