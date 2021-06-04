#4.定义一个start.py,启用文件展示最终存款金额
from salary_test.select_money import select_money
from salary_test.send_money import send_money

if __name__ == '__main__':
    send_money(1000)
    select_money()