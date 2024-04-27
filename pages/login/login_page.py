from pages import login
from base.base import Base
from utils.get_log import GetLog

log = GetLog.get_logger()

class PageLogin(Base):
    # 输入用户名
    def page_input_username(self, username):
        self.base_input(login.username, username)

    # 输入密码
    def page_input_password(self, password):
        self.base_input(login.password, password)

    # 点击登录
    def page_click_login(self):
        self.base_click_element(login.login_btn)

    # 组装业务方法
    def page_login(self, username, password):
        log.info("正在调用登录业务方法，用户名为：{}，密码为：{}".format(username, password))
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_click_login()