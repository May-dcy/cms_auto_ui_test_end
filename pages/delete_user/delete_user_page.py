#coding=utf-8
"""
===========================
Author:杭州多测师_王sir
Time:2022-11-19 10:21
website:https://duoceshi.net
===========================
"""

from pages import delete_user
from base.base import Base
from utils.get_log import GetLog

log = GetLog.get_logger()

class DeleteUser(Base):

    # 点击用户中心
    def page_click_user_center(self):
        self.base_click_element(delete_user.user_center)

    # 点击用户管理
    def page_click_user_management(self):
        self.base_click_element(delete_user.user_management)

    # 进入到第一个frame弹框
    def page_switch_frame1(self):
        self.base_switch_frame(delete_user.switch_frame1)

    # 点击删除
    def page_click_delete_btn(self):
        self.base_click_element(delete_user.delete_btn)

    # 点击确定
    def page_click_confirm_delete_btn(self):
        self.base_click_element(delete_user.confirm_delete_btn)

    # 组装业务方法
    def delete_user(self):
        log.info("=========正在调用删除用户方法==========")
        self.page_click_user_center()
        self.page_click_user_management()
        self.page_switch_frame1()
        self.page_click_delete_btn()
        self.page_click_confirm_delete_btn()



