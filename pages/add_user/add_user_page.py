from pages import add_user
from base.base import Base
from utils.get_log import GetLog

log = GetLog.get_logger()

class AddUser(Base):

    # 点击用户中心
    def page_click_user_center(self):
        self.base_click_element(add_user.user_center)

    # 点击用户管理
    def page_click_user_management(self):
        self.base_click_element(add_user.user_management)

    # 进入到第一个frame弹框
    def page_switch_frame1(self):
        self.base_switch_frame(add_user.switch_frame1)

    # 点击添加用户按钮
    def page_click_add_user_btn(self):
        self.base_click_element(add_user.add_user_btn)

    # 进入到第二个frame弹框
    def page_switch_frame2(self):
        self.base_switch_frame(add_user.switch_frame2)

    # 输入姓名
    def page_input_name(self, name):
        self.base_input(add_user.name, name)

    # 输入手机号码
    def page_input_mobile_phone(self, mobile_phone):
        self.base_input(add_user.mobile_phone, mobile_phone)

    # 输入邮箱
    def page_mail(self,mail):
        self.base_input(add_user.mail,mail)

    # 输入用户名
    def page_username(self,username):
        self.base_input(add_user.username,username)

    # 输入密码
    def page_password(self,password):
        self.base_input(add_user.password, password)

    # 输入确认密码
    def page_confirm_password(self,confirm_password):
        self.base_input(add_user.confirm_password, confirm_password)

    # 点击确定
    def page_submit_btn(self):
        self.base_click_element(add_user.submit_btn)

    # 回到上个iframe弹框
    def page_switch_to_parent_frame(self):
        self.base_switch_to_parent_frame()

    # 刷新页面
    def page_refresh(self):
        self.base_refresh()


    # 组装业务方法
    def add_user(self,name,mobile_phone,mail,username,password,confirm_password):
        log.info("正在调用新增用户方法，姓名为：{}".format(name))
        self.page_click_user_center()
        self.page_click_user_management()
        self.page_switch_frame1()
        self.page_click_add_user_btn()
        self.page_switch_frame2()
        self.page_input_name(name)
        self.page_input_mobile_phone(mobile_phone)
        self.page_mail(mail)
        self.page_username(username)
        self.page_password(password)
        self.page_confirm_password(confirm_password)
        self.page_submit_btn()
        self.page_switch_to_parent_frame()
        self.page_refresh()
        self.page_click_user_center()
        self.page_click_user_management()
        self.page_switch_frame1()



"""
元素层
流程层
用例层

"""
