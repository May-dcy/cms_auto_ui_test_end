"""用户中心界面元素"""
from selenium.webdriver.common.by import By

#点击用户中心
user_center = By.XPATH,'//*[@id="menu-user"]/dt'
#点击用户管理
user_management = By.XPATH,'//*[@id="menu-user"]/dd/ul/li[1]/a'
#进入第一个iframe框
switch_frame1 = By.XPATH, '//*[@id="iframe_box"]/div[2]/iframe'
#点击添加用户按钮
add_user_btn = By.XPATH, '/html/body/div/div[2]/span[1]/a[2]'
#进入第二个iframe框
switch_frame2 = By.ID,'xubox_iframe1'

"""
添加用户页面元素
"""
# 姓名
name = By.ID, 'userName'
# 手机号码
mobile_phone = By.ID, 'user-tel'
# 邮箱
mail = By.ID, 'user-email'
# 用户名
username = By.ID, 'userAccount'
# 密码
password = By.ID, 'loginPwd'
# 确认密码
confirm_password = By.ID, 'confirmPwd'
# 点击确定
submit_btn = By.ID, 'submitBtn'
# 断言内容
user_info = By.XPATH, '//*[@id="sysUserTab"]/tr[1]/td[5]'