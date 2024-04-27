#coding=utf-8
"""
===========================
Author:杭州多测师_王sir
Time:2022-11-19 10:21
website:https://duoceshi.net
===========================
"""

"""用户中心界面元素"""
from selenium.webdriver.common.by import By

#点击用户中心
user_center = By.XPATH,'//*[@id="menu-user"]/dt'
#点击用户管理
user_management = By.XPATH,'//*[@id="menu-user"]/dd/ul/li[1]/a'
#进入第一个iframe框
switch_frame1 = By.XPATH, '//*[@id="iframe_box"]/div[2]/iframe'


"""
删除用户页面元素
"""
# 删除按钮
delete_btn = By.XPATH, '//*[@title="删除"]'
# 确定删除按钮
confirm_delete_btn = By.CSS_SELECTOR, '.xubox_yes'

# 断言内容
