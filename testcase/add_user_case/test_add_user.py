import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages import add_user
from pages.login import login_page
from pages.add_user import add_user_page
from utils.get_driver import GetDriver
from pages import login
from utils.read_yaml import read_yaml
import allure

@allure.epic("针对添加用户接口的测试")
@allure.feature("添加用户模块")
class TestAddUser:

    def setup_class(self):
        self.driver = GetDriver().get_web_driver(login.url)
        self.login = login_page.PageLogin(self.driver)
        self.login.page_login('admin', '123456')
        self.add_user = add_user_page.AddUser(self.driver)

    def teardown_class(self):
        GetDriver().quit_web_driver()

    @allure.story("用例-添加用户正常场景")
    @allure.description("该用例是针对添加用户正常场景的ui自动化测试")
    @allure.issue("https://duoceshi.net", name="点击，跳转到对应BUG的链接地址")
    @pytest.mark.parametrize('name,mobile_phone,mail,username,password,confirm_password', read_yaml('add_user.yaml'))
    def test_add_user(self, name,mobile_phone,mail,username,password,confirm_password):
        self.add_user.add_user(name,mobile_phone,mail,username,password,confirm_password)
        loc = add_user.user_info
        WebDriverWait(self.driver, timeout=20, poll_frequency=0.5).until(EC.visibility_of_element_located(loc))
        value = self.login.driver.find_element(*loc).text

        # 断言
        try:
            assert value == mobile_phone
        except Exception as error:
            # 输出错误信息
            # log.error(error)
            # 截图
            self.login.base_get_image("add_user")
            # 抛出异常
            raise

if __name__ == '__main__':
    pytest.main(['-vs','test_add_user.py'])

