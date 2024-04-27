import pytest
import os
import time
from utils import send_email

if __name__ == '__main__':
    pytest.main(['-vs', '--alluredir', './tmp', '--clean-alluredir'])
    os.system("allure generate ./tmp --clean")
    time.sleep(10)

    # 判断是否存在，存在先删除
    if os.path.exists('send_report.zip'):
        os.system('del -s -q send_report.zip')
    if os.path.exists('send_report\\allure-report'):
        os.system(r'rmdir /s /q send_report\\allure-report')

    # 移动文件到send_dir里面，allure-2.9.0 已经在了send_dir 不能删除
    os.system('move allure-report send_report')

    # a = send_email.SendEmail('send_report.zip', r'send_report', r"send_report.zip")
    # # 压缩文件夹
    # a.zip_dir()
    # time.sleep(10)
    # # 默认发送当前文件夹下的allure-report.zip
    # # 调取发送邮件接口，传入文件参数
    # a.run()








