import random
import string

def get_random(r_num):
    """
    :param r_num: 长度
    :return: 返回随机长度字母加数字字符串
    """
    return ''.join(random.sample(string.digits + string.ascii_letters, r_num))

if __name__ == '__main__':
    print(get_random(10))


