import logging.handlers
import os

from config import BASE_PATH


class GetLog:
    # 新建日志器变量
    __logger = None

    # 新建获取日志器的方法
    @classmethod
    def get_logger(cls):
        # 如果日志器为空
        if cls.__logger is None:
            # 获取日志器
            cls.__logger = logging.getLogger()
            # 修改默认级别
            cls.__logger.setLevel(logging.INFO)
            # 日志存放路径
            log_path = BASE_PATH + os.sep + "log" + os.sep + "login_log"
            # 获取处理器
            th = logging.handlers.TimedRotatingFileHandler(filename=log_path,
                                                           when="midnight",
                                                           interval=1,
                                                           backupCount=30,
                                                           encoding="utf-8")
            # 获取格式器
            fmt = "%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s"
            fm = logging.Formatter(fmt)
            # 将格式器添加到处理器中
            th.setFormatter(fm)
            # 将处理器添加到日志器中
            cls.__logger.addHandler(th)
        # 返回日志器
        return cls.__logger


log = GetLog.get_logger()
# log.info("info")
# log.error("error")
