from selenium.webdriver.common.by import By

# cms系统的URL
url = 'http://cms.duoceshi.cn/cms/manage/login.do'

"""登录界面元素"""
# 用户名输入框
username = By.ID, 'userAccount'
# 密码输入框
password = By.ID, 'loginPwd'
# 登录按钮
login_btn = By.ID, 'loginBtn'








